<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-toolbar-title>
          Newsletter App
        </q-toolbar-title>
        <q-space/>
        <q-btn v-if="isLoggedIn()" label="Logout" flat color="white" @click="logout()" />
        <q-btn v-if="!isLoggedIn()" label="Login as admin" flat color="white" to="/login" />
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { useAuthStore } from 'src/store/auth';

const authStore = useAuthStore()
console.log({...authStore.user})

let isLoggedIn = () =>   {
  return authStore.user.access ? true : false
}

const logout = () => {
  authStore.user = {}
}



</script>
