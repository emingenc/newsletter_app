<template>
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
let accessToken = `Bearer ${authStore.user.access}`

api.get('auth/me', {
    headers: {
        Authorization: accessToken
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
            }).catch(err => {
                console.log(err)

            })
    })

let title = ref('')
let news = ref('')
let file = ref('')

const onSubmit = (e) => {
    e.preventDefault()
    let data = {
        title: title.value,
        news: news.value,
        photo: file.value
    }
    api.post('newsletters',data,{
        headers: {
            Authorization: accessToken
        }
    }).then(res => {
        console.log(res)
    }).catch(err => {
        console.log(err)
    })
}
/*
curl -X POST "http://127.0.0.1:5000/api/v1/newsletters" -H "accept: application/json" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0NzExNDYwMCwianRpIjoiZTgyODdiMTMtNGU4Zi00YWE2LWI4MTAtZThkNjk1MGViNzVjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjQ3MTE0NjAwLCJleHAiOjE2NDcxMTU1MDB9.QB9YIl8R_dRYDGiOsJ3_sT-5v9nP4pu-xctMI0E63zg" -H "Content-Type: multipart/form-data" -F "news=Ever wondered how to come up with new ideas for your work projects, assignments, or product sales? This article explains just that. Read on to find out. Here are a few pointers: 1) Sleep on it. You may question your creative mind and keep questioning until you fall asleep at night. Your dreams may do the trick and give you ideas on how to solve the problem of your work project or any assignment or sales of products. 2) Keep an open mind Look around you while you walk or drive. Be in the moment with an open mind. Ideas can come flowing. Before you know, you have in your lap several ideas to choose from. 3) Say a prayer Take the help of a Higher Power or God or the Universe. Ask for the ideas you need and say why. Make simple statements. Ask questions in the affirmative. Then forget the whole process and get detached. And the Eureka moment will surely hit you in a short while. 4) Meditate Keep in a no-thought state while you meditate. Be in the moment. Query the Universe about ideas that will help you and the problems you are not able to solve. Meditate for two to fifteen minutes. Keep still and complete your ritual. Later in the day, an avalanche of ideas regarding what you need is sure to come flowing to you. 5) Do a buddies' group discussion Remember two heads are always better than one. Together discuss and ask questions. Soon enough, you will be bombarded with fresh ideas regarding your problem. 6) Discuss with a mentor Mentors are always knowledgeable. So, if you have one whom you can call up, do so, discuss, and brainstorm. Surely, you will be flooded with ideas in no time. 7) Converse with your family If it is some nagging problem that you are unable to come to a solution, discuss with your significant other first, and then call the whole family to the table, talk, and discuss, and something worthy is sure to follow. Yes, there will be a bunch of ideas. Kids' brains also have a way of working out problems. So, I say yes, you will get ideas popping up. Summing up, these are a few pointers you could use to generate ideas and solve your problem regarding work projects or products sales. Start working with one or two that I mention here and that appeal to you and sound convenient, and yes, you will have lots of ideas on your plate. Rosina S Khan has authored this article. For a wealth of free resources based on stunning fiction stories and academic guides, amazing self-help eBooks, articles and blogs, all authored by her, and much more, visit: https://rosinaskhan.weebly.com. You will be glad that you did. Alternatively, for a different layout of free resources, visit: http://www.facebook.com/RosinaSKhan.hub. You won't be disappointed and remember to like her Facebook page. Article Source: https://EzineArticles.com/expert/Rosina_S_Khan/2054435 Article Source: http://EzineArticles.com/10553192" -F "photo=@28639.jpg;type=image/jpeg" -F "title=How Can You Come Up With New Ideas?"
*/

</script>