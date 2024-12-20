<script setup>
import axios from "axios";
import PulseLoader from 'vue-spinner/src/PulseLoader.vue';
import { onMounted, ref, reactive } from 'vue';
import { inputData } from '@/store.js'

const valueMappings = {
    Liczba_graczy: {
        0: "Solo",
        1: "Duet",
        2: "3+",
        "-1": "Not specified"
    },
    koszt1: {
        0: "darmowe",
        1: "<500",
        2: "premium",
        "-1": "Not specified"
    },
    koszt2: {
        0: "<500",
        1: "premium",
        "-1": "Not specified"
    },
    Przesten: {
        0: "Tak",
        1: "Nie",
        "-1": "Not specified"
    },
    Samodzielny_druk: {
        0: "Tak",
        1: "Ne",
        "-1": "Not specified"
    },
    Duzy_stol: {
        0: "Tak",
        1: "Nie",
        "-1": "Not specified"
    },
    typ_gry: {
        0: "Strategia",
        1: "Logiczne",
        2: "Przygodowe",
        "-1": "Not specified"
    },
    mechanika_gry_s: {
        0: "Deck building",
        1: "Euro",
        "-1": "Not specified"
    },
    mechanika_gry_l: {
        0: "pattern&matching",
        1: "roll&write",
        "-1": "Not specified"
    },
    mechanika_gry_p: {
        0: "dungeon crawl",
        1: "boss battler",
        "-1": "Not specified"
    }
};

let review = ref('')
let prediction = ref('brak');
let title = ref('Twoja gra planszowa to:')
let opis = ref('opis')
let czekaj = ref(false)
let primaryGame = ref('')
const state = reactive({
  isLoading: true,
  title: '',
  opis: ''
});

let games = ref('')

function generateReview(inputData) {
    const review = Object.entries(inputData)
        .map(([key, value]) => {
            const mapping = valueMappings[key];
            const mappedValue = mapping[value];

            // Skip if value is "Not specified"
            if (mappedValue === "Not specified") return null;
            

            // Format key: Replace underscores with spaces, remove suffixes like "_l", "_s", or "_p"
            let formattedKey = key
                .replace(/_/g, " ") // Replace underscores with spaces
                .replace(/\b(l|s|p)\b/g, "") // Remove single-character suffixes
                .trim(); // Remove trailing spaces
            console.log(`${formattedKey}: ${mappedValue}\n`)
            if (formattedKey === 'koszt1' || formattedKey === 'koszt2'){
              formattedKey= formattedKey.replace(/[0-9]/g, '');
            }
            return `${formattedKey}: ${mappedValue}\n`;
        })
        .filter(Boolean); // Remove null entries

    return review.join('').replace(/\n/g, '<br>'); // Combine all entries into a single string
}

async function addPrediction() {
  const path = 'http://localhost:5000/manual';
  try {
      // Send POST request with the proper data
      const response = await axios.post(path,inputData, {headers: {
          'Content-Type': 'application/json'  // Ensure content type is JSON
        }
      
      });
      console.log(response.data.message)
      //Tytuł gry
      state.title = response.data.message[0]
      state.opis = response.data.message[1]
      
      console.log('Prediction added successfully');
      console.log(state.title)
   
      
      
    } catch (error) {
      console.error('Error adding prediction:', error);
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
      
      //imaz.value = details.value.image
      czekaj.value = true
    }
    
  }
  catch (error){
    console.error("Error getting prediction", error)
  }
  finally{
    state.isLoading = false
    review.value = generateReview(inputData)
  }
});

</script>

<template>
  <section v-if="!state.isloading" class="bg-slate-300">
  <div class="container mx-auto p-4">
    <!-- Header -->
    <h3 class="text-xl font-semibold mb-4 text-center">{{ title }}</h3>
    <h1 class="text-4xl font-bold mb-2 text-center p-4">{{state.title}}</h1>

    <!-- Main Grid Layout -->
    <div class="grid grid-cols-1 gap-4 items-center">
      

      <!-- Right: Text -->
      <div class="flex flex-col justify-center text-center space-y-4">
      <div v-html="state.opis"></div>
      </div>
    </div>

    <!-- Bottom Section -->
    <h3 v-if="!state.isLoading" class="text-xl font-semibold text-center mt-6">Podsumowanie wyborów:</h3>
    <p v-html="review" class="text-center font-medium text-xl" ></p>
  </div>
  
  </section>
  <div v-else class="text-center text-gray-500 py-6">
      <PulseLoader />
  </div>
    <!-- <div class="container mx-auto p-4">
      <h3 class="text-xl font-semibold mb-4 text-center">{{ title }}</h3>
      <h1 class="text-4xl font-bold mb-2 text-center p-4">{{ prediction }}</h1>
    </div> -->
  </template>
