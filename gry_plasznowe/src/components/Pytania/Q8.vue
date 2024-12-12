<script setup>
import Questions from '@/components/Questions2.vue';
const opis1 = 'Mechanika polegająca na budowaniu własnej talii kart podczas gry, co pozwala graczowi rozwijać unikalne strategie.Stół duży obiadowy lub tzw. specjalnie do tego przygotowany'
const opis2= 'Gry skupiające się na zarządzaniu zasobami i punktacji, często z minimalną interakcją między graczami i bez elementów losowych.'
</script>

<template>
  <Questions pytanie="Wybierz mechanikę gry:" nazwa1="deck building" nazwa2="euro" :opis1="opis1" :opis2="opis2"/>
</template>