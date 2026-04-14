import LoginPage from './views/LoginPage.vue'
import NotFoundPage from './views/NotFoundPage.vue'
import HomePage from './views/HomePage.vue'
import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from './store/store'

const routes = [
  { path: '', component: HomePage, name: 'home' },
  { path: '/home', component: HomePage, name: 'home' },
  { path: '/', component: HomePage, name: 'home' },
  { path: '/login', component: LoginPage, name: 'login' },
  { path: '/:pathMatch(.*)*', component: NotFoundPage, name: 'notfound' },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {

  const userStore = useUserStore()
  console.log(`is auth : `,userStore.isAuthentificated)
  console.log(`to : `,to.name)
  if (to.name !== 'login' && !userStore.isAuthentificated) {
    next({name: 'login'})
    // Redirect to login if not authenticated
  } else {
    next(); // Proceed as normal
  }
});
