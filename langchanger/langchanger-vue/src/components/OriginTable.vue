<template>
    <div class="origin-table">
        <OriginLink
        v-for="origin in ORIGINS"
        :key="origin.id"
        :origins_data="origin"
        />
    </div>
</template>

<script>
import OriginLink from '@/components/OriginLink'
import {mapActions, mapGetters} from 'vuex'
export default {
    name: "OriginTable",
    components: {
        OriginLink
    },
    methods: {
        ...mapActions([
            'GET_ORIGINS'
        ])
    },
    computed: {
        ...mapGetters([
            'ORIGINS'
        ])
    },
    mounted() {
        this.GET_ORIGINS()
    }
}
</script>

<style scoped>
.origin-table {
    display: flex;
    flex-wrap: wrap;
}
</style>