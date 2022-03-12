import { defineStore } from "pinia";
import { watch } from "vue";


const STATE_NAME = "newsletterState";


const defaultState = {
    newsletters: [{
        id: 1,
        title: "Newsletter 1",
        news: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        date: "2020-01-01",
        photo: `https://picsum.photos/id/${Math.floor(Math.random() * 1000) + 1}/400/300`
    },
    {
        id: 2,
        title: "Newsletter 2",
        news: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        date: "2020-01-02",
        photo: `https://picsum.photos/id/${Math.floor(Math.random() * 1000) + 1}/400/300`
    },
    {
        id: 3,
        title: "Newsletter 3",
        news: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        date: "2020-01-03",
        photo: `https://picsum.photos/id/${Math.floor(Math.random() * 1000) + 1}/400/300`
    }],
    newsletter: {
        id: 1,
        title: "Newsletter 1",
        news: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        date: "2020-01-01",
        photo: `https://picsum.photos/id/${Math.floor(Math.random() * 1000) + 1}/400/300`
    },
}

const getDefaultState = () => {
    if (localStorage.getItem(STATE_NAME) !== null) {
        return JSON.parse(localStorage.getItem(STATE_NAME));
    }
    
    return defaultState;
};


export const useNewsletterStore = defineStore(STATE_NAME, {
    state: getDefaultState,
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
    () => useNewsletterStore(),
    () => {
      localStorage.setItem(STATE_NAME, JSON.stringify(useNewsletterStore()));
    },
    { deep: true }
  );
