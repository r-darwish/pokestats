#!/usr/bin/env python

from typing import List
from aiohttp import ClientSession
from bs4 import BeautifulSoup
from asyncio import get_event_loop, Semaphore, gather
from itertools import zip_longest
from enum import Enum, auto
from dataclasses import dataclass


@dataclass
class ShortStats:
    image_id: str
    link_id: int


class PokemonType(Enum):
    Normal = auto()
    Fire = auto()
    Water = auto()
    Electricity = auto()
    Grass = auto()
    Ice = auto()
    Fighting = auto()

    Poison = auto()
    Earth = auto()
    Flying = auto()
    Psychic = auto()
    Bug = auto()
    Rock = auto()
    Ghost = auto()

    Dragon = auto()
    Dark = auto()
    Metal = auto()
    Farie = auto()
    Science = auto()
    Culture = auto()
    Religion = auto()


@dataclass
class Pokemon:
    short_stats: ShortStats
    english_name: str
    hebrew_name: str
    major_weaknesses: List[PokemonType]
    weaknesses: List[PokemonType]
    resistancess: List[PokemonType]


def grouper(iterable, n):
    args = [iter(iterable)] * n
    return zip_longest(*args)


async def get_basic_db(session: ClientSession) -> List[ShortStats]:
    db: List[ShortStats] = []
    response = await session.get("https://www.pocketmonsters.co.il/?p=87980")
    response.raise_for_status()
    soup = BeautifulSoup(await response.text(), features="html.parser")
    entry = soup.find("div", class_="entry")
    for (pics_row, _) in grouper(entry.find_all("tr"), 2):
        for pic in pics_row.find_all("td"):
            link = pic.find("a")
            if not link:
                break
            link_id = int(link.attrs["href"].split("=")[1])
            image_id = pic.find("img").attrs["src"]

            db.append(ShortStats(image_id=image_id, link_id=link_id,))

    return db


async def get_pokemon_info(
    stats: ShortStats, *, session: ClientSession, rate_limit: Semaphore
) -> Pokemon:
    async with rate_limit:
        response = await session.get(
            f"https://www.pocketmonsters.co.il/?p={stats.link_id}"
        )
        response.raise_for_status()
        soup = BeautifulSoup(await response.text(), features="html.parser")
        tables = soup.find("div", class_="entry").find_all("table")
        hebrew_name, english_name = [td.text for td in tables[0].find_all("td")[2:]]

        types_table = tables[6]
        weaknesses: List[PokemonType] = []
        major_weaknesses: List[PokemonType] = []
        resistancess: List[PokemonType] = []
        types_iterator = iter(PokemonType)
        for _, tr in grouper(types_table.find_all("tr"), 2):
            for td, pokemon_type in zip(tr.find_all("td"), types_iterator):
                value: str = td.text
                if "/" in value or float(value) == 0:
                    resistancess.append(pokemon_type)
                else:
                    value = int(value)
                    if value == 2:
                        weaknesses.append(pokemon_type)
                    elif value > 2:
                        major_weaknesses.append(pokemon_type)
                    else:
                        assert int(value) == 1

        return Pokemon(
            short_stats=stats,
            english_name=english_name,
            hebrew_name=hebrew_name,
            major_weaknesses=major_weaknesses,
            resistancess=resistancess,
            weaknesses=weaknesses,
        )


def type_list_to_ts(type_list: List[PokemonType]) -> str:
    return "[" + ", ".join(str(t) for t in type_list) + "]"


def into_ts(pokemon: Pokemon) -> str:
    return f"""{{
        hebrewName: "{pokemon.hebrew_name}",
        englishName: "{pokemon.english_name}",
        imageId: "{pokemon.short_stats.image_id}",
        linkId: {pokemon.short_stats.link_id},
        majorWeaknesses: {type_list_to_ts(pokemon.major_weaknesses)},
        weaknesses: {type_list_to_ts(pokemon.weaknesses)},
        resistancess: {type_list_to_ts(pokemon.resistancess)},
    }}"""


async def main():
    async with ClientSession() as session:
        basic_db = await get_basic_db(session)
        rate_limit = Semaphore(5)
        all_db: List[Pokemon] = await gather(
            *[
                get_pokemon_info(stats, session=session, rate_limit=rate_limit)
                for stats in basic_db
            ]
        )

        with open("db.ts", "w", encoding="utf-8") as f:
            f.write(
                """import { Pokemon, PokemonType } from "./types";

const data: Pokemon[] = [
    """
            )
            for pokemon in all_db:
                f.write(f"{into_ts(pokemon)},")

            f.write(
                """];
            
            export default data;
            """
            )


if __name__ == "__main__":
    get_event_loop().run_until_complete(main())
