<template>
    <button>
        {{ value }}
    </button>
</template>

<script>
export default {
    name: 'ButtonBlack',
  
    props: {
        value: String
    }
}
</script>

<style scoped>
button {
  min-width: 150px;
  height: 40px;
  padding: 0 10px;
  font-size: 18px;
  text-transform: uppercase;
  border: 0;
  border-radius: 4px;
  background-color: var(--secondary);
  color: white;
}

button:hover {
  box-shadow: 0 0 3px black;
  cursor: pointer;
}

button:active {
  background-color: white;
  color: var(--secondary);
  border: 1px solid var(--secondary);
  box-shadow: 0 0 3px black inset;
}
</style>