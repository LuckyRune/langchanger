<template>
  <a href="#">
    <span class="mr5">Имя пользователя</span>
    <span>(<span>345)</span></span>
  </a>
</template>

<script>
import UserIcon from '@/components/UserIcon'

export default {
    name: 'UserIcon',

    components: {
        UserIcon
    }
}
</script>

<style scoped>
a {
  display: flex;
  align-items: center;
  color: var(--text-link);
}

a:hover > div {
  box-shadow: 0 0 2px black;
}

a:active > div {
  box-shadow: 0 0 2px black inset;
}
</style>