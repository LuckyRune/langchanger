<template>
  <div>
    <div class="create-translation mb10">
      <button class="btnBlack" @click="saveVersion">Сохранить</button>
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
    name: 'AddVersion',
    data() {
      return {
        id: this.$route.params.id,
        source_link: '',
        origin: '',
        file: {}
      }
    },
    computed: {
        ...mapGetters([
            'loggedIn'
        ])
    },
    created () {
         axios(host + '/project-api/library/translation/read/?translation=' + this.id)
         .then((response) => {
           this.origin = response.data.data.translation.origin

             axios(host + '/project-api/library/origin/read/?origin=' + this.origin)
            .then((resp) => {
              var file = resp.data.data.source_link.file
              axios(cors + file)
              .then((res) => {
                document.getElementById('origin-text').value = res.data
              })
              })
            //axios(host + 'origins/' + this.origin + '.txt')
            //.then((resp) => {
            //document.getElementById('origin-text').value = resp.data
            //})
              
              var text = response.data.data.last_version.version_link.file
              axios(cors + text)
                .then((respon) => {
                document.getElementById('text-area').value = respon.data
              })
         })
    },
    methods: {
        saveVersion() {
          const text = document.getElementById('text-area').value
          console.log("text: ", document.getElementById('text-area').value)
          if (text !== '') {
            const blob = new Blob([text], {
              type: 'text/plain'
            })
            this.file = blob

            this.$store.dispatch('ADD_VERSION', {
              translation: this.id,
              file: this.file
            })

            this.$router.push('/book/' + this.origin)
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
  justify-content: flex-end;
  align-items: center;
}

.create-translation > span {
  align-self: center;
}
</style>