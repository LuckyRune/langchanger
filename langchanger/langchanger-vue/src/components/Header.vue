<template>
    <header>
        <div class="username-div"><p v-if="loggedIn" id="username-p">Вы вошли как: <a :href="/user/ + USERID">{{CLIENT_USERNAME}}</a></p></div>
        <nav>
            <Finder/>
            <router-link :to="{ name: 'Home' }"><img src="@/assets/svg/logo.svg"></router-link>
            <MainMenu/>
        </nav>
        <div>
            <router-link to="/login" v-if="!loggedIn"><ButtonWhite class="sign-in" value="Войти"/></router-link>
            <router-link to="/logout" v-if="loggedIn"><ButtonWhite class="sign-in" value="Выйти"/></router-link>
            <img src="@/assets/svg/sign-in.svg">
        </div>
    </header>
</template>

<script>
import Finder from '@/components/Finder'
import MainMenu from '@/components/MainMenu'
import ButtonWhite from '@/components/ButtonWhite'
import axios from 'axios'
import {mapActions, mapGetters} from 'vuex'

export default {
    name: 'Header',
    created() {
        if(this.loggedIn) {
            this.GET_USER_SETTINGS()
        }
    },
    methods: {
        ...mapActions([
            'GET_USER_SETTINGS'
        ])
    },
    computed: {
        ...mapGetters([
            'CLIENT_USERNAME',
            'USERID',
            'loggedIn'
        ])
    },
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

p {
  color: white
}

.username-div {
  justify-self: start;
  margin-left: 20px;
}

a {
  color: var(--secondary)
}

a:hover {
  color: white
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
