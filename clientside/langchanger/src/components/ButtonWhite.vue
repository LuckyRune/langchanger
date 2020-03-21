<template>
    <button>
        {{ value }}
    </button>
</template>

<script>
export default {
    name: 'ButtonWhite',

    props: {
        value: String
    }
}
</script>

<style scoped>
button {
    min-width: 150px;
    height: 40px;
    padding: 0 10px;
    font-size: 18px;
    text-transform: uppercase;
    border: 0;
    border-radius: 4px;
    background-color: white;
}

button:hover {
    box-shadow: 0 0 3px black;
    cursor: pointer;
}

button:active {
    background-color: #545871;
    color: white;
    box-shadow: 0 0 3px black inset;
}
</style>