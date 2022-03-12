<template>
</template>
<script setup>
import {useAuthStore} from 'src/store/auth'
import { api } from 'src/boot/axios';
import { useRouter } from 'vue-router'

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

</script>