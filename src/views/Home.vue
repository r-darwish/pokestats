<template>
  <div class="home">
    <p>Insert a pokemon name in English or Hebrew:</p>
    <br />
    <input v-model="pokemonFilter" placeholder="Pokemon" />
    <div v-if="shouldSearch">
      <div v-for="pokemon in filteredData" :key="pokemon">
        <a :href="`https://www.pocketmonsters.co.il/?p=${pokemon.linkId}`">
          <img
            :src="`https://www.pocketmonsters.co.il/wp-content/uploads/2020/06/${pokemon.imageId}-1.png`"
          />
        </a>
        {{pokemon.hebrewName}} / {{pokemon.englishName}}
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Watch } from "vue-property-decorator";

interface Pokemon {
  hebrewName: string;
  englishName: string;
  linkId: number;
  imageId: number;
}

@Component({})
export default class Home extends Vue {
  private pokemonData: Pokemon[] = [
    {
      hebrewName: "נגביר",
      englishName: "Negeveer",
      imageId: 650,
      linkId: 87267
    }
  ];
  private pokemonFilter = "";

  get shouldSearch(): boolean {
    return this.pokemonFilter.length > 3;
  }
  get filteredData(): Pokemon[] {
    return this.pokemonData.filter(
      pokemon =>
        pokemon.hebrewName.includes(this.pokemonFilter) ||
        pokemon.englishName
          .toLowerCase()
          .includes(this.pokemonFilter.toLowerCase())
    );
  }
}
</script>