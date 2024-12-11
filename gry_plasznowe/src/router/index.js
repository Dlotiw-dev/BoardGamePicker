import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Q1 from '@/components/Pytania/Q1.vue'
import Q2 from '@/components/Pytania/Q2.vue'
import Q3 from '@/components/Pytania/Q3.vue'
import Q4 from '@/components/Pytania/Q4.vue'
import Q5 from '@/components/Pytania/Q5.vue'
import Q6 from '@/components/Pytania/Q6.vue'
import Q7 from '@/components/Pytania/Q7.vue'
import Q8 from '@/components/Pytania/Q8.vue'
import Q9 from '@/components/Pytania/Q9.vue'
import Q10 from '@/components/Pytania/Q10.vue'
import Answer from '@/views/Answer.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/answer',
      name: 'answer',
      component: Answer,
    },
  ],
})

export default router
