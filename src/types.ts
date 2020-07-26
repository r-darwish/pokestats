enum PokemonType {
    Fire = "Fire"
}

interface Pokemon {
    hebrewName: string;
    englishName: string;
    linkId: number;
    imageId: number;
    weaknessess: PokemonType[];
    majorWeaknessess: PokemonType[];
    resistancess: PokemonType[];
}

export { PokemonType, Pokemon };