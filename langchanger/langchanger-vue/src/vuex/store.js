import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
      main_origins: [],
      origins: []
    },
    actions: {
      GET_MAIN_ORIGINS({commit}) {
        return axios('http://127.0.0.1:8000/project-api/library/main/', {
          method: 'GET'
        })
        .then((response) => {
          commit('SET_MAIN_ORIGINS', response.data.data)
        })
      },

      GET_ORIGINS({commit}) {
        return axios('http://127.0.0.1:8000/project-api/library/origin/all/?page_size=15', {
            method: 'GET'
        })
        .then((response) => {
          commit('SET_ORIGINS', response.data.data)
        })
      }
    },
    mutations: {
      SET_MAIN_ORIGINS: (state, main_origins) => {
        state.main_origins = main_origins
      },
      SET_ORIGINS: (state, origins) => {
        state.origins = origins
      }
    },
    getters: {
      MAIN_ORIGINS(state) {
          return state.main_origins
      },
      ORIGINS(state) {
          return state.origins
      }
    }
})

export default store;