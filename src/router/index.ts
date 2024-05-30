import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TranslatorVue from '../views/Evaluation.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
     {
       path: '/',
       name: 'home',
       component: HomeView
     },
    {
      path: '/translator',
      name: "translator",
      component: TranslatorVue
    }, 
    {
      path: '/evaluation',
      name: "evaluation",
      component: () => import('@/views/Test.vue')
    }

    
  ]
})

export default router
