import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import { host } from '../vars.js'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
      main_origins: [],
      origins: [],
      users: [],
      client_username: '',
      userID: '',
      token: localStorage.getItem('access_token') || null
    },
    actions: {
      GET_MAIN_ORIGINS({commit}) {
        return axios(host + 'project-api/library/main/', {
          method: 'GET'
        })
        .then((response) => {
          commit('SET_MAIN_ORIGINS', response.data.data)
        })
      },

      GET_ORIGINS({commit}) {
        return axios(host + 'project-api/library/origin/all/?page_size=999999999999')
        .then((response) => {
          commit('SET_ORIGINS', response.data.data)
        })
      },

      GET_USERS({commit}) {
        return axios(host + 'project-api/user/all/?page_size=30', {
            method: 'GET'
        })
        .then((response) => {
          commit('SET_USERS', response.data.data)
        })
      },

      DESTROY_TOKEN(context) {
        axios.defaults.headers.common['Authorization'] = 'Token ' + context.state.token

        if(context.getters.loggedIn) {
          return new Promise((resolve, reject) => {

            axios.post(host + 'auth/token/logout/')
                .then((response) => {
                localStorage.removeItem('access_token')
                context.commit('DESTROY_TOKEN')
                resolve(response)
                })
                .catch((error) => {
                  localStorage.removeItem('access_token')
                  context.commit('DESTROY_TOKEN')
                  reject(error)
                })
              })
        }
      },

      RETRIEVE_TOKEN(context, credentials) {
        return new Promise((resolve, reject) => {

        let form = new FormData()
        form.append("email", credentials.email)
        form.append("password", credentials.password)

        axios.post(host + 'auth/token/login/', form)
            .then((response) => {
            const token = response.data.data.attributes.auth_token
            localStorage.setItem('access_token', token)
            context.commit('RETRIEVE_TOKEN', token)
            resolve(response)
            })
            .catch((error) => {
              reject(error)
            })
          })
      },

      GET_USER_SETTINGS(context) {
        axios.defaults.headers.common['Authorization'] = 'Token ' + context.state.token

        return new Promise((resolve, reject) => {

          axios(host + 'project-api/user/main-info/')
              .then((response) => {
              context.commit('SET_CLIENT_USERNAME', response.data.username)
              context.commit('SET_USERID', response.data.id)
              resolve(response)
              })
              .catch((error) => {
                reject(error)
              })
            })
      },

      TRANSLATION_ADD(context, translationData) {
        axios.defaults.headers.common['Authorization'] = 'Token ' + context.state.token

        let form = new FormData()
        form.append("origin", translationData.origin)
        form.append("language", translationData.language)
        form.append("file", translationData.file, "file.txt")

        axios.post(host + 'project-api/library/translation/add/', form)
              .then((response) => {
              console.log(response)
              })
      },
      
      ADD_VERSION(context, versionData) {
        axios.defaults.headers.common['Authorization'] = 'Token ' + context.state.token

        let form = new FormData()
        form.append("translation", versionData.translation)
        form.append("file", versionData.file, "file.txt")

        axios.put(host + 'project-api/library/translation/add-version/', form)
              .then((response) => {
              console.log(response)
              })
      },
      DELETE_TRANSLATION(context, delTranslationData) {
        console.log(delTranslationData.translation)
        console.log(typeof delTranslationData.translation)
        var form = new FormData()
        form.append("translation", delTranslationData.translation)

        axios.delete(host + 'project-api/library/translation/delete/', {
          headers: {
            'Authorization': 'Token ' + context.state.token
          }, data: form
        })
        .then((response) => {
          console.log(response)
        })
      },
      COMMENT_POST(context, commentData) {
        var form = new FormData()
        form.append("post", commentData.post)
        form.append("author", context.state.userID)
        form.append("origin", commentData.origin)

        axios.post(host + 'project-api/library/comment-origin/add/', form, {
          headers: {
            'Authorization': 'Token ' + context.state.token
          }
        })
        .then((response) => {
          console.log(response)
        })
      }
    },
    mutations: {
      SET_MAIN_ORIGINS: (state, main_origins) => {
        state.main_origins = main_origins
      },
      SET_ORIGINS: (state, origins) => {
        state.origins = origins
      },
      SET_USERS: (state, users) => {
        state.users = users
      },
      SET_CLIENT_USERNAME: (state, client_username) => {
        state.client_username = client_username
      },
      SET_USERID: (state, userID) => {
        state.userID = userID
      },
      RETRIEVE_TOKEN(state, token) {
        state.token = token
      },
      DESTROY_TOKEN(state) {
        state.token = null
      }
    },
    getters: {
      MAIN_ORIGINS(state) {
          return state.main_origins
      },
      ORIGINS(state) {
          return state.origins
      },
      USERS(state) {
        return state.users
      },
      CLIENT_USERNAME(state) {
        return state.client_username
      },
      USERID(state) {
        return state.userID
      },
      loggedIn(state) {
        return state.token !== null
      }
    }
})

export default store;