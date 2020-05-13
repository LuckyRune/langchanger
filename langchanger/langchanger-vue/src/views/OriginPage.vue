<template>
  <DefaultLayout>
    <h3 class="mb20">{{ origin.title }}</h3>
    <div class="book-info mb20">
        <Book width="220" height="290" class="mr20" :poster="origin.poster.image"/>
        <div>
            <h5>Информация</h5>
            <p><span class="book-prop">Формат: </span><a href="#">{{ origin.format_type.name }}</a></p>
            <p><span class="book-prop">Жанры: </span><a href="#" class="genre">{{ origin.genre[0].name }}</a>
            <p><span class="book-prop">Возрастной рейтинг: </span><a href="#">{{ origin.age_limit }}+</a></p>
            <p><span class="book-prop">Автор: </span>{{ origin.author }}</p>
        </div>
    </div>
    <div class="book-desc mb20">
        <h5>Описание</h5>
        <p>{{ origin.description }}</p>
    </div>
    <div class="mb20">
        <h5>Читать</h5>
        <SelectList id="select-language"/>
        <SelectList id="select-editor"/>
        <a href="/reading"><ButtonBlack value="Читать"/></a>
    </div>
    <div>
        <h5>Комментарии</h5>
        <div class="mb20">
            <p>Пока нет комментариев.</p>
        </div>
        <textarea id="comment-form" class="mb20"/>
        <ButtonBlack value="Написать"/>
    </div>
  </DefaultLayout>
</template>

<script>
import DefaultLayout from '@/layouts/DefaultLayout'
import Book from '@/components/Book'
import SelectList from '@/components/SelectList'
import ButtonBlack from '@/components/ButtonBlack'
import axios from 'axios'

export default {
    name: 'OriginPage',
    data() {
      return {
        id: this.$route.params.id,
        origin: []
      }
    },
    created () {
      axios('http://127.0.0.1:8000/project-api/library/origin/?origin=' + this.id, {
        method: 'GET'
      })
      .then((response) => {
        this.origin = response.data.data.origin
        console.log(response.data.data.origin)
        document.title = response.data.data.origin.title + " - Langchanger"
      })
    },

    components: {
        DefaultLayout,
        Book,
        SelectList,
        ButtonBlack
    }
}
</script>

<style scoped>
a {
  color: var(--text-link);
}

a:hover {
  text-decoration: underline;
}

.book-info {
  display: flex;
}

.book-info p {
  margin-bottom: 5px;
  font-size: 16px;
}

.book-prop {
  color: var(--text-desc);
}

.genre {
  padding: 3px 5px;
  border-radius: 4px;
  background-color: var(--secondary);
  color: white;
  margin-right: 5px;
}

.genre:hover {
  box-shadow: 0 0 2px black;
  text-decoration: none;
}

.genre:active {
  background-color: white;
  color: var(--secondary);
}

.book-desc p {
  width: 700px;
}

textarea {
  display: block;
  width: 650px;
  height: 170px;
  min-width: 650px;
  max-width: 650px;
}
</style>