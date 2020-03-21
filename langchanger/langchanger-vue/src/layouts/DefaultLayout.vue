<template>
  <div>
    <Header/>
    <section id="content">
      <div id="wrapper">
          <section id="main">
              <slot/>
          </section>
          <Footer/>
      </div>
    </section>
  </div>
</template>

<script>
import Header from '@/components/Header'
import Footer from '@/components/Footer'

export default {
    name: 'DefaultLayout',

    components: {
        Header,
        Footer
    }
}
</script>


<style scoped>
#main {
  padding: 50px 20px 40px 20px;
}

#content {
  display: flex;
  align-items: center;
  flex-direction: column;
}

#wrapper {
  margin-top: -10px;
  z-index: 0;
  box-shadow: 0 0 7px black;
}

#wrapper, footer {
  width: 1000px;
}
</style>