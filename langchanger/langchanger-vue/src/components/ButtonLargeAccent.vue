<template>
    <button>
        {{ value }}
    </button>
</template>

<script>
export default {
    name: 'ButtonLargeAccent',

    props: {
        value: String
    }
}
</script>

<style scoped>
button {
    width: 250px;
    height: 60px;
    font-size: 24px;
    text-transform: uppercase;
    border: 0;
    border-radius: 6px;
    color: white;
    background-color: var(--large-accent);
}

button:hover {
    box-shadow: 0 0 3px black;
    cursor: pointer;
}

button:active {
    background-color: white;
    border: 1px solid var(--large-accent);
    color: var(--large-accent);
    box-shadow: 0 0 3px black inset;
}
</style>