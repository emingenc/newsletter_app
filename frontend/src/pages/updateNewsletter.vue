<template>
    <q-btn class="q-pa-xl"  size="xl" flat  icon="arrow_back" to="/" ></q-btn>
<q-card class="collumn q-pa-xl " flat bordered>
   <q-form @submit="onSubmit" class="q-gutter-md">

        <div>
            <q-img
                :src="newsletter.photo ? `http://api:8000/${newsletter.photo}` : newsletter.photo"
            />
    
           <q-file
                name="newsletter_photo"
                v-model="file"
                filled
                label="Change newsletter image"
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
                <q-btn  label="Update Newsletter" type="submit" color="primary"/>
        </div>
    </q-form>

    </q-card>
</template>
<script setup>
import {useNewsletterStore} from 'src/store/newsletter'
import { useAuthStore } from 'src/store/auth';
import { api } from 'src/boot/axios';
import { useRoute , useRouter} from 'vue-router'
import { ref } from 'vue';

let newsletterState = useNewsletterStore()
let newsletter = newsletterState.newsletter

const route = useRoute()
const router = useRouter()

let id = route.params.id

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
let file = ref(null)

const onSubmit = (e) => {
    e.preventDefault()
    let formData = new FormData()
    formData.append('title', newsletter.title)
    formData.append('news', newsletter.news)
    if (file.value !== null) {
        formData.append('photo', file.value, file.value.name, file.value.type)
    }
    
    api.put(`newsletters/${id}`,formData, {headers: {
        'Authorization': accessToken.value,
        'accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Access-Control-Allow-Origin': '*'

    }},  ).then(res => {
        router.push('/newsletter/' +id)

    }).catch(err => {
        console.log(err)
        
    })
}

</script>