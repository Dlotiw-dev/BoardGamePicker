<script setup>
import axios from "axios";
import { onMounted, ref } from 'vue';
import { inputData } from '@/store.js'
let prediction = ref('brak');
let title = ref('Twoja gra planszowa to:')
let czekaj = ref(false)
async function addPrediction() {
    const path = 'http://localhost:5000/predict';
    try {
      // Send POST request with the proper data
      const response = await axios.post(path,inputData, {headers: {
          'Content-Type': 'application/json'  // Ensure content type is JSON
        }
      
      });
      prediction = response.data.message
      console.log('Prediction added successfully');
      console.log(prediction)
      czekaj.value = true
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
      addPrediction()
    }
    
  }
  catch (error){
    console.error("Error getting prediction", error)
  }
});

</script>

<template>
  <div v-if="czekaj" class="container mx-auto p-4">
    <!-- Header -->
    <h3 class="text-xl font-semibold mb-4 text-center">{{ title }}</h3>
    <h1 class="text-4xl font-bold mb-2 text-center p-4">{{ prediction }}</h1>

    <!-- Main Grid Layout -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
      
      <!-- Left: Image -->
      <div class="flex justify-center">
        <img src="" alt="Image description" class="w-full max-w-xs rounded-lg shadow-md" />
      </div>

      <!-- Right: Text -->
      <div class="flex flex-col justify-center text-lg space-y-4">
        <p>
          This is where the answer text will be shown. The description will be aligned next to the image.
          You can add any relevant information here.
        </p>
      </div>
    </div>

    <!-- Bottom Section -->
    <h3 class="text-xl font-semibold text-center mt-6">Conclusion or Final Thought</h3>
  </div>
  <div v-else class="container mx-auto p-4">
    <h3 class="text-xl font-semibold mb-4 text-center">{{ title }}</h3>
    <h1 class="text-4xl font-bold mb-2 text-center p-4">{{ prediction }}</h1>
  </div>
</template>
  

  
 <style scoped>
  /* You can add styling here */
 </style>
  