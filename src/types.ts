enum PokemonType {
    Normal = "https://www.pocketmonsters.co.il/wp-content/uploads/2020/01/%D7%A0%D7%95%D7%A8%D7%9E%D7%9C%D7%99.png",
    Fire = "https://www.pocketmonsters.co.il/wp-content/uploads/2020/01/%D7%90%D7%A9.png",
    Water = "https://www.pocketmonsters.co.il/wp-content/uploads/2020/01/%D7%9E%D7%99%D7%9D.png",
    Electricity = "https://www.pocketmonsters.co.il/wp-content/uploads/2020/01/%D7%97%D7%A9%D7%9E%D7%9C.png",
    Grass = "https://www.pocketmonsters.co.il/wp-content/uploads/2020/01/%D7%A2%D7%A9%D7%91.png",
    Ice = "https://www.pocketmonsters.co.il/wp-content/uploads/2020/01/%D7%A7%D7%A8%D7%97.png",
    Fighting = "https://www.pocketmonsters.co.il/wp-content/uploads/2020/01/%D7%9C%D7%97%D7%99%D7%9E%D7%94.png",

    Poison = "https://www.pocketmonsters.co.il/wp-content/uploads/2020/01/%D7%A8%D7%A2%D7%9C.png",
    Earth = "https://www.pocketmonsters.co.il/wp-content/uploads/2020/01/%D7%90%D7%93%D7%9E%D7%94.png",
    Flying = "https://www.pocketmonsters.co.il/wp-content/uploads/2020/01/%D7%9E%D7%A2%D7%95%D7%A4%D7%A3.png",
    Psychic = "https://www.pocketmonsters.co.il/wp-content/uploads/2020/01/%D7%A2%D7%9C-%D7%97%D7%95%D7%A9%D7%99.png",
    Bug = "https://www.pocketmonsters.co.il/wp-content/uploads/2020/01/%D7%97%D7%A8%D7%A7.png",
    Rock = "https://www.pocketmonsters.co.il/wp-content/uploads/2020/01/%D7%90%D7%91%D7%9F.png",
    Ghost = "https://www.pocketmonsters.co.il/wp-content/uploads/2020/01/%D7%A8%D7%95%D7%97.png",

    Dragon = "https://www.pocketmonsters.co.il/wp-content/uploads/2020/01/%D7%93%D7%A8%D7%A7%D7%95%D7%9F.png",
    Dark = "https://www.pocketmonsters.co.il/wp-content/uploads/2020/01/%D7%90%D7%95%D7%A4%D7%9C.png",
    Metal = "https://www.pocketmonsters.co.il/wp-content/uploads/2020/01/%D7%9E%D7%AA%D7%9B%D7%AA.png",
    Fairy = "https://www.pocketmonsters.co.il/wp-content/uploads/2020/01/%D7%A4%D7%99%D7%94.png",
    Science = "https://www.pocketmonsters.co.il/wp-content/uploads/2020/04/%D7%9E%D7%93%D7%A2.png",
    Culture = "https://www.pocketmonsters.co.il/wp-content/uploads/2020/04/%D7%AA%D7%A8%D7%91%D7%95%D7%AA.png",
    Religion = "https://www.pocketmonsters.co.il/wp-content/uploads/2020/04/%D7%93%D7%AA.png",
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