import { defineStore } from "pinia";
import { watch } from "vue";


const STATE_NAME = "authState";

const defaultState = {
    user:{},
  }

const getDefaultState = () => {
if (localStorage.getItem(STATE_NAME) !== null) {
    return JSON.parse(localStorage.getItem(STATE_NAME));
}

return defaultState;
};

export const useAuthStore = defineStore(STATE_NAME, {
    state: getDefaultState,
    getters: {
    },
    mutations: {
    },
    actions: {
    }
});

watch(
    () => useAuthStore(),
    () => {
      localStorage.setItem(STATE_NAME, JSON.stringify(useAuthStore()));
    },
    { deep: true }
  );
