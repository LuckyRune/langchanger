<template>
  <div>
    <div class="form-style">
      <h2 class="mb10">Войти</h2>
      <p class="mb10"><span>Впервые на сайте? </span><a href="/register">Зарегистрироваться</a></p>
      <div class="mb10">
        <h4 class="mb10">Почта</h4>
        <input type="text" id="login" v-model="email">
      </div>
      <div class="mb10">
        <h4 class="mb10">Пароль</h4>
        <input type="password" id="pass" v-model="password">
      </div>
      <span id="invalid-login">Введены неверные данные.</span>
      <p class="mb20"><span>Забыли пароль? </span><a href="#">Восстановить</a></p>
      <button class="btnBlack" @click="login">Войти</button>
    </div>
  </div>
</template>

<script>
import ButtonBlack from '@/components/ButtonBlack'
import { required } from 'vuelidate/lib/validators'
import {mapActions} from 'vuex'

export default {
    name: 'Login',
    data() {
      return {
        email: '',
        password: ''
      }
    },
    created () {
      document.title = "Войти - Langchanger";
    },
    methods: {
      ...mapActions([
            'GET_USER_SETTINGS'
      ]),
      login() {
        this.$store.dispatch('RETRIEVE_TOKEN', {
          email: this.email,
          password: this.password
    })
    .then(response => {
      this.GET_USER_SETTINGS()
      this.$router.push({ name: 'Home' })
    })
    .catch((error) => {
      document.getElementById('invalid-login').style.display = "block"
    })
      }
    },
    validations: {
      email: {
        required
      },
      password: {
        required
      }
    },
    components: {
        ButtonBlack
    }
}
</script>

<style scoped>
#invalid-login {
  display: none;
  margin-bottom: 10px;
  color: var(--large-accent);
}
</style>