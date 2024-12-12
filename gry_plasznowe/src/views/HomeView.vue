<script setup>
import { ref } from 'vue';
import { RouterLink, useRouter } from 'vue-router';
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
const router = useRouter()
async function go (){
  
  await router.push({name: 'answer'})
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

import { inputData } from '@/store.js'


function getAnswer1(option){
  inputData.Liczba_graczy = option
  questions.value.q1 = 0
  if (option === 0){
    questions.value.q2 = 1
  }
  else{
    questions.value.q3 = 1
  }
  console.log(inputData)
}
function getAnswer2(option){
  inputData.koszt1 = option
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
  console.log(inputData)
}
function getAnswer3(option){
  inputData.koszt2 = option
  questions.value.q3 = 0
  if (inputData.Liczba_graczy === 2 && option === 1){
    questions.value.q6 = 1
  }
  else{
    questions.value.q7 = 1
  }
  console.log(inputData)
}
function getAnswer4(option){
  inputData.Przesten = option
  questions.value.q4 = 0
  questions.value.q7= 1
  console.log(inputData)
}
function getAnswer5(option){
  inputData.Samodzielny_druk = option
  questions.value.q5 = 0
  questions.value.q7 = 1
  console.log(inputData)
}
function getAnswer6(option){
  inputData.Duzy_stol = option
  questions.value.q6 = 0
  questions.value.q7 = 1
  console.log(inputData.value)
}
function getAnswer7(option){
  inputData.typ_gry = option
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
  console.log(inputData)
}
function getAnswer8(option){
  inputData.mechanika_gry_s = option
  questions.value.q8 = 0
  go('/answer')
  console.log(inputData)
}
function getAnswer9(option){
  inputData.mechanika_gry_l = option
  questions.value.q9 = 0
  go('/answer')
  console.log(inputData)
}
function getAnswer10(option){
  inputData.mechanika_gry_p = option
  questions.value.q10 = 0
  go('/answer')
  console.log(inputData)
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
  <Q8Cards v-if="questions.q8" @pickedAnswer="getAnswer8"/>
  <Q9Cards v-if="questions.q9" @pickedAnswer="getAnswer9"/>
  <Q10Cards v-if="questions.q10" @pickedAnswer="getAnswer10"/>


  
</template>