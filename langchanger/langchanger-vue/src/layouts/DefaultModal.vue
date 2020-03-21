<template>
  <transition name="fade">
    <div class="modal-wrapper" v-if="show" @click.self="$emit('close')">
      <div class="modal">
        <img src="@/assets/svg/close.svg" @click="$emit('close')">
        <section>
            <slot/>
        </section>
      </div>
    </div>
  </transition>
</template>
<script>
export default {
    name: 'Achievements',

    props: {
      show: Boolean
    }
}
</script>

<style scoped>
.modal-wrapper {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2;
}

.modal {
  padding: 20px;
  background-color: white;
  border-radius: 6px;
  box-shadow: 0 0 5px black;
  position: relative;
  transition: all .3s;
}

img {
  position: absolute;
  top: 0px;
  right: 0px;
  padding: 20px;
  cursor: pointer;
}

.fade-enter-active, .fade-leave-active {
  transition: all .3s;
}

.fade-enter, .fade-leave-active {
  opacity: 0;
}

.fade-enter .modal, .fade-leave-active .modal {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>