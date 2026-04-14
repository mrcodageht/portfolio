<template>
    <v-container class="px-8 my-8" fluid>
    
       

    <v-card max-width="800" class="mx-auto">
      <v-card-text >
        <div class="text-headline-large font-weight-black mb-4 mt-4 text-center">Connexion</div>
      </v-card-text>
      <v-alert :text="errorMessage" type="error" class="mx-8 my-8" v-show="hasError"></v-alert>
      <form class="px-8 pb-8" autocomplete="false" >

    <v-text-field
      v-model="state.email"
      :error-messages="v$.email.$errors.map(e => e.$message)"
      label="Nom d'utilisateur"
      required
      @blur="v$.email.$touch"
      @input="v$.email.$touch"
      class="mb-3"
      autocomplete="false"
    ></v-text-field>

    <v-text-field
    
      v-model="state.password"
      :error-messages="v$.password.$errors.map(e => e.$message)"
      label="Mot de passe"
      required
      @blur="v$.password.$touch"
      @input="v$.password.$touch"
      class="mb-3"
      type="password"
    ></v-text-field>


    <v-btn
      class="me-4"
      @click="submit"
      color="primary"
      rounded="md"
      block
      size="x-large"
      :prepend-icon="mdiLogin"
      :loading="isLoading"
      elevation="2"
    >
      Se connecter
    </v-btn>
  
  </form>
  </v-card>
  
      </v-container>
</template>
<script setup>
  import { reactive, ref } from 'vue'
  import { useVuelidate } from '@vuelidate/core'
  import { required, email } from '@vuelidate/validators'
import { mdiLogin } from '@mdi/js'
import { useUserStore } from '../store/store'
import { HttpError } from '../classes/Error'
import { useRouter } from 'vue-router'

const isLoading = ref(false)
const userStore = useUserStore();
const hasError = ref()
let errorMessage = ''
const router = useRouter()

  const initialState = {
    email: '',
    password: '',
  }

  const state = reactive({
    ...initialState,
  })


  const rules = {
    password: { required },
    email: { required, email },
  }

const v$ = useVuelidate(rules, state)

const submit = async () => {
  
  isLoading.value = true
  const isFormCorrect = await v$.value.$validate()
  if (!isFormCorrect)
    return
  console.log(`form valide process : ${state.email}`)
  const form = new FormData()
  form.append("username", state.email)
  form.append("password", state.password)
  try {
    await userStore.login(form)
    hasError.value = false
    errorMessage = ''
    router.push({name: 'home'})
  } catch (error) {
    if (error instanceof HttpError) {
      if (error.statusCode === 401) {
        hasError.value = true
        errorMessage = error.message
      }
    }
  } finally {
    isLoading.value = false
  }
}

  function clear () {
    v$.value.$reset()

    for (const [key, value] of Object.entries(initialState)) {
      state[key] = value
    }
  }
</script>