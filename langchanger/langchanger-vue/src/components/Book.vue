<template>
  <div class="svg-placeholder" :style="{ width: width + 'px', height: height + 'px'}">
    <img :src="poster" :style="{ width: width + 'px', height: height + 'px'}">
  </div>
</template>

<script>
export default {
    name: 'Book',

    props: {
        width: String,
        height: String,
        poster: String
    }
}
</script>

<style scoped>
div {
  width: 126px;
  height: 200px;
}
img {
  width: 130px;
  height: 200px;
}
</style>