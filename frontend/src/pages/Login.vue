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
import { defineComponent, ref } from 'vue'
import {useAuthStore} from '../store/auth'
import { storeToRefs} from 'pinia'

const submitResult = ref({})
let authStore = useAuthStore()

let email = ref('')
let password = ref('')

function onSubmit(e) {
    
    e.preventDefault()
    submitResult.value = {
        email: email,
        password: password
    }
    authStore.user = {
        email: email,
        password: password
    }
}


</script>