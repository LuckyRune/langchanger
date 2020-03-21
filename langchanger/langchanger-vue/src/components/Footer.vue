<template>
  <footer>
      <span>© Copyright 2020</span>
  </footer>
</template>

<script>
export default {
    name: 'Footer'
}
</script>

<style scoped>
  footer {
      display: flex;
      justify-content: flex-end;
      align-items: flex-end;
      height: 50px;
      background-color: #545871;
      color: white;
      font-size: 14px;
  }

  span {
      padding: 5px;
  }
</style>