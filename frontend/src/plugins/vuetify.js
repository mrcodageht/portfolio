import { createVuetify } from 'vuetify'
import { aliases, mdi } from 'vuetify/iconsets/mdi-svg'
import { mdiAccount } from '@mdi/js'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify =  createVuetify({
    components,
  directives,
  icons: {
    defaultSet: 'mdi',
    aliases: {
      ...aliases,
      account: mdiAccount,
    },
    sets: {
      mdi,
    },
    },
    theme: {
      defaultTheme: 'dark'
  },
  defaults: {
    VBtn: {
      rounded: true,
    },
  }
})

export { vuetify }
  