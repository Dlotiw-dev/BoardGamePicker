<script setup>
import { RouterLink, useRoute } from 'vue-router';

const isActiveLink = (routePath) => {
  const route = useRoute();
  return route.path === routePath;
};
</script>

<template>
  <nav class="bg-green-700 border-b border-green-500">
    <div class="mx-auto max-w-8xl px-2 sm:px-6 lg:px-8">
        <div class="flex h-20 items-center justify-between">
        <div class="flex flex-1 items-center justify-center md:items-stretch md:justify-start">
        
            <div class="flex justify-center md:justify-start space-x-4">
                <h1 class="text-white text-2xl text-left font-semibold">Board Game Picker</h1>
            </div>
        
            <div class="md:ml-auto">
                <div class="flex space-x-2">
                <RouterLink
                    to="/"
                    :class="[
                    isActiveLink('/')
                        ? 'bg-green-900'
                        : 'hover:bg-gray-900 hover:text-white',
                    'text-white',
                    'px-3',
                    'py-2',
                    'rounded-md',
                    ]"
                    >Home</RouterLink
                >
                <RouterLink
                    to="/jobs"
                    :class="[
                    isActiveLink('/jobs')
                        ? 'bg-green-900'
                        : 'hover:bg-gray-900 hover:text-white',
                    'text-white',
                    'px-3',
                    'py-2',
                    'rounded-md',
                    ]"
                    >Jobs</RouterLink
                >
                <RouterLink
                    to="/jobs/add"
                    :class="[
                    isActiveLink('/jobs/add')
                        ? 'bg-green-900'
                        : 'hover:bg-gray-900 hover:text-white',
                    'text-white',
                    'px-3',
                    'py-2',
                    'rounded-md',
                    ]"
                    >Add Job</RouterLink
                >
                </div>
            </div>
        </div>
      </div>
    </div>
  </nav>
</template>