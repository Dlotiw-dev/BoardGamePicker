<script setup>
import { ref } from 'vue';
import axios from "axios";
import { RouterLink, useRoute } from 'vue-router';
import Q1Cards from '@/components/Pytania/Q1.vue';
import Q2Cards from '@/components/Pytania/Q2.vue';
import Q3Cards from '@/components/Pytania/Q3.vue';
import Q4Cards from '@/components/Pytania/Q4.vue';
import Q5Cards from '@/components/Pytania/Q5.vue';
import Q6Cards from '@/components/Pytania/Q6.vue';
import Q7Cards from '@/components/Pytania/Q7.vue';
import Q8Cards from '@/components/Pytania/Q8.vue';
import Q9Cards from '@/components/Pytania/Q9.vue';
import Q10Cards from '@/components/Pytania/Q10.vue';

const go = (routePath) => {
  const router = useRoute()
  router.push('/answer')
};
const questions = ref({
  q1: 1,
  q2: 0,
  q3: 0,
  q4: 0,
  q5: 0,
  q6: 0,
  q7: 0,
  q8: 0,
  q9: 0,
  q10: 0,
});
const inputData = ref({
        Liczba_graczy: '-1',
        koszt1: '-1',
        koszt2: '-1',
        Przesten: '-1',
        Samodzielny_druk: '-1',
        Duzy_stol: '-1',
        typ_gry: '-1',
        mechanika_gry_l: '-1',
        mechanika_gry_s: '-1',
        mechanika_gry_p: '-1'
      });
let prediction = ref('brak');

async function addPrediction() {
    const path = 'http://localhost:5000/predict';
    try {
      // Send POST request with the proper data
      await axios.post(path,inputData.value, {headers: {
          'Content-Type': 'application/json'  // Ensure content type is JSON
        }
      });
      
      console.log('Book added successfully');
      this.getAnswer();  // Fetch updated books list
    } catch (error) {
      console.error('Error adding book:', error);
      this.getAnswer();  // Fetch updated books list on error as well
    }
  }
async function getPrediction() {
    const path = 'http://localhost:5000/predict';

    try {
      const response = await axios.get(path);
      this.prediction = response.data.books;
    } catch (error) {
      console.error('Error fetching books:', error);
    }
  }
function getAnswer1(option){
  inputData.value.Liczba_graczy = option
  questions.value.q1 = 0
  if (option === 0){
    questions.value.q2 = 1
  }
  else{
    questions.value.q3 = 1
  }
  console.log(inputData.value)
}
function getAnswer2(option){
  inputData.value.koszt1 = option
  questions.value.q2 = 0
  if (option === 0){
    questions.value.q4 = 1
  }
  else if (option === 1){
    questions.value.q5 = 1
  }
  else if (option === 2){
    questions.value.q6 = 1
  }
  console.log(inputData.value)
}
function getAnswer3(option){
  inputData.value.koszt2 = option
  questions.value.q3 = 0
  if (inputData.value.Liczba_graczy === 2 && option === 1){
    questions.value.q6 = 1
  }
  else{
    questions.value.q7 = 1
  }
  console.log(inputData.value)
}
function getAnswer4(option){
  inputData.value.Przesten = option
  questions.value.q4 = 0
  questions.value.q7= 1
  console.log(inputData.value)
}
function getAnswer5(option){
  inputData.value.Samodzielny_druk = option
  questions.value.q5 = 0
  questions.value.q7 = 1
  console.log(inputData.value)
}
function getAnswer6(option){
  inputData.value.Duzy_stol = option
  questions.value.q6 = 0
  questions.value.q7 = 1
  console.log(inputData.value)
}
function getAnswer7(option){
  inputData.value.typ_gry = option
  questions.value.q7 = 0
  if (option  === 0){
    questions.value.q8 = 1
  }
  else if (option === 1){
    questions.value.q9 = 1
  }
  else if (option === 2){
    questions.value.q10 = 1
  }
  console.log(inputData.value)
}
function getAnswer8(option){
  inputData.value.mechanika_gry_s = option
  questions.value.q8 = 0
  go('/answer')
  console.log(inputData.value)
}
function getAnswer9(option){
  inputData.value.mechanika_gry_l = option
  questions.value.q9 = 0
  go('/answer')
  console.log(inputData.value)
}
function getAnswer10(option){
  inputData.value.mechanika_gry_p = option
  questions.value.q10 = 0
  go('/answer')
  console.log(inputData.value)
}
</script>

<template>
  <Q1Cards v-if="questions.q1" @pickedAnswer="getAnswer1"/>
  <Q2Cards v-if="questions.q2" @pickedAnswer="getAnswer2"/>
  <Q3Cards v-if="questions.q3" @pickedAnswer="getAnswer3"/>
  <Q4Cards v-if="questions.q4" @pickedAnswer="getAnswer4"/>
  <Q5Cards v-if="questions.q5" @pickedAnswer="getAnswer5"/>
  <Q6Cards v-if="questions.q6" @pickedAnswer="getAnswer6"/>
  <Q7Cards v-if="questions.q7" @pickedAnswer="getAnswer7"/>
  <Q8Cards v-if="questions.q8" @pickedAnswer="getAnswer8">
  <Q9Cards v-if="questions.q9" @pickedAnswer="getAnswer9"/>
  <Q10Cards v-if="questions.q10" @pickedAnswer="getAnswer10"/>


  
</template>