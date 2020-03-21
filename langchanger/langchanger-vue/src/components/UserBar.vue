<template>
  <a href="/user">
    <PlaceholderEqual size="40" class="mr10" value="usericon"/>
    <span class="mr5">Имя пользователя</span>
    <span>(<span>345)</span></span>
  </a>
</template>

<script>
import PlaceholderEqual from '@/components/PlaceholderEqual'

export default {
    name: 'UserBar',

    components: {
        PlaceholderEqual
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