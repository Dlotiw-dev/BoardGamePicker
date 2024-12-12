<script setup>
import Questions from '@/components/Questions.vue';
const opis1 = 'Gry, które nie wymagają żadnych wydatków (poza: tonerem, papierem i czasem), a jednocześnie oferują ciekawe doświadczenie. '
const opis2 = 'Gry w tej kategorii oferują głębszą mechanikę, a także różnorodność opcji do wyboru.'
const opis3 = 'Gry o wyższej jakości i cenie, często oferujące ekskluzywne elementy i bardziej rozbudowaną rozgrywkę.'

</script>

<template>
  <Questions pytanie="Koszt gry?" nazwa1="darmowe" nazwa2="<500" nazwa3="premium" :opis1="opis1" :opis2="opis2" :opis3="opis3"/>
</template>