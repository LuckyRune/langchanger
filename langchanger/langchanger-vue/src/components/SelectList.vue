<template>
  <select :id="id" v-model="select">
      <option v-for="option in options" :key="option.id" :value="option.id">{{ option.name }}</option>
  </select>
</template>

<script>
export default {
    name: 'SelectList',
    data() {
      return {
        select: ''
      }
    },
    props: {
        id: String,
        options: Array
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