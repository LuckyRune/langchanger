<template>
    <div>
        <h3 class="mb20">Версия от: {{ date }}</h3>
        <textarea id="version-read" readonly></textarea>
    </div>
</template>

<script>
import axios from 'axios'
import { cors } from '../vars.js'
 
export default {
    name: 'VersionRead',
    data() {
        return {
            id: this.$route.params.id,
            date: ''
        } 
    },
    created() {
        axios(host + '/project-api/library/version/differences/?version=' + this.id)
        .then((response) => {
            console.log(response.data.data.current_version)
            this.date = response.data.data.current_version.creation_date.substr(0, 10)
            var file = response.data.data.current_version.version_link.file
            axios(cors + file)
            .then((resp) => {
                document.getElementById('version-read').value = resp.data
            })
        })
    }
}
</script>

<style scoped>
textarea {
  width: 950px;
  min-width: 950px;
  max-width: 950px;
  height: 75vh;
  min-height: 200px;
}
</style>