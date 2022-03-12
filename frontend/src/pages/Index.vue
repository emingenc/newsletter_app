<template>
  <q-page class="flex flex-center">
    <div class="flex flex-center q-pa-xl q-gutter-xl">

    <Newsletter  v-for="newsletter in newsletters"
     :key="newsletter.id" :id="newsletter.id" 
     :title="newsletter.title" :news="newsletter.newa" 
     :photo="newsletter.photo" :date="newsletter.date" />
    </div>
  </q-page>
</template>

<script setup>
import Newsletter from 'src/components/NewsletterComponent.vue'
import {useNewsletterStore} from 'src/store/newsletter'
import { storeToRefs} from 'pinia'
import { api } from 'src/boot/axios';

let newsletterState = storeToRefs(useNewsletterStore())
let newsletters = newsletterState.newsletters


api.get('/api/v1/newsletters').then(response => {
  useNewsletterStore().newsletters = response.data.newsletters

})


</script>
