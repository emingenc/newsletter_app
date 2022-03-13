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
/*
curl -X POST "http://127.0.0.1:5000/api/v1/newsletters" -H "accept: application/json" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0NzExNDYwMCwianRpIjoiZTgyODdiMTMtNGU4Zi00YWE2LWI4MTAtZThkNjk1MGViNzVjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjQ3MTE0NjAwLCJleHAiOjE2NDcxMTU1MDB9.QB9YIl8R_dRYDGiOsJ3_sT-5v9nP4pu-xctMI0E63zg" -H "Content-Type: multipart/form-data" -F "news=Ever wondered how to come up woduct saldreams may do the trick and give you ideas on how to solve the problem of your work project or any assignment or sales of products. 2) Keep an open mind Look around you while you walk or drive.  Before you know, you have in your lap several ideas to choose from. 3) Say a prayer Take the help of a Higher Power or God or the Universe. Ask for the ideas you need and say why. Make simple statements. Ask questions in the affirmative. Then forget the whole process and get detached. And the Eureka moment will surely hit you in a short while. 4) Meditate Keep in a no-thought state while you meditate. Be in the moment. Query the Universe about ideas that will help you and the problems you are not able to solve. Meditate for two to fifteen minutes. Keep still and complete your ritual. Later in the day, an avalanche of ideas regarding what you need is sure to come flowing to you.://EzineArticles.com/10553192" -F "photo=@28639.jpg;type=image/jpeg" -F "title=How Can You Come Up With New Ideas?"
*/
api.post('newsletters',{
    headers: {
        'Authorization': accessToken.value,
        'accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Access-Control-Allow-Origin': '*'

    }
}).then(res => {
    console.log(res)
}).catch(err => {
    console.log(err)
})

</script>