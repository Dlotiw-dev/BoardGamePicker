<script setup>
import Questions from '@/components/Questions.vue';
const opis1 = 'Gry wymagające rozwiązywania zagadek i myślenia analitycznego, idealne dla miłośników łamigłówek i intelektualnych wyzwań.'
const opis2 = 'Gry skoncentrowane na planowaniu, zarządzaniu zasobami i podejmowaniu kluczowych decyzji dla osiągnięcia zwycięstwa.'
const opis3 = 'Gry oferujące narracyjną rozgrywkę, eksplorację i elementy fabularne, idealne dla osób szukających emocjonujących doświadczeń.'
</script>

<template>
  <Questions pytanie="Wybierz typ gry:" nazwa1="strategia" nazwa2="logiczne" nazwa3="przygodowe" :opis1="opis1" :opis2="opis2" :opis3="opis3"/>
</template>