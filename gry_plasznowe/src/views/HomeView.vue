<script setup>
import { ref } from 'vue';
import axios from "axios";
import Q1Cards from '@/components/Pytania/Q1.vue';
// import Q2Cards from '@/components/Q2.vue';
// import Q3Cards from '@/components/Q3.vue';
// import Q4Cards from '@/components/Q4.vue';
// import Q5Cards from '@/components/Q5.vue';
// import Q6Cards from '@/components/Q6.vue';
// import Q7Cards from '@/components/Q7.vue';
// import Q8Cards from '@/components/Q8.vue';
// import Q9Cards from '@/components/Q9.vue';
// import Q10Cards from '@/components/Q10.vue';
const questions = ref({
  q1: -1,
  q2: -1,
  q3: -1,
  q4: -1,
  q5: -1,
  q6: -1,
  q7: -1,
  q8: -1,
  q9: -1,
  q10: -1,
});
const inputData = ref({
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
  console.log(inputData.value)
}
function getAnswer2(option){
  inputData.value.koszt1 = option
  console.log(inputData.value)
}
function getAnswer3(option){
  inputData.value.koszt2 = option
  console.log(inputData.value)
}
function getAnswer4(option){
  inputData.value.Przesten = option
  console.log(inputData.value)
}
function getAnswer5(option){
  inputData.value.Samodzielny_druk = option
  console.log(inputData.value)
}
function getAnswer6(option){
  inputData.value.Duzy_stol = option
  console.log(inputData.value)
}
function getAnswer7(option){
  inputData.value.typ_gry = option
  console.log(inputData.value)
}
function getAnswer8(option){
  inputData.value.mechanika_gry_s = option
  console.log(inputData.value)
}
function getAnswer9(option){
  inputData.value.mechanika_gry_l = option
  console.log(inputData.value)
}
function getAnswer10(option){
  inputData.value.mechanika_gry_p = option
  console.log(inputData.value)
}
</script>

<template>
  <Q1Cards v-if="questions.q1" @pickedAnswer="getAnswer1"/>
  <!-- <Q2Cards v-if="questions.q2" @pickedAnswer="getAnswer2"/>
  <Q3Cards v-if="questions.q3" @pickedAnswer="getAnswer3"/>
  <Q4Cards v-if="questions.q4" @pickedAnswer="getAnswer4"/>
  <Q5Cards v-if="questions.q5" @pickedAnswer="getAnswer5"/>
  <Q6Cards v-if="questions.q6" @pickedAnswer="getAnswer6"/>
  <Q7Cards v-if="questions.q7" @pickedAnswer="getAnswer7"/>
  <Q8Cards v-if="questions.q8" @pickedAnswer="getAnswer8"/>
  <Q9Cards v-if="questions.q9" @pickedAnswer="getAnswer9"/>
  <Q10Cards v-if="questions.q10" @pickedAnswer="getAnswer10"/> -->


  
</template>