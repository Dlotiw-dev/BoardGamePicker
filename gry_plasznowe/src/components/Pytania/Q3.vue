<script setup>
import Questions2 from '@/components/Questions2.vue';
const opis1 = 'Gry w tej kategorii oferują głębszą mechanikę, a także różnorodność opcji do wyboru.'
const opis2= 'Gry o wyższej jakości i cenie, często oferujące ekskluzywne elementy i bardziej rozbudowaną rozgrywkę.'
</script>

<template>
  <Questions2 pytanie="Koszt gry?" nazwa1="<500" nazwa2="premium" :opis1="opis1" :opis2="opis2"/>
</template>