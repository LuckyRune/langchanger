<template>
  <div>
    <div style="position: relative">
        <h5>Настройки профиля</h5>
        <div class="form-style mb20">
            <div class="change-inputs mr20">
                <h4>Логин (Имя пользователя)</h4>
                <input type="text" id="user-login">
                <h4>Почта</h4>
                <input type="email" id="user-email">
            </div>
            <div class="usericon-upload mt5">
            <UserIcon size="128"/>
            <div class="upload-info ml20">
                <div>
                <p>Иконка пользователя</p>
                <p class="recommended-size">250x250</p>
                </div>
                <ButtonBlack value="Загрузить"/>
            </div>
            </div>
        </div>
        <ButtonBlack value="Изменить пароль" class="mb20"/>
        <h4 class="mb10">О себе</h4>
        <textarea id="user-about" placeholder="Опишите себя"/>
        <div class="edit-btns">
            <ButtonSemiWhite value="Отмена" class="mr5"/>
            <button class="btnBlack">Сохранить</button>
        </div>
    </div>
  </div>
</template>

<script>
import BackTo from '@/components/BackTo'
import ButtonBlack from '@/components/ButtonBlack'
import ButtonSemiWhite from '@/components/ButtonSemiWhite'
import UserIcon from '@/components/UserIcon'

export default {
    name: 'UserSettings',
    created () {
      document.title = "Настройки - Langchanger";
    },

    components: {
        BackTo,
        ButtonBlack,
        UserIcon,
        ButtonSemiWhite
    }
}
</script>

<style scoped>
h5 {
  font-size: 24px;
}

.change-inputs {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
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

.form-style {
  display: flex;
}

textarea {
  width: 430px;
  height: 90px;
  min-width: 430px;
  max-width: 430px;
  min-height: 90px;
}

.edit-btns {
  position: absolute;
  bottom: 0px;
  right: 0px;
}
</style>