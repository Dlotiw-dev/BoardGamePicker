<script setup>
import { RouterLink } from 'vue-router';
import Card from '@/components/Card.vue';
import router from '@/router';
const emit = defineEmits(['pickedAnswer'])
function handleSelection(option, event, link) {
  // Emit the selected option back to the parent (Home.vue)
  emit('pickedAnswer', option);
  
}
defineProps({
  pytanie: {
    type: String,
    default: 'Witamy w programie',
  },
  nazwa1: {
    type: String,
    default: 'essegesgdsef',
  },
  nazwa2: {
    type: String,
    default: 'essegesgdsef',
  },
  opis1:{
    type: String,
    default: 'essegesgdsef',
  },
  opis2:{
    type: String,
    default: 'essegesgdsef',
  },
  link1:{
    type: String,
    default: '/',
  },
  link2:{
    type: String,
    default: '/',
  },
});
</script>

<template>
  <section class="py-4">
    <div class="container-xl lg:container m-auto">
      <h1 class="text-2xl font-bold py-2 mt-2 mb-4 text-center">{{ pytanie }}</h1>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 p-4 rounded-lg items-center justify-center">
        <Card class="max-w-sm p-4">
          <h2 class="text-2xl font-bold">{{nazwa1}}</h2>
          <p class="mt-2 mb-4">
            {{opis1}}
          </p>
          <button
            @click="handleSelection(0)"
            class="inline-block bg-green-500 text-white rounded-lg px-4 py-2 hover:bg-gray-700"
          >
            Wybierz
        </button>
        </Card>
        <Card class="max-w-sm p-4">
          <h2 class="text-2xl font-bold">{{nazwa2}}</h2>
          <p class="mt-2 mb-4">
            {{ opis2 }}
          </p>
          <button
            @click="handleSelection(1)"
            class="inline-block bg-green-500 text-white rounded-lg px-4 py-2 hover:bg-green-600"
          >
            Wybierz
        </button>
        </Card>
      </div>
    </div>
  </section>
</template>