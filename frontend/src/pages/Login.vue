<template>
    <q-page class="flex flex-center login">
        <q-form @submit="onSubmit" class="q-gutter-md">
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
                        :rules="[val => !!val || 'Field is required']"/>

            </div>
            <div class="flex flex-center">
                <q-btn  label="Submit" type="submit" color="primary"/>
            </div>
         </q-form>
        
    </q-page>
</template>
<script setup>
import { defineComponent, ref } from 'vue'
const submitResult = ref([])

function onSubmit(e) {
    e.preventDefault()
    submitResult.value = [
        'Email: ' + this.email,
        'Password: ' + this.password
    ]
}


</script>