<template>
  <router-link :to=" '/book/' + origins_data.id ">
    <div class="book">
        <Book :poster="origins_data.poster.image"/>
        <p class="book-title">{{ origins_data.title }}</p>
        <p>{{ origins_data.author }}</p>
    </div>
  </router-link>
</template>

<script>
import Book from '@/components/Book'

export default {
    name: 'OriginLink',

    components: {
      Book
    },

    props: {
      origins_data: {
            type: Object,
            default: () => {
                return []
            }
        }
    }
}
</script>

<style scoped>
.book {
  margin-bottom: 10px;
}

.book-title {
  max-width: 130px;
}

a {
    text-decoration: none;
    color: black;
    margin-right: 20px;
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