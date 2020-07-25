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
      const self = this as any;
      return self.pokemonFilter.length > 3;
    },
    filteredData(): Pokemon[] {
      const self = this as any;
      return self.pokemons.filter(
        (pokemon: Pokemon) =>
          pokemon.hebrewName.includes(self.pokemonFilter) ||
          pokemon.englishName.includes(self.pokemonFilter)
      );
    }
  }
};
</script>