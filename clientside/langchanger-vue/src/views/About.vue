<template>
  <DefaultLayout>
    
  </DefaultLayout>
</template>

<script>
import DefaultLayout from '@/layouts/DefaultLayout'

export default {
    name: 'About',
    created () {
      document.title = "О сайте - Langchanger";
    },

    components: {
        DefaultLayout
    }
}
</script>