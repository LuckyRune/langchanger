<template>
  <DefaultLayout>
    <h3 class="mb20">Имя пользователя</h3>
    <div class="user-info mb20">
        <PlaceholderEqual class="mr20" value="usericon"/>
        <div>
            <p class="mb10"><span class="accent">Рейтинг: </span><span id="user-rating">356</span></p>
            <button @click="showModal = true" class="mb10"><h5 class="link"><span class="mr5">Достижения</span><span>(<span id="user-achievements">7</span>)</span></h5></button>
            <div class="user-achievements mb10">
                <PlaceholderEqual size="50" value="achievement"/>
                <PlaceholderEqual size="50" value="achievement"/>
                <PlaceholderEqual size="50" value="achievement"/>
                <PlaceholderEqual size="50" value="achievement"/>
            </div>
            <a href="/user-onhold"><h5 class="link"><span class="mr5">Отложенное</span><span>(<span id="user-on-hold">4</span>)</span></h5></a>
        </div>
    </div>
    <div class="user-desc mb40">
        <h5 class="mb5">Описание</h5>
        <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Architecto, vel! Dignissimos, perferendis. Quo sit fugit a quasi. Fugiat, minima nihil.</p>
    </div>
    <div>
        <h5 class="mb10">Переводы</h5>
        <table>
            <tr>
                <th>Название</th>
                <th>Рейтинг</th>
                <th>Язык перевода</th>
                <th>Последнее изменение</th>
                <th>Изменения</th>
            </tr>
            <tr>
                <td><a href="/book-page">Война и мир</a></td>
                <td>382</td>
                <td><a href="/translation">Английский</a></td>
                <td>20.12.20</td>
                <td>356</td>
            </tr>
            <tr>
                <td><a href="/book-page">Мёртвые души</a></td>
                <td>382</td>
                <td><a href="/translation">Английский</a></td>
                <td>20.12.20</td>
                <td>356</td>
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
                    <PlaceholderEqual size="150" value="achievement" class="mr5"/>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium dolorem laudantium et cum? Obcaecati perferendis rerum culpa incidunt unde magnam.</p>
                </div>
            </div>
        </section>
    </Modal>
  </DefaultLayout>
</template>

<script>
import DefaultLayout from '@/layouts/DefaultLayout'
import PlaceholderEqual from '@/components/PlaceholderEqual'
import Modal from '@/layouts/DefaultModal'

export default {
    name: 'User',
    created () {
      document.title = "Имя пользователя - Langchanger";
    },

    components: {
        DefaultLayout,
        PlaceholderEqual,
        Modal
    },

    data() {
        return {
            showModal: false
        }
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
  width: 1240px;
  height: 550px;
  overflow: auto;
}
</style>