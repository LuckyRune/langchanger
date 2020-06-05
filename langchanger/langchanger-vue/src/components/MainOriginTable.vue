<template>
    <div class="origins-table">
        <OriginLink
        v-for="origin in limitedOrigins"
        :key="origin.id"
        :origins_data="origin"
        />
    </div>
</template>

<script>
import OriginLink from '@/components/OriginLink'
import {mapActions, mapGetters} from 'vuex'
export default {
    name: "MainOriginTable",
    components: {
        OriginLink
    },
    methods: {
        ...mapActions([
            'GET_MAIN_ORIGINS'
        ])
    },
    computed: {
        ...mapGetters([
            'MAIN_ORIGINS'
        ]),
        limitedOrigins() {
            return this.MAIN_ORIGINS.slice(0, 6)
        }
    },
    mounted() {
        this.GET_MAIN_ORIGINS()
    }
}
</script>

<style scoped>
.origins-table {
    display: flex;
}
</style>