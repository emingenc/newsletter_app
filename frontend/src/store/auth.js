import { defineStore } from "pinia";
import { watch } from "vue";

export const useAuthStore = defineStore("main", {
    state: () => ({
        user: {},
    }),
    getters: {
    },
    mutations: {
    },
    actions: {
    }
});

watch(
    () => useAuthStore,
    () => {
      localStorage.setItem(STATE_NAME, JSON.stringify(useAuthStore));
    },
    { deep: true }
  );
