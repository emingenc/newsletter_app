<template>
    <q-page class="flex flex-center row">
        <q-form @submit="onSubmit" class="q-gutter-md">
            <h5 class="flex flex-center" >Login</h5>
            <div class="q-gutter-md" >
                    <q-input
                        v-model="email"
                        label="Email"
                        type="email"
                        placeholder="Email"
                        filled
                        clearable
                        :rules="[val => !!val || 'Field is required']"
                    />
                    <q-input
                        v-model="password"
                        label="Password"
                        type="password"
                        placeholder="Password"
                        filled
                        clearable
                        />

            </div>
            <div class="flex flex-center">
                <q-btn  label="Submit" type="submit" color="primary"/>
            </div>
         </q-form>
        
    </q-page>
</template>
<script setup>
import { ref } from 'vue'
import {useAuthStore} from 'src/store/auth'
import { api } from 'src/boot/axios';
import { useRouter } from 'vue-router'

const router = useRouter()


const submitResult = ref({})
let authStore = useAuthStore()

let email = ref('')
let password = ref('')

let headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
};

function onSubmit(e) {
    
    e.preventDefault()
    submitResult.value = {
        email: email,
        password: password
    }
    api.post('auth/login', submitResult.value, headers)
    .then(response => {
     authStore.user = response.data.user

    }).then(() => {
        router.push('/')
    })
}


</script>