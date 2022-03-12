<template>
<q-page class="flex flex-center collumn">
    
    <q-form @submit="onSubmit" class="q-gutter-md">
        <h5 class="flex flex-center">Register</h5>
        <div class="q-gutter-md" >
            <q-input
                v-model="username"
                label="Username"
                type="text"
                placeholder="Username"
                filled
                clearable
                :rules="[val => !!val || 'Field is required']"
            />

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
        <q-input
            v-model="passwordConfirmation"
            label="Password Confirmation"
            type="password"
            placeholder="Password Confirmation"
            filled
            clearable
            />

        </div>
        <div class="flex flex-center">
            <q-btn  label="Submit" type="submit" color="primary"/>
        </div>
            <h6 class="flex flex-center" >{{message}}</h6>

        
    </q-form>
</q-page>
</template>
<script setup>
import {useAuthStore} from 'src/store/auth'
import { api } from 'src/boot/axios';
import { useRouter } from 'vue-router'
import { ref } from 'vue';

const router = useRouter()


let authStore = useAuthStore()

let username = ref('')
let email = ref('')
let password = ref('')
let passwordConfirmation = ref('')
var message = ref('')

const onSubmit = async (e) => {
    e.preventDefault()
    let data = {
        email: email.value,
        password: password.value,
        username: username.value
    }
    if (password.value !== passwordConfirmation.value) {
        message.value = 'Passwords do not match'
        return
    }
    api.post('/auth/register', data).then(
        (res) => {
            authStore.user = res.data
            router.push('/login')
        }
    ).catch(err => {
        message.value = "username already exists";
    })
}


</script>