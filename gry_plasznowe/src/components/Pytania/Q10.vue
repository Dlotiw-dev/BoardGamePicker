<script setup>
import Questions from '@/components/Questions2.vue';
const opis1 = 'Gry, w których rozgrywka oparta jest na eksploracji podziemi, pokonywaniu potworów i zdobywaniu skarbów, często w klimacie fantasy.'
const opis2 = 'Gry, w których gracze wspólnie walczą przeciwko potężnemu przeciwnikowi, wymagające współpracy i strategicznego myślenia.'
</script>

<template>
  <Questions pytanie="Wybierz mechanikę gry:" nazwa1="dungeon crawl" nazwa2="boss battler" :opis1="opis1" :opis2="opis2"/>
</template>