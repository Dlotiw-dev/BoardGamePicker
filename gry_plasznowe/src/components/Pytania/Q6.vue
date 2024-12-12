<script setup>
import Questions from '@/components/Questions2.vue';
const opis1 = 'Stół duży obiadowy lub tzw. specjalnie do tego przygotowany'
const opis2= 'Zwykły stół np. kuchenny'
</script>

<template>
  <Questions pytanie="Czy masz odpowiednio duży stół do gry?" nazwa1="tak" nazwa2="nie" :opis1="opis1" :opis2="opis2"/>
</template>