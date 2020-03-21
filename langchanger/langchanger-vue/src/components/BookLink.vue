<template>
  <a :href="link">
    <div class="book">
        <Book/>
        <p>Заголовок</p>
        <p>Автор</p>
    </div>
  </a>
</template>

<script>
import Book from '@/components/Book'

export default {
    name: 'BookLink',

    components: {
      Book
    },

    props: {
      link: String,
    }
}
</script>

<style scoped>
a {
    text-decoration: none;
    color: black;
}

a:hover .book > div {
  box-shadow: 0 0 3px black;
}

a:active .book > div {
  box-shadow: 0 0 3px black inset;
}

p:nth-child(3) {
  font-size: 14px;
  color: var(--text-desc);
}
</style>