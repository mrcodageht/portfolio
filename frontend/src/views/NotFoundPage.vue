<template>
    <v-container fluid>
       <v-sheet
    class="d-flex align-center justify-center flex-wrap text-center mx-auto px-4"
    elevation="2"
    height="250"
    max-width="800"
    width="100%"
    rounded
  >
    <div>
      <h2 class="text-headline-large font-weight-black text-orange my-0">Oupss!</h2>

      <div class="text-headline-small font-weight-medium mb-2">
        404 - Non trouve
      </div>

      <p class="text-body-medium mb-4">
        La ressource que vous demandiez n'est actuellement pas disponible.
      </p>

      <v-btn color="orange" density="default" variant="text" size="large" :prepend-icon="mdiPagePrevious" text="Retouner a la page d'accueil"
      @click="router.push({name: 'home'})"
      ></v-btn>
    </div>
  </v-sheet>
    </v-container>
</template>
<script setup lang="js">
import { mdiPagePrevious, mdiStepBackward } from '@mdi/js';
import { useRouter } from 'vue-router';
const router = useRouter()

</script>