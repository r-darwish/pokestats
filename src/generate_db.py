#!/usr/bin/env python

import pprint
from typing import List
from aiohttp import ClientSession
from bs4 import BeautifulSoup
from asyncio import get_event_loop, Semaphore, gather
import re
from itertools import zip_longest
from dataclasses import dataclass


@dataclass
class ShortStats:
    image_id: str
    link_id: int


@dataclass
class Pokemon:
    short_stats: ShortStats
    english_name: str
    hebrew_name: str


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
            image_id = pic.find("img").attrs["src"].split("/")[-1].replace(".png", "")

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
        hebrew_name, english_name = [
            td.text
            for td in soup.find("div", class_="entry").find("table").find_all("td")[2:]
        ]

        return Pokemon(
            short_stats=stats, english_name=english_name, hebrew_name=hebrew_name
        )


async def main():
    async with ClientSession() as session:
        basic_db = await get_basic_db(session)
        rate_limit = Semaphore(5)
        all_db: List[Pokemon] = await gather(
            *[
                get_pokemon_info(stats, session=session, rate_limit=rate_limit)
                for stats in basic_db[:10]
            ]
        )
        pprint.pprint(all_db)


if __name__ == "__main__":
    get_event_loop().run_until_complete(main())
