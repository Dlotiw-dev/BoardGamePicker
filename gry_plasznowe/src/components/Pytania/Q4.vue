<script setup>
import Questions from '@/components/Questions2.vue';
const opis1 = 'tak np. stolik'
const opis2= 'nie: poczekalnia w szpitalu gra w ręce'
</script>

<template>
  <Questions pytanie="Czy masz miejsce do gry?" nazwa1="tak" nazwa2="nie" :opis1="opis1" :opis2="opis2"/>
</template>