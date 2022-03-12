<template>
<q-card class="my-card" flat bordered>
      <q-img
        src="https://cdn.quasar.dev/img/parallax2.jpg"
      />

      <q-card-section>
        <div class="text-h5 q-mt-sm q-mb-xs">Title</div>
        <div class="text-caption text-grey">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        <q-btn no-caps flat :align="right" label="< Read More > "/>
        </div>
      </q-card-section>
    </q-card>
</template>
<script setup>
import { defineComponent, ref } from 'vue'
import {useNewsletterStore} from '../store/newsletter'
import { storeToRefs} from 'pinia'

let newsletterState = storeToRefs(useNewsletterStore())
let expanded = ref(false)


</script>