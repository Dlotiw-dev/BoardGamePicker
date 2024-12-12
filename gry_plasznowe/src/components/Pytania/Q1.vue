<script setup>
import { ref } from 'vue';
import Questions from '@/components/Questions.vue';
const opis1 = 'Gry przeznaczone do zabawy w pojedynkę, idealne dla osób, które chcą spędzić czas w samotności lub po prostu potrzebują wyzwań w pojedynkę. Gry solo mogą być wciągające i oferują dużą głębię, mimo braku interakcji z innymi graczami.'
const opis2 = 'Gry planszowe dedykowane dla dwóch graczy, które oferują równą rywalizację, w której obie strony mają równe szanse na wygraną. Często gry dwuosobowe skupiają się na bezpośredniej interakcji i strategii, dzięki czemu są idealne na wieczorne spotkania czy wypad do kawiarni.'
const opis3 = 'Gry przeznaczone dla większej liczby graczy, które są świetnym wyborem na spotkania towarzyskie, imprezy czy większe wydarzenia. Te gry często oferują elementy rywalizacji, kooperacji lub połączenie obu, co sprawia, że każdy gracz czuje się zaangażowany.'
</script>

<template>
  <Questions pytanie="W ilu graczy chcesz grać?" nazwa1="Solo" nazwa2="Duet" nazwa3="Trzech lub więcej graczy" :opis1="opis1" :opis2="opis2" :opis3="opis3"/>
</template>