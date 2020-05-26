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
        this.$router.push('/')
      })
      .catch((error) => {
        this.$router.push('/')
      })
    }
}
</script>