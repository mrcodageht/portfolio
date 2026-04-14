import { createApp } from 'vue'
import 'vuetify/styles'
import App from './App.vue'
import { vuetify } from './plugins/vuetify'
import { createTheme } from 'vuetify/lib/composables/theme.mjs'
import VueCookies from 'vue-cookies'
import { router } from './router'
import axios from 'axios'
import { createPinia } from 'pinia'
import { HttpError } from './classes/Error'
import { useUserStore } from './store/store'



export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
export const COOKIE_NAME_TOKEN = import.meta.env.VITE_COOKIE_NAME_TOKEN ?? 'access_token';
const ENVIRONMENT = import.meta.env.ENVIRONMENT ?? 'dev'

export const api = axios.create({
    baseURL: API_BASE_URL,
    timeout: 2500,
})

api.interceptors.response.use(
  response => response,

  error => {
    if (error.response) {
      const message =
        error.response.data?.detail || "Erreur serveur"

      return Promise.reject(
        new HttpError(message, error.response.status)
      )
    }

    if (error.request) {
      return Promise.reject(
        new HttpError("Serveur injoignable", 0)
      )
    }

    return Promise.reject(
      new HttpError("Erreur inattendue", 0)
    )
  }
)



const secure = ENVIRONMENT === 'prod' || ENVIRONMENT === 'production'
$cookies.config('1d', '/', '', secure, 'Strict')


const theme = createTheme()

const pinia = createPinia()


createApp(App)
    .use(vuetify)
    .use(router)
    .use(theme)
    .use(VueCookies)
    .use(pinia)
    .mount('#app')
