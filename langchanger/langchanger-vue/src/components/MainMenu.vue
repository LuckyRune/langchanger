<template>
    <ul>
        <li><a href="/library">Библиотека</a></li>
        <li><a href="/users">Пользователи</a></li>
        <li><a href="/about">О сайте</a></li>
    </ul>
</template>

<script>
export default {
    name: 'MainMenu'
}
</script>

<style scoped>
    li {
        list-style: none;
        display: inline-block;
        text-transform: uppercase;
    }

    a {
        font-size: 18px;
        text-decoration: none;
        color: var(--text-secondary);
        padding: 20px 10px;
    }

    a:hover {
        box-shadow: 0 0 3px black;
    }

    a:active {
        box-shadow: inset 0 0 3px black;
    }
</style>
