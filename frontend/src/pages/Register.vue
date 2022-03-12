<template>
<q-page class="flex flex-center collumn">
    
    <q-from class="q-gutter-md" @submit="onSubmit">
        <h5 class="flex flex-center">Register</h5>
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
        
    </q-from>
</q-page>
</template>
<script setup>
</script>