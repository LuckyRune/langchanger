import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './vuex/store'
import Vuelidate from 'vuelidate'

Vue.use(Vuelidate)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
  store
}).$mount('#app')
