<template>  
    <q-page class="flex flex-center fit">
        
        <q-card class="my-card q-pa-xl fit" flat bordered>
            <q-btn class=""  size="md" flat  icon="arrow_back" to="/" ></q-btn>
            <p class="row ">{{newsletter.date}}</p>
            <q-img
             :src="newsletter.photo ? `http://api:8000/${newsletter.photo}` : newsletter.photo"

            />

            <q-card-section>
                <div class="text-h5 q-mt-sm q-mb-xs">{{newsletter.title}}</div>
                <div class="text-caption text-grey">
                    {{newsletter.news}}
                </div>
            </q-card-section>


           
            </q-card>
            <q-page-sticky v-if="authStore.user.access" position="bottom-right" :offset="[18, 18]">
                <q-fab color="primary" icon="keyboard_arrow_up" direction="up">
                    <q-fab-action color="red-5" @click="deleteNewsletter()" icon="delete" />
                    <q-fab-action color="secondary" :to="id+'/update'" icon="edit" />
                </q-fab>
            </q-page-sticky>
    </q-page>
</template>
<script setup>
import {useNewsletterStore} from 'src/store/newsletter'
import { storeToRefs} from 'pinia'
import { api } from 'src/boot/axios';
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from 'src/store/auth';


let newsletterState = storeToRefs(useNewsletterStore())
let newsletter = newsletterState.newsletter
let authStore = useAuthStore()


const route = useRoute()
const router = useRouter()

let id = route.params.id

api.get('newsletters/'+id).then(response => {
    useNewsletterStore().newsletter = {
        id: response.data.id,
        title: response.data.title,
        news: response.data.news,
        photo: response.data.photo || `https://picsum.photos/id/${Math.floor(Math.random() * 100) + 1}/400/300`,
        date: response.data.date
    }
})

let  headers = {
        Authorization: `Bearer ${authStore.user.access}`,
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'

    }

let deleteNewsletter = () => {
    api.delete('newsletters/'+id , {headers: headers}).then(response => {
        useNewsletterStore().newsletters = useNewsletterStore().newsletters.filter(newsletter => newsletter.id != id)
        router.push('/')
    }).catch(error => {
        console.log(error)
    })
    
    }

</script>