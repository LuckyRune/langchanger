<template>
  <div>
    <PageHeader>
        <template v-slot:header>Пользователи</template>
        <template v-slot:header-desc>На данной странице отображены пользователи.</template>
    </PageHeader>
    <section class="user-list">
      <aside>
        <div>
            <h4>Сортировка</h4>
            <span>
                <input type="radio" id="book-featured" name="book-sort" checked>
                <label for="book-featured">По имени</label>
            </span>
            <span>
                <input type="radio" id="book-popular" name="book-sort">
                <label for="book-popular">По рейтингу</label>
            </span>
        </div>
      </aside>
      <section>
        <UsersTable/>
      </section>
    </section>
  </div>
</template>

<script>
import PageHeader from '@/components/PageHeader'
import UsersTable from '@/components/UsersTable'

export default {
    name: 'Users',
    created () {
      document.title = "Пользователи - Langchanger";
    },

    components: {
        PageHeader,
        UsersTable
    }
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

.user-list {
  display: flex;
}

aside {
  margin-top: 50px;
  margin-right: 60px;
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
</style>