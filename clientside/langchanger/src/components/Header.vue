<template>
    <header>
        <div></div>
        <nav>
            <Finder/>
            <a href="/"><img src="@/assets/svg/logo.svg"></a>
            <MainMenu/>
        </nav>
        <div>
            <router-link to="/login"><ButtonWhite class="sign-in" value="Войти"/></router-link>
            <img src="@/assets/svg/sign-in.svg">
        </div>
    </header>
</template>

<script>
import Finder from '@/components/Finder'
import MainMenu from '@/components/MainMenu'
import ButtonWhite from '@/components/ButtonWhite'

export default {
    name: 'Header',

    components: {
        Finder,
        MainMenu,
        ButtonWhite
    }
}
</script>

<style scoped>
header {
    position: sticky;
    top: 0;
    z-index: 1;
    height: 60px;
    background-color: var(--primary);
    display: grid;
    grid-template-columns: 1fr 1000px 1fr;
    align-items: center;
    box-shadow: 0 0 7px black;
}

nav img {
    height: 30px;
    display: block;
}

nav {
    display: flex;
    align-items: center;
    justify-content: space-around;
}

div {
    justify-self: end;
    margin-right: 20px;
}

div > img {
    display: block;
}

.sign-in {
    display: none;
}

@media screen and (min-width: 1360px) {
    .sign-in {
        display: block;
    }

    div > img {
        display: none;
    }
}
</style>
