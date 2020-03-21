<template>
  <DefaultLayout>
    <PageHeader>
        <template v-slot:header>Отложенное</template>
        <template v-slot:header-desc>На данной странице отображены отложенные книги пользователя.</template>
    </PageHeader>
  </DefaultLayout>
</template>

<script>
import DefaultLayout from '@/layouts/DefaultLayout'
import PageHeader from '@/components/PageHeader'

export default {
    name: 'About',
    created () {
      document.title = "Отложенное: Имя пользователя - Langchanger";
    },

    components: {
        DefaultLayout,
        PageHeader
    }
}
</script>