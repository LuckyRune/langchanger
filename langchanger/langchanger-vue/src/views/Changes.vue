<template>
    <div>
        <PageHeader>
            <template v-slot:header>Версии</template>
            <template v-slot:header-desc>На данной странице отображены версии перевода.</template>
        </PageHeader>
        <div class="version" v-for="version in versions" :key="version.id"><a :href="/version/ + version.id">Версия от: {{ version.creation_date.substr(0, 10) }}</a></div>
    </div>
</template>

<script>
import PageHeader from '@/components/PageHeader'
import axios from 'axios'
import { cors, host } from '../vars.js'

export default {
    name: 'Changes',
    data() {
        return {
            id: this.$route.params.id,
            versions: []
        }
    },
    created() {
        axios(host + '/project-api/library/version/all/?translation=' + this.id)
        .then((response) => {
            console.log(response.data.data)
            this.versions = response.data.data
        })
    },
    components: {
        PageHeader
    }
}
</script>

<style scoped>
.version a {
  padding: 20px 0;
  color: var(--text-link);
  font-size: 20px
}
.version {
  margin: 20px 0;
}
</style>