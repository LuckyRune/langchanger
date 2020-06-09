<template>
  <div>
    <PageHeader>
      <template v-slot:header>Библиотека</template>
      <template v-slot:header-desc>На данной странице отображены книги, отсортированные по актуальности.</template>
    </PageHeader>
    <section class="book-list">
      <aside>
        <div>
            <h4>Сортировка</h4>
            <span>
                <input type="radio" id="book-featured" name="book-sort" checked>
                <label for="book-featured">По актуальности</label>
            </span>
            <span>
                <input type="radio" id="book-popular" name="book-sort">
                <label for="book-popular">По популярности</label>
            </span>
        </div>
        <div>
            <h4>Формат</h4>
            <span>
              <input type="checkbox" id="book-book" name="book-type">
              <label for="book-book">Книга</label>
            </span>
            <span>
              <input type="checkbox" id="book-guide" name="book-type">
              <label for="book-guide">Руководство</label>
            </span>
        </div>
        <div>
            <h4>Жанры</h4>
            <span>
              <input type="checkbox" id="book-romance" name="book-genre">
              <label for="book-romance">Роман</label>
            </span>
            <span>
              <input type="checkbox" id="book-drama" name="book-genre">
              <label for="book-drama">Драма</label>
            </span>
            <span>
              <input type="checkbox" id="book-comedy" name="book-genre">
              <label for="book-comedy">Комедия</label>
            </span>
            <span>
              <input type="checkbox" id="book-tragic" name="book-genre">
              <label for="book-tragic">Трагедия</label>
            </span>
            <span>
              <input type="checkbox" id="book-fantastic" name="book-genre">
              <label for="book-fantastic">Фантастика</label>
            </span>
            <span>
              <input type="checkbox" id="book-military" name="book-genre">
              <label for="book-military">Военное</label>
            </span>
            <span>
              <input type="checkbox" id="book-fantasy" name="book-genre">
              <label for="book-fantasy">Фэнтэзи</label>
            </span>
        </div>
        <div>
            <h4>Возрастной рейтинг</h4>
            <span>
              <input type="checkbox" id="book-0" name="book-agelimit">
              <label for="book-0">0+</label>
            </span>
            <span>
              <input type="checkbox" id="book-6" name="book-agelimit">
              <label for="book-6">6+</label>
            </span>
            <span>
              <input type="checkbox" id="book-12" name="book-agelimit">
              <label for="book-12">12+</label>
            </span>
            <span>
              <input type="checkbox" id="book-16" name="book-agelimit">
              <label for="book-16">16+</label>
            </span>
            <span>
              <input type="checkbox" id="book-18" name="book-agelimit">
              <label for="book-18">18+</label>
            </span>
        </div>
      </aside>
      <section class="origin-table">
        <OriginTable/>
      </section>
    </section>
  </div>
</template>

<script>
import Pagination from '@/components/Pagination'
import PageHeader from '@/components/PageHeader'
import OriginTable from '@/components/OriginTable'

export default {
    name: 'Library',
    created () {
      document.title = "Библиотека - Langchanger";
    },
    components: {
        Pagination,
        PageHeader,
        OriginTable
    },

}
</script>

<style scoped>
p {
  color: var(--text-desc);
  font-size: 14px;
}

h4 {
  font-size: 18px;
  text-transform: uppercase;
  color: var(--primary);
}

.book-list {
  display: flex;
}

aside {
  margin-top: 50px;
  margin-right: 20px;
}

aside div {
  margin-bottom: 20px;
}

aside h4 {
  margin-bottom: 10px;
}

aside span {
  display: block;
}

input[type=checkbox], input[type=radio] {
  position:absolute;
  z-index:-1000;
  left:-1000px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  height:1px;
  width:1px;
  margin:-1px;
  padding:0;
  border:0;
}

input[type=checkbox] + label, input[type=radio] + label {
  padding-left:21px;
  height:16px; 
  display:inline-block;
  line-height:16px;
  background-repeat:no-repeat;
  background-position: 0 0;
  font-size:14px;
  vertical-align:middle;
  cursor:pointer;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  margin-bottom: 5px;
}

input[type=checkbox] + label {
  background-image:url(../assets/elements/checkboxsheet.png);
}

input[type=radio] + label {
  background-image:url(../assets/elements/radiosheet.png);
}

input[type=checkbox]:checked + label, input[type=radio]:checked + label {
  background-position: 0 -16px;
}

.origin-table {
  width: 800px;
}
</style>