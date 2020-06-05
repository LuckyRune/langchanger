<template>
  <div>
    <section>
        <h1>Langchanger</h1>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatum, officiis.</p>
        
        <a href="/login" v-if="!loggedIn"><ButtonLargeAccent class="mr10" value="Войти"/></a>
        <a href="/register" v-if="!loggedIn"><ButtonLargeAccent value="Регистрация"/></a>
    </section>
    <section class="start-most-active">
        <div>
            <h2 class="mr20">Наиболее активные</h2>
            <a href="/library"><ButtonAccent value="К библиотеке"/></a>
        </div>
        <MainOriginTable/>
    </section>    
  </div>
</template>

<script>
import ButtonLargeAccent from '@/components/ButtonLargeAccent'
import ButtonAccent from '@/components/ButtonAccent'
import MainOriginTable from '@/components/MainOriginTable'
import axios from 'axios'
import { mapGetters } from 'vuex'

export default {
    name: 'Home',
    created() {
        document.title = "Langchanger"
    },
    computed: {
        ...mapGetters([
            'loggedIn'
        ])
    },
    components: {
        ButtonLargeAccent,
        ButtonAccent,
        MainOriginTable
    }
}
</script>

<style scoped>
section:nth-child(1) {
    padding: 40px 300px 50px 40px;
}

section:nth-child(2) {
    padding: 0 40px;
}

p {
    font-size: 36px;
    color: var(--text-desc);
    margin-bottom: 40px;
}

.start-most-active > div:nth-child(1) {
    display: flex;
    margin-bottom: 30px;
}

.start-most-active > div:nth-child(2) {
    display: flex;
    margin-bottom: 115px;
}
</style>