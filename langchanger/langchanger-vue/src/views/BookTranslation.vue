<template>
  <div>
    <div class="edit-bar mb10">
      <div class="edit-props">
          <div class="edit-prop">
              <span>Версия от:</span>
              <span>{{ last_change }}</span>
          </div>
          <div class="edit-prop">
              <span>Язык:</span>
              <span>{{ language }}</span>
          </div>
          <div id="edit-translation">
            <router-link :to="/editing/ + this.id"><button class="btnBlack">Изменить</button></router-link>
          </div>
          <!-- <div class="edit-prop">
              <span>Рейтинг:</span>
              <span><span>234</span></span>
          </div>
          <div class="edit-rating">
            <span id="edit-rating-dislike" class="mr5">-</span>
            <span id="edit-rating-like">+</span>
          </div> -->
      </div>
      <a class="authorBar" :href="/user/ + authorId">
        <span class="mr5">Автор:</span>
        <span class="mr10">{{ author }}</span>
        <!-- <span>(<span>345</span>)</span> -->
      </a>
    </div>

    <textarea id="translation-read-area" readonly>
        
    </textarea>
  </div>
</template>

<script>
import axios from 'axios'
import { cors, host } from '../vars.js'
import { mapGetters, mapMutations } from 'vuex'

export default {
    name: 'BookTranslation',
    data() {
      return {
        id: this.$route.params.id,
        author: '',
        authorId: '',
        language: '',
        last_change: ''
      }
    },
    created () {
      axios(host + 'project-api/library/translation/read/?translation=' + this.id)
      .then((response) => {

        var file = response.data.data.last_version.version_link.file
        axios(cors + file)
          .then((res) => {
          document.getElementById('translation-read-area').value = res.data
        })

        this.authorId = response.data.data.translation.author.id
        this.author = response.data.data.translation.author.username
        this.language = response.data.data.translation.language.name
        this.last_change = response.data.data.last_version.creation_date.substr(0, 10)
        document.title = "Перевод " + response.data.data.translation.author.username + " - Langchanger"
      })

      setTimeout(this.editShow, 500)
    },
    methods: {
      editShow() {
      if (this.author == this.$store.getters.CLIENT_USERNAME) {
        console.log(1)
        document.getElementById('edit-translation').style.display = "block"
      }
      }
    }
}
</script>

<style scoped>
.edit-bar {
  display: flex;
  justify-content: space-between;
}

.edit-props {
    display: flex;
}

.edit-prop {
  display: flex;
  flex-direction: column;
  margin-right: 20px;
  font-size: 20px;
}

.edit-prop > span:nth-child(1) {
  color: var(--text-desc);
  font-size: 18px;
}

.edit-rating {
  display: flex;
  justify-content: center;
}

#edit-rating-like, #edit-rating-dislike {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 46px;
  height: 46px;
  cursor: pointer;
  background-color: var(--secondary);
  color: white;
  border-radius: 6px;
  font-size: 24px;
}

#edit-rating-like:hover, #edit-rating-dislike:hover {
  box-shadow: 0 0 2px black;
}

#edit-rating-like:hover {
  background-color: var(--text-link);
}

#edit-rating-dislike:hover {
  background-color: var(--large-accent);
}

textarea {
  width: 940px;
  min-width: 940px;
  max-width: 940px;
  height: 75vh;
  min-height: 90px;
  padding: 10px;
}

.authorBar {
  display: flex;
  align-items: center;
  color: var(--text-link);
  font-size: 20px;
}

.authorBar span:nth-child(1) {
  color: black;
}

.authorBar:hover > div {
  box-shadow: 0 0 2px black;
}

.authorBar:active > div {
  box-shadow: 0 0 2px black inset;
}

#edit-translation {
  display: none;
}
</style>