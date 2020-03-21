<template>
    <button>
        {{ value }}
    </button>
</template>

<script>
export default {
    name: 'ButtonAccent',

    props: {
        value: String
    }
}
</script>

<style scoped>
    button {
        width: 150px;
        height: 40px;
        font-size: 18px;
        border: 1px solid var(--large-accent);
        border-radius: 6px;
        color: var(--large-accent);
        background-color: white;
    }

    button:hover {
        box-shadow: 0 0 3px black;
        cursor: pointer;
    }

    button:active {
        background-color: var(--large-accent);
        color: white;
        box-shadow: 0 0 3px black inset;
    }
</style>