<template>
  <div>
    <h3 class="mb20">{{ origin.title }}</h3>
    <div class="book-info mb20">
        <!-- <Book width="220" height="290" class="mr20" :poster="origin.poster.image"/> -->
        <div class="svg-placeholder mr20">
          <img :src="origin.poster.image">
        </div>
        <div>
            <h5>Информация</h5>
            <p><span class="book-prop">Формат: </span><a href="#">{{ origin.format_type.name }}</a></p>
            <p><span class="book-prop">Жанры: </span><a href="#" class="genre">{{ origin.genre[0].name }}</a>
            <p><span class="book-prop">Возрастной рейтинг: </span><a href="#">{{ origin.age_limit }}+</a></p>
            <p><span class="book-prop">Автор: </span>{{ origin.author }}</p>
            <router-link :to="/reading/ + origin.id"><ButtonBlack value="Читать оригинал" class="mt20"/></router-link>
        </div>
    </div>
    <div class="book-desc mb40">
        <h5>Описание</h5>
        <p v-if="origin.description !=''">{{ origin.description }}</p>
        <p v-else>Без описания.</p>
    </div>
    <div class="mb40 read">
          <h5>Переводы</h5>
        <div class="read-selectors" v-if="translation_languages.length > 0">
          <div>
            <p>Язык</p>
            <select @change="selectLang" id="select-language" v-model="selected_language">
              <option v-for="option in translation_languages" :key="option.id" :value="option.id">{{ option.name }}</option>
            </select>
          </div>
          <div v-if="selected_language !== ''">
            <p>Автор</p>
            <select id="select-translation" v-model="selected_translation">
              <option v-for="author in authors" :key="author.id" :value="author.id">{{ author.author.username }}</option>
            </select>
          </div>
          <router-link v-if="selected_translation !== ''" :to="/translation/ + selected_translation"><button id="translation-read" class="btnBlack">Читать перевод</button></router-link>
        </div>
        <div v-else><p>Пока нет переводов. Создать версию перевода можно на странице чтения оригинала.</p></div>
    </div>
    <div>
        <h5>Комментарии</h5>
        <div class="mb20">
            <p v-if="!comments.length > 0">Пока нет комментариев.</p>
            <div class="comment" v-for="comment in comments" :key="comment.id">
              <div class="comment-usericon"><img src="/usericon.svg" alt="fsdf"></div>
              <div class="comment-data">
                <div class="comment-info">
                  <div class="comment-author">{{ comment.author.username }}</div>
                  <div class="comment-date">{{ comment.post_date.substr(0, 10) }}</div>
                </div>
                <div class="comment-text">{{ comment.post }}</div>
              </div>
            </div>
        </div>
        <textarea id="comment-form" class="mb20"/>
        <button class="btnBlack" @click="postComment">Написать</button>
    </div>
  </div>
</template>

<script>
import Book from '@/components/Book'
import SelectList from '@/components/SelectList'
import ButtonBlack from '@/components/ButtonBlack'
import axios from 'axios'
import { mapGetters } from 'vuex'
import { host } from '../vars.js'
export default {
    name: 'OriginPage',
    data() {
      return {
        id: this.$route.params.id,
        origin: [],
        translation_languages: [],
        selected_language: '',
        selected_translation: '',
        authors: [],
        comments: []
      }
    },
    methods: {
      selectLang() {
        var sel = document.getElementById('select-language').selectedIndex
        var selectedLang = document.getElementById('select-language').options[sel].value

        axios(host + '/project-api/library/origin/translation/?origin=' + this.origin.id + '&language=' + selectedLang)
        .then((response) => {
          this.authors = response.data.data
        })
      },
      getComments() {
        axios(host + '/project-api/library/comment-origin/?origin=' + this.id)
          .then((res) => {
            console.log(res.data.data)
            this.comments = res.data.data
        })
      },
      postComment() {
        var comment = document.getElementById('comment-form').value
        if (comment !== '') {
          this.$store.dispatch('COMMENT_POST', {
            post: comment,
            origin: this.id
          })
          document.getElementById('comment-form').value = ''
          setTimeout(this.getComments, 500)
        }
        else alert('Напишите что-нибудь!')
      }
    },
    created () {
      axios(host + '/project-api/library/origin/?origin=' + this.id)
      .then((response) => {
        this.origin = response.data.data.origin
        this.translation_languages = response.data.data.languages
        document.title = response.data.data.origin.title + " - Langchanger"
      })
      axios(host + '/project-api/library/comment-origin/?origin=' + this.id)
      .then((resp) => {
        console.log(resp.data.data)
        this.comments = resp.data.data
      })
      .catch((error) => {
        console.log(error.response)
      })
    },
    computed: {
      ...mapGetters([
          'USERID'
      ])
    },
    components: {
        Book,
        SelectList,
        ButtonBlack
    }
}
</script>

<style scoped>
.svg-placeholder, .svg-placeholder > img {
  width: 220px;
  height: 290px;
}

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
  width: 900px;
}

textarea {
  display: block;
  width: 650px;
  height: 170px;
  min-width: 650px;
  max-width: 650px;
}

.read {
  display: flex;
  flex-direction: column;
}

.read-btn {
  display: flex;
}

.read-selectors {
  display: flex;
}

.read-selectors a {
  display: flex;
  align-items: flex-end;
  text-decoration: none;
}

.btnBlack {
  min-width: 150px;
  height: 40px;
  padding: 0 10px;
  font-size: 18px;
  text-transform: uppercase;
  border: 0;
  border-radius: 4px;
  background-color: var(--secondary);
  color: white;
}

.btnBlack:hover {
  box-shadow: 0 0 3px black;
  cursor: pointer;
}

.btnBlack:active {
  background-color: white;
  color: var(--secondary);
  border: 1px solid var(--secondary);
  box-shadow: 0 0 3px black inset;
}

.btnBlack:disabled {
  background-color: gray;
}
.btnBlack:hover:disabled {
  box-shadow: none;
  cursor: default;
}

.comment {
  display: flex;
  margin: 20px 0
}

.comment-usericon {
  margin-right: 10px;
}

.comment-usericon img {
  width: 64px;
  height: 64px;
}

.comment-info {
  display: flex;
  margin-bottom: 10px;
}

.comment-author {
  margin-right: 10px;
  font-weight: 600;
}

.comment-date {
  color: var(--text-desc)
}

.comment-date, .comment-author {
  font-size: 18px;
}

.comment-text {
  font-size: 17px;
}
</style>