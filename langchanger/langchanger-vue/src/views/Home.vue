<template>
  <DefaultLayout>
    <section>
        <h1>Langchanger</h1>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatum, officiis.</p>
        
        <a href="/login"><ButtonLargeAccent class="mr10" value="Войти"/></a>
        <a href="/register"><ButtonLargeAccent value="Регистрация"/></a>
    </section>
    <section class="start-most-active">
        <div>
            <h2 class="mr20">Наиболее активные</h2>
            <a href="/library"><ButtonAccent value="К библиотеке"/></a>
        </div>
        <MainOriginTable/>
    </section>    
  </DefaultLayout>
</template>

<script>
import DefaultLayout from '@/layouts/DefaultLayout'
import ButtonLargeAccent from '@/components/ButtonLargeAccent'
import ButtonAccent from '@/components/ButtonAccent'
import MainOriginTable from '@/components/MainOriginTable'

export default {
    name: 'Home',
    created() {
        document.title = "Langchanger"
    },
    components: {
        DefaultLayout,
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