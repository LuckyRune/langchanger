<template>
  <div>
    <h3 class="mb20">{{ username }}</h3>
    <div class="user-info mb20">
        <UserIcon poster="/usericon.svg" class="mr20"/>
        <div>
            <p class="mb10"><span class="accent">Рейтинг: </span><span id="user-rating">0</span></p>
            <button @click="showModal = true" class="mb10"><h5 class="link"><span class="mr5">Достижения</span></h5></button>
            <p class="mb10">Достижений пока нет.</p>
            <!-- <div class="user-achievements mb10">
                <PlaceholderEqual size="50" value="achievement"/>
                <PlaceholderEqual size="50" value="achievement"/>
                <PlaceholderEqual size="50" value="achievement"/>
                <PlaceholderEqual size="50" value="achievement"/>
            </div> -->
            <a href="/user-onhold"><h5 class="link"><span class="mr5">Отложенное</span></h5></a>
            <p>Отложенного пока нет.</p>
        </div>
    </div>
    <div class="user-desc mb40">
        <h5 class="mb5">Описание</h5>
        <p v-if="description != null ">{{ description }}</p>
        <p v-else>Без описания.</p>
    </div>
    <div>
        <h5 class="mb10">Переводы</h5>
        <p v-if="!translations.length > 0">Пока переводов нет.</p>
        <table v-if="translations.length > 0">
            <tr>
                <th>Название</th>
                <th>Язык перевода</th>
                <th>Последнее изменение</th>
                <th>Версии</th>
                <th></th>
            </tr>
            <tr v-for="translation in translations" :key="translation.id">
                <td><a :href="/book/ + translation.origin.id">{{ translation.origin.title }}</a></td>
                <td><a :href="/translation/ + translation.id">{{ translation.language.name }}</a></td>
                <td>{{ translation.creation_date.substr(0, 10) }}</td>
                <td><a :href="/changes/ + translation.id">Посмотреть</a></td>
                <td><button v-if="id == USERID" class="btnDelete" id="delete-translation" :value="translation.id" @click="showDelModal = true">X</button></td>
            </tr>
        </table>
    </div>
    <Modal @close="showModal = false" :show="showModal">
        <header class="mb20">
            <h3 class="mb5">Достижения</h3>
            <p>На данной странице отображены достижения пользователя.</p>
        </header>
        <section>
            <div>
                <h3>Название</h3>
                <div>
                    <!-- <PlaceholderEqual size="150" value="achievement" class="mr5"/> -->
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium dolorem laudantium et cum? Obcaecati perferendis rerum culpa incidunt unde magnam.</p>
                </div>
            </div>
        </section>
    </Modal>
    <Modal @close="showDelModal = false" :show="showDelModal">
      <header class="mb20">
            <h3 class="mb5">Удаление</h3>
      </header>
      <section>
        <p class="subm">Вы действительно хотите удалить перевод?</p>
        <div class="choose">
          <button class="yes" @click="deleteTranslation">Да</button><button class="no">Нет</button>
        </div>
      </section>
    </Modal>
  </div>
</template>

<script>
import UserIcon from '@/components/UserIcon'
import Modal from '@/layouts/DefaultModal'
import axios from 'axios'
import { mapGetters } from 'vuex'

export default {
    name: 'User',
    data() {
      return {
        id: this.$route.params.id,
        username: '',
        profile_icon: '',
        description: '',
        rate: '',
        translations: [],
        showModal: false,
        showDelModal: false
      }
    },
    created () {
      axios('http://127.0.0.1:8000/project-api/user/profile/?user=' + this.id, {
        method: 'GET'
      })
      .then((response) => {
        let user_data = response.data.data.user
        console.log(response.data.data.user)
        this.username = user_data.username
        // this.profile_icon = user_data.user_profile.profile_icon.image
        this.description = user_data.user_profile.description
        this.rate = user_data.rate
        this.translations = response.data.data.translations
        document.title = response.data.data.user.username + " - Langchanger"
      })
    },
    methods: {
      getTranslations() {
        axios('http://127.0.0.1:8000/project-api/user/profile/?user=' + this.id)
        .then((response) => {
        this.translations = response.data.data.translations
      })
      },
      deleteTranslation() {
        this.showDelModal = false
        this.$store.dispatch('DELETE_TRANSLATION', {
          translation: document.getElementById('delete-translation').value
        })
        setTimeout(this.getTranslations, 500)
      }
    },
    computed: {
        ...mapGetters([
            'USERID'
        ])
    },
    components: {
        UserIcon,
        Modal
    }
}
</script>

<style scoped>
.accent {
  color: var(--text-accent);
}

.link {
  color: var(--text-link);
}

h5 {
  font-size: 22px;
}

.user-info {
  display: flex;
}

.user-desc p {
  width: 800px;
}

a {
  color: var(--text-link);
}

button {
  border: 0;
  background: transparent;
  cursor: pointer;
}

a h5, button h5 {
  padding: 5px 10px;
  margin: 0 -10px;
  border-radius: 4px;
}

a h5:hover, button:hover h5 {
  box-shadow: 0 0 4px black;
  color: white;
  background-color: var(--text-link);
}

a h5:active, button:active h5 {
  box-shadow: 0 0 4px black inset;
}

.user-achievements {
  display: grid;
  grid-template-columns: 54px 54px 54px 54px;
  grid-gap: 0 5px;
}

table a:hover {
  text-decoration: underline;
}

table {
  border-collapse: collapse;
  width: 800px;
}

th {
  background-color: var(--el-holder);
  color: white;
}

tr:nth-child(odd) {
  background-color: var(--el-background);
}

th, td {
  padding: 10px 0;
  text-align: center;
}

.modal p {
  color: var(--text-desc);
  font-size: 14px;
}

.subm {
  font-size: 15px;
  color: var(--large-accent)!important;
  margin-bottom: 10px;
}

.yes {
  background-color: var(--large-accent);
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  margin-right: 10px;
}

.no {
  background-color: var(--secondary);
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
}

.modal section h3 {
  margin-bottom: 5px;
}

.modal section div > div {
  display: flex;
}

.modal section div > div p {
  width: 460px;
  height: 150px;
  font-size: 18px;
}

.modal section {
  width: 620px;
  height: 70px;
  overflow: auto;
}

.btnDelete {
  background-color: var(--large-accent);
  padding: 6px 8px;
  border-radius: 3px;
  color: white
}

.btnDelete:hover {
  box-shadow: 0 0 2px black;
}
</style>