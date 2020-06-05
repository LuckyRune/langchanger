<template>
  <div>
    <PageHeader>
        <template v-slot:header>Отложенное</template>
        <template v-slot:header-desc>На данной странице отображены отложенные книги пользователя.</template>
    </PageHeader>
  </div>
</template>

<script>
import PageHeader from '@/components/PageHeader'

export default {
    name: 'About',
    created () {
      document.title = "Отложенное: Имя пользователя - Langchanger";
    },

    components: {
        PageHeader
    }
}
</script>