<template>
  <select :id="id">
      <option v-for="option in options" :key="option.value" :value="option.value">{{ option.text }}</option>
  </select>
</template>

<script>
export default {
    name: 'SelectList',

    props: {
        id: String,
        options: Object
    }
}
</script>

<style scoped>
select {
  width: 150px;
  height: 40px;
  font-size: 16px;
  box-shadow: 0 0 2px black;
  border-radius: 6px;
  margin-right: 10px;
}

select:hover {
  box-shadow: 0 0 4px black;
}
</style>