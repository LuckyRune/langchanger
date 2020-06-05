<template>
<div class="asd">
    <div class="origin-table">
        <OriginLink
        v-for="origin in ORIGINS"
        :key="origin.id"
        :origins_data="origin"
        />
    </div>
    <!-- <div class="pagination">
          <div class="page"
          v-for="page in pages"
          :key="page"
          >{{ page }}</div>
        </div> -->
    </div>
</template>

<script>
import OriginLink from '@/components/OriginLink'
import {mapActions, mapGetters} from 'vuex'
export default {
    name: "OriginTable",
    data () {
      return {
        originsPerPage: 15,
        pageNumber: 1
      }
    },
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
        ]),
    //     pages() {
    //     return Math.ceil(this.ORIGINS.length / 10)
    //   },
    //   paginatedUsers() {
    //       let from = (this.pageNumber - 1) * this.usersPerPage
    //       let to = from + this.usersPerPage
    //       return this.ORIGINS.slice(from, to)
    //   }
    },
    mounted() {
        this.GET_ORIGINS()
    }
}
</script>

<style scoped>
.asd {
    display: flex;
    flex-direction: column;
}

.origin-table {
    display: flex;
    flex-wrap: wrap;
}

.pagination {
    display: flex;
    justify-content: center;
}

.page {
    padding: 8px;
    border: 1px solid black;
    margin: 1px;
}
</style>