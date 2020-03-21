<template>
  <div>
      <input type="text" placeholder="Поиск...">
      <button><img src="@/assets/svg/finder.svg"></button>
  </div>
</template>

<script>
export default {
    name: 'Finder'
}
</script>

<style scoped>
div {
  position: relative;
  display: flex;
  align-items: center;
  width: 350px;
  height: 40px;
}

input {
  padding-left: 5px;
  padding-right: 40px;
  border: 0;
  border-radius: 6px;
  width: 100%;
  height: 100%;
  font-size: 16px;
}

input:focus {
  box-shadow: 0 0 3px black;
}

button {
  position: absolute;
  right: 10px;
  border: 0;
  background: transparent;
  cursor: pointer;
  height: 20px;
}
</style>
