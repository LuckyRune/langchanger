<template>
  <DefaultLayout>
    <PageHeader>
        <template v-slot:header>Пользователи</template>
        <template v-slot:header-desc>На данной странице отображены пользователи.</template>
    </PageHeader>
  </DefaultLayout>
</template>

<script>
import DefaultLayout from '@/layouts/DefaultLayout'
import PageHeader from '@/components/PageHeader'

export default {
    name: 'Users',
    created () {
      document.title = "Пользователи - Langchanger";
    },

    components: {
        DefaultLayout,
        PageHeader
    }
}
</script>