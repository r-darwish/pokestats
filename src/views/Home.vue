<template>
  <div class="home">
    <p>Insert a pokemon name in English or Hebrew:</p>
    <br />
    <input v-model="pokemonFilter" placeholder="Pokemon" />
    <ul v-if="shouldSearch">
      <li
        v-for="pokemon in filteredData"
        :key="pokemon"
      >{{pokemon.hebrewName}} / {{pokemon.englishName}}</li>
    </ul>
  </div>
</template>

<script lang="ts">
interface Pokemon {
  hebrewName: string;
  englishName: string;
}

export default {
  name: "Home",
  components: {},
  data() {
    const pokemonData: Pokemon[] = [];

    return { pokemonFilter: "", pokemons: pokemonData };
  },
  computed: {
    shouldSearch(): boolean {
      return this.pokemonFilter.length > 3;
    },
    filteredData(): Pokemon[] {
      return this.pokemons.filter(
        pokemon =>
          pokemon.hebrewName.includes(this.pokemonFilter) ||
          pokemon.englishName.includes(this.pokemonFilter)
      );
    }
  }
};
</script>