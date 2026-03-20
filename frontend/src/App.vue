<template>
  <!-- <v-responsive min-height="100vh" height="100%"> -->
    <v-app>

        <v-app-bar title="Mrcfolio CMS" class="px-3">
  <template v-slot:prepend>
    <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
  </template>

  <template v-slot:append>
    <v-btn
          :prepend-icon="theme === 'light' ? mdiWeatherSunny : mdiWeatherSunnyOff"
          :text="theme"
          slim
          @click="onClick"
        ></v-btn>
  </template>
</v-app-bar>



      <v-navigation-drawer
        expand-on-hover
        :temporary="false"
        v-model="drawer"
        
      >
        <v-divider></v-divider>

        <v-list  nav>
          <v-list-item :prepend-icon="mdiViewDashboard" title="Tableau de bord" value="dashboard"></v-list-item>
          <v-list-item :prepend-icon="mdiMerge" title="Projets" value="projects"></v-list-item>
          <v-list-item :prepend-icon="mdiXml" title="Technologies" value="technologies"></v-list-item>
          <v-list-item :prepend-icon="mdiAccountMultiple" title="Collaborateurs" value="collaborators"></v-list-item>
          <v-list-item :prepend-icon="mdiFolderMultipleImage" title="Medias" value="medias"></v-list-item>
        </v-list>

        <template v-slot:append>
          <v-list>
            <v-list-item @click="console.log('logout')" :active="false" title="Logout" :prepend-icon="mdiLogout" value="logout"  >
              
          </v-list-item> 
          </v-list>
                  
        </template>
      </v-navigation-drawer>

      <v-main>
          <RouterView/>
      </v-main>
    </v-app>
  <!-- </v-responsive> -->
</template>
<script setup lang="js">
import { RouterView } from 'vue-router';

  import { onMounted, ref, watch } from 'vue'
import { mdiAccountMultiple, mdiFolderMultipleImage, mdiLogout, mdiMerge, mdiViewDashboard, mdiWeatherSunny, mdiWeatherSunnyOff, mdiXml } from '@mdi/js';
import { useDisplay } from 'vuetify';

  const theme = ref('light')

  function onClick () {
    theme.value = theme.value === 'light' ? 'dark' : 'light'
  }
   const drawer = ref(false)


const { width, mobile } = useDisplay()
onMounted(() => {
    console.log(width.value)
  })
</script>