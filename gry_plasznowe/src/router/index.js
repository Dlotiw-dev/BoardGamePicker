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
      path: '/q1',
      name: 'question1',
      component: Q1,
    },
    {
      path: '/q2',
      name: 'question2',
      component: Q2,
    },
    {
      path: '/q3',
      name: 'question3',
      component: Q3,
    },
    {
      path: '/q4',
      name: 'question4',
      component: Q4,
    },
    {
      path: '/q5',
      name: 'question5',
      component: Q5,
    },
    {
      path: '/q6',
      name: 'question6',
      component: Q6,
    },
    {
      path: '/q7',
      name: 'question7',
      component: Q7,
    },
    {
      path: '/q8',
      name: 'question8',
      component: Q8,
    },
    {
      path: '/q9',
      name: 'question9',
      component: Q9,
    },
    {
      path: '/q10',
      name: 'question10',
      component: Q10,
    },
    {
      path: '/answer',
      name: 'answer',
      component: Answer,
    },
  ],
})

export default router
