<template>
<div class="asd">
    <div class="origin-table">
        <OriginLink
        v-for="origin in paginatedOrigins"
        :key="origin.id"
        :origins_data="origin"
        />
    </div>
    <div class="pagination">
          <div class="page" :class="{ 'active-page': page === pageNumber }"
          v-for="page in pages"
          :key="page"
          @click="pageClick(page)"
          >{{ page }}</div>
        </div>
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
        ]),

        pageClick(page) {
            this.pageNumber = page
        }
    },
    computed: {
        ...mapGetters([
            'ORIGINS'
        ]),
        pages() {
        return Math.ceil(this.ORIGINS.length / 10)
      },
      paginatedOrigins() {
          let from = (this.pageNumber - 1) * this.originsPerPage
          let to = from + this.originsPerPage
          return this.ORIGINS.slice(from, to)
      }
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
    box-shadow: 0 0 2px black;
    margin: 2px;
    border-radius: 5px;
}

.page:hover {
  cursor: pointer;
  background-color: var(--secondary);
  color: white;
}

.page:active {
  box-shadow: 0 0 2px black inset;
  background-color: white;
  color: black;
}

.active-page {
  background-color: var(--secondary);
  color: white;
}
</style>