<template>
  <div class="svg-placeholder" :style="{ width: width + 'px', height: height + 'px'}">
    <img src="@/assets/svg/book.svg">
  </div>
</template>

<script>
export default {
    name: 'Book',

    props: {
        width: String,
        height: String
    }
}
</script>

<style scoped>
div {
  width: 126px;
  height: 200px;
}
</style>