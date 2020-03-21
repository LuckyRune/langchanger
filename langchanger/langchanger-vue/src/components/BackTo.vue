<template>
  <router-link :to="link" tag="button" class="mb20">
    <span class="mr10">🡰</span>
    <span class="back-desc"><slot/></span>
  </router-link>
</template>

<script>
export default {
    name: 'BackTo',

    props: {
        link: String
    }
}
</script>

<style scoped>
button {
  padding: 5px 10px;
  margin-top: -20px;
  border-radius: 4px;
  background-color: white;
  outline: 0;
  border: 0;
}

span {
  font-size: 24px;
}

.back-desc, span {
  color: var(--text-link);
}

button:hover {
  box-shadow: 0 0 4px black;
  background-color: var(--text-link);
  cursor: pointer;
}

button:hover span, button:hover .back-desc {
  color: white;
}

button:active {
  box-shadow: 0 0 4px black inset;
}
</style>