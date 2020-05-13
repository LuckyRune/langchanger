<template>
  <DefaultLayout>
    <div class="form-style">
        <h2 class="mb10">Регистрация</h2>
        <p class="mb10">Уже есть на сайте? <a href="/login">Войти</a></p>
      <div class="inline-form">
        <div class="mr20">
          <h4 class="mb10">Почта</h4>
          <input type="email" id="email" placeholder="Используется для подтверждения аккаунта" class="mb10">
        </div>
        <div>
          <h4 class="mb10">Имя пользователя</h4>
          <input type="text" id="username" placeholder="Видимое всем имя аккаунта" class="mb10">
        </div>
      </div>
      <div class="inline-form">
        <div class="mr20">
          <h4 class="mb10">Пароль</h4>
          <input type="password" id="pass" placeholder="Чувствителен к регистру" class="mb10">
        </div>
        <div>
          <h4 class="mb10">Подтверждение пароля</h4>
          <input type="password" id="pass-repeat" placeholder="Введите пароль ещё раз" class="mb10">
        </div>
      </div>
      <div class="inline-form">
        <div class="mr20 mb20">
          <h4 class="mb10">О себе</h4>
          <textarea id="user-about" placeholder="Опишите себя"/>
        </div>
        <div class="usericon-upload mt5">
          <PlaceholderEqual size="128" value="usericon"/>
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
      <ButtonBlack value="Регистрация" @click="register()"/>
    </div>
  </DefaultLayout>
</template>

<script>
import DefaultLayout from '@/layouts/DefaultLayout'
import ButtonBlack from '@/components/ButtonBlack'
import PlaceholderEqual from '@/components/PlaceholderEqual'
import axios from 'axios'

export default {
    name: 'Register',
    methods: {
      
    },
    created () {
      document.title = "Регистрация - Langchanger";
    },

    components: {
        DefaultLayout,
        ButtonBlack,
        PlaceholderEqual
    }
}
</script>

<style scoped>
.inline-form {
  display: flex;
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
</style>