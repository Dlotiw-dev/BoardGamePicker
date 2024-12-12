<script setup>
import { RouterLink, useRoute } from 'vue-router';
import {ref} from 'vue'
const isActiveLink = (routePath) => {
  const route = useRoute();
  return route.path === routePath;
};
let navOpen = ref(true)

</script>


<template>
    <nav class="bg-green-700 border-b border-green-500">
      <div class="mx-auto max-w-8xl px-2 sm:px-6 lg:px-8">
        <div class="flex h-20 items-center justify-between">
          <!-- Logo -->
          <div class="flex items-center">
            <h1 class="text-white text-2xl font-semibold">Board Game Picker</h1>
          </div>
  
          <!-- Burger Button -->
          <div class="md:hidden">
            <button
              @click="navOpen = !navOpen"
              class="text-white hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white p-2 rounded-md"
              aria-label="Toggle navigation"
            >
              <svg
                class="h-6 w-6"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                aria-hidden="true"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M4 6h16M4 12h16m-7 6h7"
                />
              </svg>
            </button>
          </div>
  
          <!-- Navigation Links -->
          <div
            :class="[
              navOpen ? 'block' : 'hidden',
              'md:flex',
              'md:items-center',
              'space-y-2 md:space-y-0 md:space-x-4',
            ]"
            class="absolute top-20 left-0 w-full bg-green-700 md:relative md:top-0 md:w-auto md:bg-transparent"
          >
            <RouterLink
              to="/"
              :class="[
                isActiveLink('/')
                  ? 'bg-green-900'
                  : 'hover:bg-gray-900 hover:text-white',
                'block md:inline-block text-white px-3 py-2 rounded-md',
              ]"
            >
              Home
            </RouterLink>
            <RouterLink
              to="/answer"
              :class="[
                isActiveLink('/answer')
                  ? 'bg-green-900'
                  : 'hover:bg-gray-900 hover:text-white',
                'block md:inline-block text-white px-3 py-2 rounded-md',
              ]"
            >
              Wynik
            </RouterLink>
            <RouterLink
              to="/search"
              :class="[
                isActiveLink('/search')
                  ? 'bg-green-900'
                  : 'hover:bg-gray-900 hover:text-white',
                'block md:inline-block text-white px-3 py-2 rounded-md',
              ]"
            >
              Szukaj
            </RouterLink>
          </div>
        </div>
      </div>
    </nav>
</template>