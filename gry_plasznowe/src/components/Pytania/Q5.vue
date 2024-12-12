<script setup>
import Questions from '@/components/Questions2.vue';
const opis1 = 'gry tzw. PnP(print&play)'
const opis2= 'gry normalnie dostępne do zakupu w sklepie'
</script>

<template>
  <Questions pytanie="Czy chcesz drukować grę samodzielnie?" nazwa1="tak" nazwa2="nie" :opis1="opis1" :opis2="opis2"/>
</template>