import { defineStore } from "pinia";
import { watch } from "vue";

export const useNewsletterStore = defineStore("main", {
    state: () => ({
        newsletters: [2,1],
        newsletter: {},
        test: 'dsdsdssd',
    }),
    getters: {
        getFirstNewsletter: state => {
            return state.newsletters[0];
        },
        getLastNewsletter: state => {
            return state.newsletters[state.newsletters.length - 1];
        }
    },
    mutations: {
        setNewsletters(state, newsletters) {
            state.newsletters = newsletters;
        },
        setNewsletter(state, newsletter) {
            state.newsletter = newsletter;
        },
    },
    actions: {
        async fetchNewsletters({ commit }) {
            const response = await axios.get("/api/v1/newsletters");
            commit("setNewsletters", response.data);
        },
        async fetchNewsletter({ commit }, id) {
            const response = await axios.get(`/api/v1/newsletters/${id}`);
            commit("setNewsletter", response.data);
        },
    }
});

watch(
    () => useNewsletterStore,
    () => {
      localStorage.setItem(STATE_NAME, JSON.stringify(useNewsletterStore));
    },
    { deep: true }
  );
