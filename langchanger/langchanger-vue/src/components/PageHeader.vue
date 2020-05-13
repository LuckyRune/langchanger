<template>
  <header>
    <h3><slot name="header"/></h3>
    <p><slot name="header-desc"/></p>
  </header>
</template>

<script>
export default {
    name: 'PageHeader'
}
</script>

<style scoped>
header {
  margin-bottom: 20px;
}

p {
  color: var(--text-desc);
  font-size: 14px;
}
</style>