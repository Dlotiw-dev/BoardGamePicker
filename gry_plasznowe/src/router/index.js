import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Answer from '@/views/Answer.vue'
import AnswerManual from '@/views/AnswerManual.vue'


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
    {
      path: '/manual',
      name: 'manual',
      component: AnswerManual,
    },
  ],
})

export default router
