<template>
  <div id="app">
    <h1>Decision Tree Game Predictor</h1>

    <form @submit.prevent="addPrediction">
      <div>
        <h3>Liczba Graczy</h3>
        <button type="button" @click="setFeature('Liczba_graczy', 0)">1</button>
        <button type="button" @click="setFeature('Liczba_graczy', 1)">2</button>
        <button type="button" @click="setFeature('Liczba_graczy', 2)">3+</button>
      </div>

      <div>
        <h3>Koszt1</h3>
        <button type="button" @click="setFeature('koszt1', 0)">Darmowe</button>
        <button type="button" @click="setFeature('koszt1', 1)">Less than 500</button>
        <button type="button" @click="setFeature('koszt1', 2)">Premium</button>
        <button type="button" @click="setFeature('koszt1', 3)">?</button>
      </div>

      <div>
        <h3>Koszt2</h3>
        <button type="button" @click="setFeature('koszt2', 0)"><500</button>
        <button type="button" @click="setFeature('koszt2', 1)">Premium</button>
        <button type="button" @click="setFeature('koszt2', 2)">?</button>
      </div>

      <div>
        <h3>Przesten</h3>
        <button type="button" @click="setFeature('Przesten', 0)">No</button>
        <button type="button" @click="setFeature('Przesten', 1)">Yes</button>
        <button type="button" @click="setFeature('Przesten', 2)">?</button>
      </div>

      <div>
        <h3>Samodzielny Druk</h3>
        <button type="button" @click="setFeature('Samodzielny_druk', 0)">Yes</button>
        <button type="button" @click="setFeature('Samodzielny_druk', 1)">No</button>
        <button type="button" @click="setFeature('Samodzielny_druk', 2)">?</button>
      </div>

      <div>
        <h3>Duzy Stół</h3>
        <button type="button" @click="setFeature('Duzy_stol', 0)">Yes</button>
        <button type="button" @click="setFeature('Duzy_stol', 1)">No</button>
        <button type="button" @click="setFeature('Duzy_stol', 2)">?</button>
      </div>

      <div>
        <h3>Typ Gry</h3>
        <button type="button" @click="setFeature('typ_gry', 0)">Strategy</button>
        <button type="button" @click="setFeature('typ_gry', 1)">Logic</button>
        <button type="button" @click="setFeature('typ_gry', 2)">Adventure</button>
      </div>

      <div>
        <h3>Mechanika Gry L</h3>
        <button type="button" @click="setFeature('mechanika_gry_l', 0)">Pattern Matching</button>
        <button type="button" @click="setFeature('mechanika_gry_l', 1)">Roll & Write</button>
        <button type="button" @click="setFeature('mechanika_gry_l', 2)">?</button>
      </div>

      <div>
        <h3>Mechanika Gry S</h3>
        <button type="button" @click="setFeature('mechanika_gry_s', 0)">Deck Building</button>
        <button type="button" @click="setFeature('mechanika_gry_s', 1)">Euro</button>
        <button type="button" @click="setFeature('mechanika_gry_s', 2)">?</button>
      </div>

      <div>
        <h3>Mechanika Gry P</h3>
        <button type="button" @click="setFeature('mechanika_gry_p', 0)">Dungeon Crawl</button>
        <button type="button" @click="setFeature('mechanika_gry_p', 1)">Boss Battler</button>
        <button type="button" @click="setFeature('mechanika_gry_p', 2)">?</button>
      </div>

      <button type="submit">Predict</button>
    </form>

    <div v-if="prediction !== null">
      <h2>Prediction: {{ prediction }}</h2>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      inputData: {
        Liczba_graczy: '0',
        koszt1: '0',
        koszt2: '2',
        Przesten: '0',
        Samodzielny_druk: '0',
        Duzy_stol: '0',
        typ_gry: '0',
        mechanika_gry_l: '0',
        mechanika_gry_s: '0',
        mechanika_gry_p: '0'
      },
      prediction: null,
      test: {
        tst: 'norbert'
      }
    };
  },
  
  methods: {
    setFeature(feature, value) {
      this.inputData[feature] = value;
      console.log(this.inputData)
    },
    async addPrediction() {
    const path = 'http://localhost:5000/predict';

    try {
      // Send POST request with the proper data
      await axios.post(path,this.inputData, {headers: {
          'Content-Type': 'application/json'  // Ensure content type is JSON
        }
      });
      
      console.log('Book added successfully');
      this.getAnswer();  // Fetch updated books list
    } catch (error) {
      console.error('Error adding book:', error);
      this.getAnswer();  // Fetch updated books list on error as well
    }
  },
  async getAnswer() {
    const path = 'http://localhost:5000/predict';

    try {
      const response = await axios.get(path);
      this.prediction = response.data.books;
    } catch (error) {
      console.error('Error fetching books:', error);
    }
  }
    
  }
};
</script>

<style>
/* Add your styles here */
</style>
