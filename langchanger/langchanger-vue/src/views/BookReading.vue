<template>
  <div>
    <div class="mb10" align="right" v-if="!loggedIn">Чтобы создать перевод для текста сначала нужно <a href="/login">войти</a>.</div>
    <div v-if="loggedIn" id="translate-btn" align="right" class="mb10"><router-link :to="/translating/ + id"><ButtonBlack value="Переводить"/></router-link></div>
    <!-- <iframe id="frame" class="origin-read-frame" :src="this.source_link" frameborder="0"></iframe> -->
    <textarea id="origin-text" readonly></textarea>
  </div>
</template>

<script>
import ButtonBlack from '@/components/ButtonBlack'
import axios from 'axios'
import {mapGetters} from 'vuex'
import { cors, host } from '../vars.js'

export default {
    name: 'BookReading',
    data() {
      return {
        id: this.$route.params.id,
        origin: [],
        source_link: '',
      }
    },
    created () {
      axios(host + 'project-api/library/origin/read/?origin=' + this.id)
      .then((response) => {
          var file = response.data.data.source_link.file
          axios(cors + file)
            .then((res) => {
            document.getElementById('origin-text').value = res.data
          })
        })
      // axios('http://127.0.0.1:8080/origins/' + this.id + '.txt')
      // .then((response) => {
      //   document.getElementById('origin-text').value = response.data
      // })
    },
    computed: {
        ...mapGetters([
            'loggedIn',
            'userID'
        ])
    },
    mounted() {
      // if (this.loggedIn) document.getElementById('translate-btn').style.display = "block"
    },
    components: {
        ButtonBlack
    }
}
</script>

<style scoped>
textarea {
  width: 900px;
  min-width: 950px;
  max-width: 950px;
  height: 75vh;
  min-height: 90px;
  padding: 2px;
}

a {
  color: var(--text-link)
}

a:hover {
  text-decoration: underline;
}
</style>