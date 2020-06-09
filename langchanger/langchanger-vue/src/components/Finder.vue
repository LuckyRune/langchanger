<template>
  <div class="dropdown-search">
      <input type="text" placeholder="Поиск..." class="dropdown-input" v-model="inputValue">
      <div class="dropdown-list" v-show="inputValue && apiLoaded">
        <div class="dropdown-item" v-for="origin in origins" :key="origin.id" v-show="originVisible(origin)" @click="selectOrigin(origin)">
          {{ origin.title }}
        </div>
      </div>
      <!-- <button><img src="@/assets/svg/finder.svg"></button> -->
  </div>
</template>

<script>
import OriginLink from '@/components/OriginLink'
import Vue from 'vue'
import {AutoCompletePlugin } from '@syncfusion/ej2-vue-dropdowns'
import axios from 'axios'
import { host } from '../vars.js'
Vue.use(AutoCompletePlugin)
export default {
    name: 'Finder',
    data: function() {
      return {
        inputValue: '',
        origins:[],
        apiLoaded: false,
        selectedOrigin: {}
      }
    },
    components: {
      OriginLink
    },
    mounted() {
      this.getOrigins()
    },
    methods: {
      getOrigins() {
        axios(host + 'project-api/library/origin/all/?page_size=999999999999')
        .then((response) => {
          var foo = []
          for (let i = 0; i < response.data.data.length; i++) {
            let orig = new Object()
            orig = {
              id: response.data.data[i].id,
              title: response.data.data[i].title
            }
            this.origins.push(orig)
          }
          this.apiLoaded = true
        })
      },

      originVisible(origin) {
        let curName = origin.title.toLowerCase()
        let curInput = this.inputValue.toLowerCase()
        return curName.includes(curInput)
      },
        
      selectOrigin(theOrigin) {
        this.selectedOrigin = theOrigin
        this.inputValue = ''
        this.$emit('on-item-selected', theOrigin)
        this.$router.push('/book/' + theOrigin.id)
        this.$router.go()
      }
    }
}
</script>

<style scoped>
.dropdown-search {
  position: relative;
  width: 350px;
  height: 40px;
}

.dropdown-list{
  position: absolute;
  width: 100%;
  max-height: 500px;
  margin-top: 4px;
  overflow-y: auto;
  background: #ffffff;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  border-radius: 8px;
}

.dropdown-item{
  display: flex;
  padding: 11px 16px;
  cursor: pointer;
}
.dropdown-item:hover{
  background: #edf2f7;
}

input {
  padding-left: 5px;
  padding-right: 25px;
  border: 0;
  border-radius: 6px;
  width: 100%;
  height: 100%;
  font-size: 16px;
}

input:focus {
  box-shadow: 0 0 3px black;
}

button {
  position: absolute;
  right: 10px;
  border: 0;
  background: transparent;
  cursor: pointer;
  height: 20px;
}
</style>

<style>

</style>
