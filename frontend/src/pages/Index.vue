<template>
  <q-page class="flex flex-center">
    <div class="flex fit flex-center q-pa-xl q-gutter-xl">

    <Newsletter  v-for="newsletter in newsletters"
     :key="newsletter.id" :id="newsletter.id" 
     :title="newsletter.title" :news="newsletter.news" 
     :photo="newsletter.photo ? `http://127.0.0.1:8000/${newsletter.photo}` : newsletter.photo"
     :date="newsletter.date" />
    </div>
    <q-page-sticky v-if="authStore.user.access" position="bottom-right" :offset="[18, 18]">
            <q-btn  fab icon="add" color="primary" to='/add' />
    </q-page-sticky>
  </q-page>
</template>

<script setup>
import Newsletter from 'src/components/NewsletterComponent.vue'
import {useNewsletterStore} from 'src/store/newsletter'
import { useAuthStore } from 'src/store/auth';
import { storeToRefs} from 'pinia'
import { api } from 'src/boot/axios';

let newsletterState = storeToRefs(useNewsletterStore())
let authStore = useAuthStore()
let newsletters = newsletterState.newsletters


api.get('newsletters').then(response => {
  useNewsletterStore().newsletters = response.data.newsletters

})


</script>
