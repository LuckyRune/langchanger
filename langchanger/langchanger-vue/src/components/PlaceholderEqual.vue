<template>
  <div class="svg-placeholder" :style="{ width: size + 'px', height: size + 'px' }">
      <img :src="require('@/assets/svg/' + value + '.svg')">
  </div>
</template>

<script>
export default {
    name: 'PlaceholderEqual',

    props: {
        size: String,
        value: String
    }
}
</script>

<style scoped>
div {
  width: 250px;
  height: 250px;
}
</style>