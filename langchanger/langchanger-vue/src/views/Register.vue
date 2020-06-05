<template>
  <div>
    <div class="form-style">
        <h2 class="mb10">Регистрация</h2>
        <p class="mb10">Уже есть на сайте? <a href="/login">Войти</a></p>
      <div class="inline-form">
        <div class="mr20" :class="{ 'form-group--error': $v.email.$error }">
          <h4 class="mb10">Почта</h4>
          <input type="email" v-model.trim="$v.email.$model" :class="{ 'is-invalid':$v.email.$error, 'is-valid':!$v.email.$invalid }" placeholder="Используется для подтверждения аккаунта">
          <div class="invalid-feedback">
            <span v-if="!$v.email.required">Обязательное поле.</span>
            <span v-if="!$v.email.email">Введите корректный адрес электронной почты.</span>
          </div>
        </div>
        <div :class="{ 'form-group--error': $v.username.$error }">
          <h4 class="mb10">Имя пользователя</h4>
          <input type="text" v-model.trim="$v.username.$model" :class="{ 'is-invalid': $v.username.$error, 'is-valid': !$v.username.$invalid }" placeholder="Видимое всем имя аккаунта">
          <div class="invalid-feedback">
            <span v-if="!$v.username.required">Обязательное поле.</span>
            <span v-if="!$v.username.alphaNum">Имя пользователя должно состоять из латинских букв и/или цифр.</span>
            <span v-if="!$v.username.minLength">Имя пользователя должно состоять хотя бы из {{ $v.username.$params.minLength.min }} символов.</span>
            <span v-if="!$v.username.maxLength">Имя пользователя не должно превышать {{ $v.username.$params.maxLength.max }} символов.</span>
          </div>
        </div>
      </div>
      <div class="inline-form">
        <div class="mr20" :class="{ 'form-group--error': $v.password.$error }">
          <h4 class="mb10">Пароль</h4>
          <input type="password" v-model.trim="$v.password.$model" :class="{ 'is-invalid': $v.password.$error, 'is-valid': !$v.password.$invalid }" placeholder="Чувствителен к регистру">
          <div class="invalid-feedback">
            <span v-if="!$v.password.required">Обязательное поле.</span>
            <span v-if="!$v.password.alphaNum">Пароль должен состоять из букв и цифр.</span>
            <span v-if="!$v.password.minLength">Имя пользователя должно состоять хотя бы из {{ $v.password.$params.minLength.min }} символов.</span>
            <span v-if="!$v.password.notOnlyAlph">Пароль не может состоять лишь из букв.</span>
            <span v-if="!$v.password.notOnlyNum">Пароль не может состоять лишь из цифр.</span>
          </div>
        </div>
        <div>
          <h4 class="mb10" :class="{ 'form-group--error': $v.password2.$error }">Подтверждение пароля</h4>
          <input type="password" v-model.trim="$v.password2.$model" :class="{ 'is-invalid': $v.password2.$error, 'is-valid': !$v.password2.$invalid }" placeholder="Введите пароль ещё раз">
          <div class="invalid-feedback">
            <span v-if="!$v.password2.samePass">Пароли должны совпадать.</span>
          </div>
        </div>
      </div>
      <div class="inline-form">
        <div class="mr20 mb20">
          <h4 class="mb10">О себе</h4>
          <textarea v-model="description" placeholder="Опишите себя"/>
        </div>
        <div class="usericon-upload mt5">
          <div class="svg-placeholder">
            <img src="@/assets/svg/usericon.svg">
            <!-- <img v-else src="@/assets/svg/usericon.svg"> -->
          </div>
          <div class="upload-info ml20">
            <div>
              <p>Иконка пользователя</p>
              <p class="recommended-size">250x250</p>
            </div>
            <ButtonBlack value="Загрузить"/>
          </div>
        </div>
      </div>
      <p class="terms mb20">Нажатием Регистрация вы подтверждаете что прочитали и согласились с <a href="">Политикой использования</a></p>
      <button v-if="$v.email.$invalid || $v.username.$invalid || $v.password.$invalid || $v.password2.$invalid" disabled class="btnBlack">Регистрация</button>
      <button v-if="!$v.email.$invalid & !$v.username.$invalid & !$v.password.$invalid & !$v.password2.$invalid" class="btnBlack" @click="register">Регистрация</button>
    </div>
  </div>
</template>

<script>
import ButtonBlack from '@/components/ButtonBlack'
import UserIcon from '@/components/UserIcon'
import axios from 'axios'
import { required, minLength, maxLength, alphaNum, numeric, alpha, not, email, sameAs } from 'vuelidate/lib/validators'

export default {
    name: 'Register',

    data() {
      return {
        email: '',
        username: '',
        password: '',
        password2: '',
        description: ''
      }
    },

    methods: {
      register() {

        const payload = new FormData()
        payload.append("username", this.username)
        payload.append("email", this.email)
        payload.append("password", this.password)
        payload.append("password2", this.password2)
        if (this.description !== '' || null) payload.append("description", this.description)

        axios.post('http://127.0.0.1:8000/project-api/user/register/', payload)
            .then((response) => {
            console.log(response)
            this.$router.push('/login')
            })
            .catch((error) => {
            console.log(error)
            });
      } 
    },

    created () {
      document.title = "Регистрация - Langchanger"

      axios('https://thingproxy.freeboard.io/fetch/' + 'https://api.telegram.org/file/bot1230832566:AAGmZMA28NdvhHrnnCATbAnkitTUZFygCXY/documents/file_111.txt')
      .then((response) => {
        console.log(response)
      })
    },

    validations: {
      email: {
        required,
        email
      },
      username: {
        required,
        alphaNum,
        minLength: minLength(2),
        maxLength: maxLength(12)
      },
      password: {
        required,
        minLength: minLength(8),
        alphaNum,
        notOnlyNum: not(numeric),
        notOnlyAlph: not(alpha)
      },
      password2: {
        samePass: sameAs('password')
      }
    },

    components: {
        ButtonBlack,
        UserIcon
    }
}
</script>

<style scoped>
.inline-form {
  display: flex;
  margin-bottom: 10px;
}

.usericon-upload {
  display: flex;
  height: 130px;
}

.upload-info {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.recommended-size {
  font-size: 14px;
  color: var(--text-desc);
}

.terms {
  width: 430px;
  font-size: 14px;
  color: var(--text-desc);
}

.svg-placeholder img {
  width: 128px;
  height: 128px;
}
</style>