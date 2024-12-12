<script setup>
import axios from "axios";
import PulseLoader from 'vue-spinner/src/PulseLoader.vue';
import { onMounted, ref, reactive } from 'vue';
import { inputData } from '@/store.js'
let prediction = ref('brak');
let title = ref('Twoja gra planszowa to:')
let czekaj = ref(false)
let primaryGame = ref('')
const state = reactive({
  isLoading: true,
  details: {}
});

let games = ref('')
async function addPrediction() {
  const path = 'http://localhost:5000/predict';
  try {
      // Send POST request with the proper data
      const response = await axios.post(path,inputData, {headers: {
          'Content-Type': 'application/json'  // Ensure content type is JSON
        }
      
      });
      //Tytuł gry
      prediction.value = response.data.message
      
      console.log('Prediction added successfully');
      console.log(prediction.value)
      //Id Gry
      games.value = await searchBgg(prediction.value)
      if (games.value[0] === '162613'){
        primaryGame.value = games.value[1]
      }
      else if (games.value[0] == '373168'){
          primaryGame.value = games.value[1]
      }
      else if (games.value[0] == '143740'){
          primaryGame.value = games.value[7]
      }
      else{
        primaryGame.value = games.value[0]
      }
   
      //Szczegóły opis + zdjęcie
      state.details = await getBgg(primaryGame.value)
      
    } catch (error) {
      console.error('Error adding prediction:', error);
    }
  
  }
async function searchBgg(gameTitle) {
  try {
    const response = await axios.get("http://localhost:5000/bgg/search", {
      params: { game: gameTitle },
    });
    console.log(response.data)
    return response.data; 
  } catch (error) {
    console.error(error);
  }
}

async function getBgg(gameID) {
  try {
    const response = await axios.get("http://localhost:5000/bgg/get", {
      params: { gameId: gameID },
    });
    return response.data; 
  } catch (error) {
    console.error(error);
  }
}

onMounted (async () => {
  try {
    if (inputData.Liczba_graczy === -1){
      prediction.value = "Przejdź do home aby rozpocząć"
      title.value = ""
    }
    else{
      await addPrediction()
      console.log(state.details.image)
      console.log(typeof(state.details.description))
      //imaz.value = details.value.image
      czekaj.value = true
    }
    
  }
  catch (error){
    console.error("Error getting prediction", error)
  }
  finally{
    state.isLoading = false
  }
});

</script>

<template>
  <div v-if="!state.isLoading" class="container mx-auto p-4">
    <!-- Header -->
    <h3 class="text-xl font-semibold mb-4 text-center">{{ title }}</h3>
    <h1 class="text-4xl font-bold mb-2 text-center p-4">{{ prediction }}</h1>

    <!-- Main Grid Layout -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
      
      <!-- Left: Image -->
      <div class="justify-center p-4 m-2">
        <img :src="state.details.image" alt="Image description" class="w-full lg:max-w-lg md:max-w-md xs:max-w-xs rounded-lg shadow-md" />
      </div>

      <!-- Right: Text -->
      <div class="flex flex-col justify-center text-lg space-y-4">
      <div v-html="state.details.description"></div>
      </div>
    </div>

    <!-- Bottom Section -->
    <h3 class="text-xl font-semibold text-center mt-6">Conclusion or Final Thought</h3>
  </div>
  <div v-else class="text-center text-gray-500 py-6">
    <PulseLoader />
  </div>
  <div v-else class="container mx-auto p-4">
    <h3 class="text-xl font-semibold mb-4 text-center">{{ title }}</h3>
    <h1 class="text-4xl font-bold mb-2 text-center p-4">{{ prediction }}</h1>
  </div>
</template>
  

  
 <style scoped>
  /* You can add styling here */
 </style>
  