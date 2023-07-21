import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TranslatorVue from '@/views/Translator.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // {
    //   path: '/',
    //   name: 'home',
    //   component: HomeView
    // },
    {
      path: '/',
      name: 'translator',
      component: TranslatorVue
    }, 
    {
      path: '/test',
      name: 'test',
      component: () => import('../views/Test.vue')
    }

    
  ]
})

export default router
