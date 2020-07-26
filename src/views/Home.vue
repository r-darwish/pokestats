<template>
  <div class="home">
    <p>Insert a pokemon name in English or Hebrew:</p>
    <br />
    <input v-model="pokemonFilter" placeholder="Pokemon" autofocus />
    <div v-if="shouldSearch">
      <div v-for="pokemon in filteredData" :key="pokemon">
        <a :href="`https://www.pocketmonsters.co.il/?p=${pokemon.linkId}`" target="_blank">
          <img :src="pokemon.imageId" />
        </a>
        <br />
        {{pokemon.hebrewName}} / {{pokemon.englishName}}
        <p>
          <strong>Major Weaknesses:</strong>
          {{pokemon.majorWeaknesses}}
        </p>
        <p>
          <strong>Weaknesses:</strong>
          {{pokemon.weaknesses}}
        </p>
        <p>
          <strong>Resistancess:</strong>
          {{pokemon.resistancess}}
        </p>
      </div>
    </div>
  </div>
</template>

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