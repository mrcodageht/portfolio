import { createApp } from 'vue'

// Vuetify
import 'vuetify/styles'

// Components
import App from './App.vue'
import { router } from './router'
import { vuetify } from './plugins/vuetify'
import { useTheme } from 'vuetify'
import { createTheme } from 'vuetify/lib/composables/theme.mjs'

const theme = createTheme()

createApp(App).use(vuetify).use(router).use(theme).mount('#app')
