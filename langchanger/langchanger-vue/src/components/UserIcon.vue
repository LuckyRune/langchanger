<template>
  <div class="svg-placeholder" :style="{ width: size + 'px', height: size + 'px' }">
      <img v-if="poster != null" :src="poster" :style="{ width: size + 'px', height: size + 'px' }">
      <img v-else src="@/assets/svg/usericon.svg" :style="{ width: size + 'px', height: size + 'px' }">
  </div>
</template>

<script>
export default {
    name: 'UserIcon',

    props: {
        size: String,
        poster: String
    }
}
</script>

<style scoped>
div, img {
  width: 250px;
  height: 250px;
}
</style>