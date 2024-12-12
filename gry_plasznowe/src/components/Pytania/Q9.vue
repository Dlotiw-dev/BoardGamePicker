<script setup>
import Questions from '@/components/Questions2.vue';
const opis1 = 'Gry, w których kluczowe jest tworzenie lub dopasowywanie wzorów na planszy, wymagające spostrzegawczości i planowania.'
const opis2 = 'Mechanika polegająca na rzucaniu kośćmi i zapisywaniu wyników, co pozwala na szybkie i proste rozgrywki.'
</script>

<template>
  <Questions pytanie="Wybierz mechanikę gry:" nazwa1="pattern matching" nazwa2="roll&write" :opis1="opis1" :opis2="opis2"/>
</template>