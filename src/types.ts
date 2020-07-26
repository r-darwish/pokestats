enum PokemonType {
    Normal = "Normal",
    Fire = "Fire",
    Water = "Water",
    Electricity = "Electricity",
    Grass = "Grass",
    Ice = "Ice",
    Fighting = "Fighting",

    Poison = "Poison",
    Earth = "Earth",
    Flying = "Flying",
    Psychic = "Psychic",
    Bug = "Bug",
    Rock = "Rock",
    Ghost = "Ghost",

    Dragon = "Dragon",
    Dark = "Dark",
    Metal = "Metal",
    Fairy = "Fairy",
    Science = "Science",
    Culture = "Culture",
    Religion = "Religion",
}

interface Pokemon {
    hebrewName: string;
    englishName: string;
    linkId: number;
    imageId: string;
    weaknesses: PokemonType[];
    majorWeaknesses: PokemonType[];
    resistancess: PokemonType[];
}

export { PokemonType, Pokemon };