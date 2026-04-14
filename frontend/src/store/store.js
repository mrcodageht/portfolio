import storeGetters from "./store-getters";
import storeMutations from "./store-mutations";
import { defineStore } from "pinia";
import { api, COOKIE_NAME_TOKEN } from "../main";

const useUserStore = defineStore("user", {
  state: () => ({
    user: null,
    token: $cookies.get(COOKIE_NAME_TOKEN),
    authentificated: false
  }),
  getters: storeGetters,
  actions: {
    async login( payload) {
      if (this.getUser !== null || this.getToken !== null)
        return

      console.log(`Convocation de la methode login avec le payload`)
      console.table(payload)
      
      const response = await api.post('/users/login', payload)
      
      this.$state.token = response.data.access_token
      $cookies.set(COOKIE_NAME_TOKEN, this.$state.token)
      console.table($cookies.get(COOKIE_NAME_TOKEN))
      return response
    },
    async me({ commit }) {},
  },
});

export { useUserStore };
