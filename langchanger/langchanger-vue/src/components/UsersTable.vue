<template>
    <div class="users-table">
        <UserLink
        v-for="user in USERS"
        :key="user.id"
        :users_data="user"
        />
    </div>
</template>

<script>
import UserLink from '@/components/UserLink'
import {mapActions, mapGetters} from 'vuex'
export default {
    name: "UserTable",
    components: {
        UserLink
    },
    methods: {
        ...mapActions([
            'GET_USERS'
        ])
    },
    computed: {
        ...mapGetters([
            'USERS'
        ])
    },
    mounted() {
        this.GET_USERS()
    }
}
</script>

<style scoped>
.users-table {
    display: flex;
    flex-wrap: wrap;
}
</style>