<template>
  <div>
    <div class="create-translation mb10" id="create-translation">
      <span class="mr10">Выберите язык:</span>
      <select @change="enableBtn" id="select-translation-lang" v-model="selected_lang">
        <option v-for="lang in languages" :key="lang.id" :value="lang.id">{{ lang.attributes.name }}</option>
      </select>
      <button class="btnBlack" id="create-translation-btn" disabled @click="postTxt">Создать перевод</button>
    </div>
      <textarea id="origin-text"></textarea>
      <textarea id="text-area"></textarea>
  </div>
</template>

<script>
import ButtonBlack from '@/components/ButtonBlack'
import axios from 'axios'
import {mapGetters} from 'vuex'
import { cors, host } from '../vars.js' 

export default {
    name: 'BookTranslating',
    data() {
      return {
        id: this.$route.params.id,
        source_link: '',
        file: {},
        languages: [],
        selected_lang: ''
      }
    },
    computed: {
        ...mapGetters([
            'loggedIn'
        ])
    },
    created () {
      axios(host + '/project-api/library/origin/read/?origin=' + this.id)
      .then((response) => {
        var file = response.data.data.source_link.file
        axios(cors + file)
          .then((res) => {
          document.getElementById('origin-text').value = res.data
        })
      })
      //axios('http://127.0.0.1:8080/origins/' + this.id + '.txt')
      //.then((response) => {
      //  document.getElementById('origin-text').value = response.data
      //})
      if (this.loggedIn) {
        axios(host + '/project-api/library/origin/?origin=' + this.id)
        .then((resp) => {
          axios(host + '/project-api/library/language/list')
          .then((res) => {
            let j = 0
            let arr = []

            for (let i = 0; i < res.data.data.length; i++) {
              if (res.data.data[i].id != resp.data.data.origin.origin_language.id) {
                arr[j] = res.data.data[i]
                j++
              }   
            }

            this.languages = arr
          })
        })
      }
    },
    mounted() {
      if (this.loggedIn) document.getElementById('create-translation').style.display = "flex"
    },
    methods: {
        enableBtn() {
          document.getElementById('create-translation-btn').disabled = false
        },
        getUserSettings() {
          this.$store.dispatch('GET_USER_SETTINGS')
        },
        postTxt() {
          const text = document.getElementById('text-area').value
          console.log("text: ", document.getElementById('text-area').value)
          if (text !== '') {
            const blob = new Blob([text], {
              type: 'text/plain'
            })
            this.file = blob

            var sel = document.getElementById('select-translation-lang').selectedIndex
            var selectedLang = document.getElementById('select-translation-lang').options[sel].value

            this.$store.dispatch('TRANSLATION_ADD', {
              origin: this.id,
              language: selectedLang,
              file: this.file
            })

            this.$router.push('/book/' + this.id)
          }
          else {
            alert('Сначала напишите что-нибудь!')
          }
        }
    },
    components: {
        ButtonBlack
    }
}
</script>

<style scoped>
.origin-read-frame {
  width: 955px;
  min-width: 940px;
  max-width: 955px;
  height: 37vh;
  min-height: 90px;
  padding: 2px;
}
textarea {
  width: 950px;
  max-width: 950px;
  min-width: 935px;
  height: 37vh;
  min-height: 90px;
}

.create-translation {
  display: none;
  justify-content: flex-end;
  align-items: center;
}

.create-translation > span {
  align-self: center;
}
</style>