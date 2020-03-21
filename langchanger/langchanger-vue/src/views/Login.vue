<template>
  <DefaultLayout>
    <div class="form-style">
      <h2 class="mb10">Войти</h2>
      <p class="mb10"><span>Впервые на сайте?</span> <a href="/register">Зарегистрироваться</a></p>
      <h4 class="mb10">Имя пользователя</h4>
      <input type="text" id="login" class="mb10">
      <h4 class="mb10">Пароль</h4>
      <input type="password" id="pass" class="mb10">
      <p class="mb20"><span>Забыли пароль?</span> <a href="#">Восстановить</a></p>
      <ButtonBlack value="Войти"/>
    </div>
  </DefaultLayout>
</template>

<script>
import DefaultLayout from '@/layouts/DefaultLayout'
import ButtonBlack from '@/components/ButtonBlack'

export default {
    name: 'Login',
    created () {
      document.title = "Войти - Langchanger";
    },

    components: {
        DefaultLayout,
        ButtonBlack
    }
}
</script>

<style scoped>

</style>