<template>
<q-card class="my-card fit" flat bordered>
      <q-img
        :src="image"
      />

      <q-card-section>
        <div class="text-h5 q-mt-sm q-mb-xs">{{title}}</div>
        <div class="text-caption text-grey">
          {{ content.slice(0, 350) }}
        <q-btn no-caps flat :align="right" label="< Read More > "/>
        </div>
      </q-card-section>
    </q-card>
</template>
<script setup>
import {  ref } from 'vue'
import {useNewsletterStore} from '../store/newsletter'
import { storeToRefs} from 'pinia'
const props = defineProps({
  title: {
    type: String,
    default: 'Title',
  },
  content: {
    type: String,
    default: ' Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
  },
  image: {
    type: String,
    default: 'https://cdn.quasar.dev/img/parallax2.jpg',
  },
})


let newsletterState = storeToRefs(useNewsletterStore())
let expanded = ref(false)


</script>