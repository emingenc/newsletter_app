<template>
    <q-btn class="q-pa-xl"  size="xl" flat  icon="arrow_back" to="/" ></q-btn>
<q-card class="collumn q-pa-xl " flat bordered>
   <q-form @submit="onSubmit" class="q-gutter-md">

        <div>
           <q-file
                name="newsletter_photo"
                v-model="newsletter.photo"
                filled
                label="Select newsletter image"
            />
        </div>
     
        <div class="text-h5 q-mt-sm q-mb-xs"><q-input v-model="newsletter.title"  label="Title"  clearable /></div>
        <div class="text-caption text-grey">
          <q-input
            v-model="newsletter.news"
            filled
            type="textarea"
            label="Newsletter content"
            />
        
        </div>
        <div class="flex flex-center">
                <q-btn  label="Add Newsletter" type="submit" color="primary"/>
        </div>
    </q-form>

    </q-card>
</template>
<script setup>
import {useNewsletterStore} from 'src/store/newsletter'
import { useAuthStore } from 'src/store/auth';
import { storeToRefs} from 'pinia'
import { api } from 'src/boot/axios';
import { useRoute } from 'vue-router'
import { ref } from 'vue';

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
        photo: response.data.photo ,
        date: response.data.date
    }
})

const authStore = useAuthStore()

if (!authStore.user.access) {
    router.push('/login')
            };
let accessToken = ref(`Bearer ${authStore.user.access}`)

api.get('auth/me', {
    headers: {
        Authorization: accessToken.value,
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'

    }
}).then(res => {
    console.log(res.data)
}).catch(err => {
    let refreshToken = authStore.user.refresh
        api.get('auth/token/refresh', {
            headers: {
                Authorization: `Bearer ${refreshToken}`
            }
        }).then(res => {
                authStore.user.access = res.data.access
                accessToken.value = `Bearer ${res.data.access}`
            }).catch(err => {
                console.log(err)

            })
    })

let title = ref('')
let news = ref('')
let file = ref('')


const onSubmit = (e) => {
    e.preventDefault()
    let formData = new FormData()
    formData.append('title', title.value)
    formData.append('news', news.value)
    formData.append('photo', file.value, file.value.name, file.value.type)
    
    console.log(accessToken.value)
    api.post('newsletters',formData, {headers: {
        'Authorization': accessToken.value,
        'accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Access-Control-Allow-Origin': '*'

    }},  ).then(res => {
        router.push('/newsletter/' + res.data.id)

    }).catch(err => {
        console.log(err)
        
    })
}

</script>