<template>
<q-card class="my-card fit" flat bordered>
      <q-img
        :src="photo"
      />
      <q-card-section>
        <div class="text-h5 q-mt-sm q-mb-xs">{{title}}</div>
        <div class="text-caption text-grey">
          {{ news.slice(0, 350) }}
        <q-btn no-caps flat :align="'right'" label="< Detail View > " :to="`/newsletter/${id}`" />
        
        </div>
        {{date}}
      </q-card-section>
    </q-card>
</template>
<script setup>
const props = defineProps({
  id: {
    default: '',
  },
  title: {
    type: String,
    default: 'Title',
  },
  news: {
    type: String,
    default: ' Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
  },
  photo: {
    type: String,
    default: 'https://cdn.quasar.dev/img/parallax2.jpg',
  },
  date: {
    type: String,
    default: "2020-01-01",
  },
})

</script>