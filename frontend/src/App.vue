<template>
  <!-- <v-responsive min-height="100vh" height="100%"> -->
  <v-app>

    <v-app-bar title="Mrcfolio CMS" class="px-3">
      <template v-slot:prepend >
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      </template>

      <template v-slot:append>
        <v-btn :prepend-icon="theme === 'light' ? mdiWeatherSunny : mdiWeatherSunnyOff" :text="theme" slim
          @click="onClick"></v-btn>
      </template>
    </v-app-bar>



      <v-navigation-drawer expand-on-hover :temporary="false" v-model="drawer" v-if="userStore.isAuthentificated">
        <v-divider></v-divider>

        <v-list nav>
          <v-list-item :prepend-icon="mdiViewDashboard" title="Tableau de bord" value="dashboard"></v-list-item>
          <v-list-item :prepend-icon="mdiMerge" title="Projets" value="projects"></v-list-item>
          <v-list-item :prepend-icon="mdiXml" title="Technologies" value="technologies"></v-list-item>
          <v-list-item :prepend-icon="mdiAccountMultiple" title="Collaborateurs" value="collaborators"></v-list-item>
          <v-list-item :prepend-icon="mdiFolderMultipleImage" title="Medias" value="medias"></v-list-item>
        </v-list>

        <template v-slot:append>
          <v-list>
            <v-list-item @click="processLogout" :active="false" title="Logout" :prepend-icon="mdiLogout"
              value="logout">

            </v-list-item>
          </v-list>

        </template>
      </v-navigation-drawer>

      <v-main v-if="userStore.isAuthentificated">
        <router-view v-slot="{ Component }">
          <transition>
            <component :is="Component" />
          </transition>
        </router-view>
      </v-main>

            <v-main v-else>
        <login-page/>
      </v-main>
  </v-app>
  <!-- </v-responsive> -->
</template>
<script setup lang="js">

import { onMounted, ref, watch } from 'vue'
import { mdiAccountMultiple, mdiFolderMultipleImage, mdiLogout, mdiMerge, mdiViewDashboard, mdiWeatherSunny, mdiWeatherSunnyOff, mdiXml } from '@mdi/js';
import { useDisplay } from 'vuetify';
import { useUserStore } from './store/store';
import LoginPage from './views/LoginPage.vue';
import { COOKIE_NAME_TOKEN } from './main';
import { useRouter } from 'vue-router';

const theme = ref('light')

function onClick() {
  theme.value = theme.value === 'light' ? 'dark' : 'light'
}
const drawer = ref(false)


const userStore = useUserStore()
const router = useRouter()

const processLogout = () => {
  $cookies.remove(COOKIE_NAME_TOKEN)
  userStore.$state.token = ''
  userStore.$state.authentificated = false
  router.push({name: 'login'})
}

</script>