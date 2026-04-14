<template>
  <v-container class="px-8" fluid>
    <div>
      <v-row class="align-center justify-center" density="comfortable">
        <v-col>
          <v-card class="mx-auto" :prepend-icon="mdiMerge" subtitle="" height="130">
            <template v-slot:title>
              <span class="font-weight-black">6</span>
            </template>

            <v-card-text class="">
              <h4>Projets</h4>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col>
          <v-card class="mx-auto" :prepend-icon="mdiXml" subtitle="" height="130">
            <template v-slot:title>
              <span class="font-weight-black">6</span>
            </template>

            <v-card-text class="">
              <h4>Technologies</h4>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col>
          <v-card class="mx-auto" :prepend-icon="mdiAccountMultiple" subtitle="" height="130">
            <template v-slot:title>
              <span class="font-weight-black">6</span>
            </template>

            <v-card-text class="">
              <h4>Collaborateurs</h4>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col>
          <v-card class="mx-auto" :prepend-icon="mdiMultimedia" subtitle="" height="130">
            <template v-slot:title>
              <span class="font-weight-black">6</span>
            </template>

            <v-card-text class="">
              <h4>Medias</h4>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </div>
    <section class="mt-2">
      <div>
        <h2>Projets</h2>
        <v-divider />
        <v-table striped="even">
          <thead>
            <tr>
              <th class="text-left">
                Titre
              </th>
              <th class="text-center">
                Status
              </th>
              <th class="text-center">
                Date de debut
              </th>
              <th class="text-end">
                Actions
              </th>

            </tr>
          </thead>
          <tbody>
            <tr v-for="item in desserts" :key="item.name">
              <td>{{ item.title }}</td>
              <td class="text-center">
                <v-chip class="font-weight-bold" :text="getValueStatus(item.status)" :color="getColorChip(item.status)">

                </v-chip>
              </td>
              <td class="text-center">{{ dateFormatted(item.start_at) }}</td>
              <td class="text-end">
                <v-btn :prepend-icon="mdiEye" class="me-3 font-weight-semibold" rounded="sm">Voir</v-btn>
                <!-- <v-btn :prepend-icon="mdiDelete" rounded="sm" class="font-weight-semibold" color="red">Supprimer</v-btn> -->
              </td>
            </tr>
          </tbody>
        </v-table>

      </div>

    </section>

  </v-container>

</template>
<script setup lang="js">
import { mdiAccountMultiple, mdiDelete, mdiEye, mdiMerge, mdiMultimedia, mdiPencilBox, mdiXml } from '@mdi/js';

import { ref } from 'vue'

const getColorChip = (status) => {
  switch (status) {
    case 'in_progress':
      return 'green'
    case 'planning':
      return 'yellow'
    case 'finished':
      return 'default'
    default:
      return ''
  }
}


const getValueStatus = (status) => {
  switch (status) {
    case 'in_progress':
      return 'en cours'
    case 'planning':
      return 'planifier'
    case 'finished':
      return 'terminer'
    default:
      return '-'
  }
}
const dateFormatted = (date) => new Date(date).toLocaleDateString()
const desserts = ref([

  {
    "title": "Data ETL",
    "slug": "data-etl",
    "description": "Pipeline ETL pour rapports métier.",
    "start_at": "2026-03-12T02:26:34",
    "end_at": null,
    "status": "in_progress",
    "visibility": "private",
    "live_url": null,
    "repo_url": "https://github.com/davidm/data-etl",
    "pid": "447ntR"
  },
  {
    "title": "Portfolio Website",
    "slug": "portfolio-website",
    "description": "Site perso affichant projets et blog.",
    "start_at": "2026-03-12T02:26:34",
    "end_at": null,
    "status": "in_progress",
    "visibility": "published",
    "live_url": "https://portfolio.example.com",
    "repo_url": "https://github.com/alicem/portfolio",
    "pid": "44jDHB"
  },
  {
    "title": "Recettes API",
    "slug": "recettes-api",
    "description": "API pour gérer des recettes de cuisine.",
    "start_at": "2026-03-12T02:26:34",
    "end_at": null,
    "status": "finished",
    "visibility": "published",
    "live_url": "https://recettes.example.com",
    "repo_url": "https://github.com/bobd/recettes-api",
    "pid": "44sI2R"
  },
  {
    "title": "Realtime Chat",
    "slug": "realtime-chat",
    "description": "Application de chat en temps réel (mobile + web).",
    "start_at": "2026-03-12T02:26:34",
    "end_at": null,
    "status": "planning",
    "visibility": "private",
    "live_url": null,
    "repo_url": "https://github.com/carolinep/realtime-chat",
    "pid": "44yvtB"
  },
  {
    "title": "Mobile Shop",
    "slug": "mobile-shop",
    "description": "Application e-commerce sur mobile.",
    "start_at": "2026-03-12T02:26:34",
    "end_at": null,
    "status": "in_progress",
    "visibility": "published",
    "live_url": "https://shop.example.com",
    "repo_url": "https://github.com/emmal/mobile-shop",
    "pid": "45CJ2B"
  },
  {
    "title": "Dev Tools",
    "slug": "dev-tools",
    "description": "Outillage CLI et automatisation.",
    "start_at": "2026-03-12T02:26:34",
    "end_at": null,
    "status": "finished",
    "visibility": "published",
    "live_url": null,
    "repo_url": "https://github.com/fabrice/dev-tools",
    "pid": "45Iumh"
  }

])



</script>