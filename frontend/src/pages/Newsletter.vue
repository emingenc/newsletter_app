<template>  
    <q-page class="flex flex-center fit">
        
        <q-card class="my-card q-pa-xl fit" flat bordered>
            <p class="row ">{{newsletter.date}}</p>
            <q-img
             :src="newsletter.photo.startsWith('upload') ? `http://127.0.0.1:5000/${newsletter.photo}` : newsletter.photo"

            />

            <q-card-section>
                <div class="text-h5 q-mt-sm q-mb-xs">{{newsletter.title}}</div>
                <div class="text-caption text-grey">
                    {{newsletter.news}}
                </div>
            </q-card-section>


           
            </q-card>
    </q-page>
</template>
<script setup>
import {useNewsletterStore} from 'src/store/newsletter'
import { storeToRefs} from 'pinia'
import { api } from 'src/boot/axios';
import { useRoute } from 'vue-router'

let newsletterState = storeToRefs(useNewsletterStore())
let newsletter = newsletterState.newsletter

const route = useRoute()

let id = route.params.id
console.log(id)

api.get('newsletters/'+id).then(response => {
    useNewsletterStore().newsletter = {
        id: response.data.id,
        title: response.data.title,
        news: response.data.news,
        photo: response.data.photo || `https://picsum.photos/id/${Math.floor(Math.random() * 100) + 1}/400/300`,
        date: response.data.date
    }
})

</script>