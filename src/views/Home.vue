<template>
  <div class="home">
    <p>Insert a pokemon name in English or Hebrew:</p>
    <br />
    <input v-model="pokemonFilter" placeholder="Pokemon" autofocus />
    <div v-if="shouldSearch">
      <div v-for="pokemon in filteredData" :key="pokemon" class="pokemon">
        <h3>{{pokemon.hebrewName}} / {{pokemon.englishName}}</h3>
        <a :href="`https://www.pocketmonsters.co.il/?p=${pokemon.linkId}`" target="_blank">
          <img :src="pokemon.imageId" />
        </a>
        <div class="container" v-if="pokemon.majorWeaknesses.length">
          Major Weaknesses:
          <img
            v-for="t in pokemon.majorWeaknesses"
            :key="t"
            :src="t"
            class="pokemon-type"
          />
        </div>
        <div class="container">
          Weaknesses:
          <img v-for="t in pokemon.weaknesses" :key="t" :src="t" class="pokemon-type" />
        </div>
        <div class="container">
          Resistancess:
          <img
            v-for="t in pokemon.resistancess"
            :key="t"
            :src="t"
            class="pokemon-type"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  align-items: center;
  margin-bottom: 0.5em;
  justify-content: center;
}

.pokemon-type {
  margin-left: 0.2em;
}

.pokemon {
  margin-bottom: 5em;
}
</style>

<script lang="ts">
import { Component, Vue, Watch } from "vue-property-decorator";
import data from "../db";
import { Pokemon } from "../types";

@Component({})
export default class Home extends Vue {
  private pokemonFilter = "";

  get shouldSearch(): boolean {
    return this.pokemonFilter.length >= 3;
  }
  get filteredData(): Pokemon[] {
    return data.filter(
      pokemon =>
        pokemon.hebrewName.includes(this.pokemonFilter) ||
        pokemon.englishName
          .toLowerCase()
          .includes(this.pokemonFilter.toLowerCase())
    );
  }
}
</script>