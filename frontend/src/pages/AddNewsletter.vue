<template>
    <q-btn class="q-pa-xl"  size="xl" flat  icon="arrow_back" to="/" ></q-btn>
<q-card class="collumn q-pa-xl " flat bordered>
   <q-form @submit="onSubmit" class="q-gutter-md">

        <div>
           <q-file
                name="newsletter_photo"
                v-model="file"
                filled
                label="Select newsletter image"
            />
        </div>
     
        <div class="text-h5 q-mt-sm q-mb-xs"><q-input v-model="title"  label="Title"  clearable /></div>
        <div class="text-caption text-grey">
          <q-input
            v-model="news"
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
import {useAuthStore} from 'src/store/auth'
import { api } from 'src/boot/axios';
import { useRouter } from 'vue-router'
import { ref } from 'vue';

const router = useRouter()
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