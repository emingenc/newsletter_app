<template>  
    <q-page class="flex flex-center">
        <q-card class="my-card q-pa-xl" flat bordered>
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
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                </div>
            </q-card-section>


            <q-slide-transition>
                <div v-show="expanded">
                <q-separator />
                <q-card-section class="text-subitle2">
                    {{ main }}
                </q-card-section>
                </div>
            </q-slide-transition>
            </q-card>
    </q-page>
</template>
<script setup>
</script>