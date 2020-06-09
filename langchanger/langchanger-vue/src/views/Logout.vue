<template>
  <div>
    
  </div>
</template>

<script>

export default {
    name: 'Logout',
    created () {
      this.$store.dispatch('DESTROY_TOKEN')
      .then((response) => {
        this.$router.push({ name: 'Home' })
      })
      .catch((error) => {
        this.$router.push({ name: 'Home' })
      })
    }
}
</script>