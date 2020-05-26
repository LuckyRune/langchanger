<template>
  <router-link :to=" '/user/' + users_data.id ">
    <div class="user">
        <UserIcon :poster="image" size="128"/>
        <p class="user-title">{{ users_data.username }}</p>
        <p></p>
    </div>
  </router-link>
</template>

<script>
import UserIcon from '@/components/UserIcon'

export default {
    name: 'UserLink',
    components: {
      UserIcon
    },
    data() {
      return {
        image: ''
      }
    },
    props: {
      users_data: {
            type: Object,
            default: () => {
                return []
            }
        }
    },
    created() {
      if (this.users_data.user_profile.profile_icon == null) this.image = '/usericon.svg'
      else this.image = this.users_data.user_profile.profile_icon.image
    }
}
</script>

<style scoped>
.user {
  margin-bottom: 10px;
}

.user-title {
  max-width: 130px;
  overflow: hidden;
  text-overflow: clip;
}

a {
    text-decoration: none;
    color: black;
    margin-right: 20px;
}

a:hover .user > div {
  box-shadow: 0 0 3px black;
}

a:active .user > div {
  box-shadow: 0 0 3px black inset;
}

p:nth-child(3) {
  font-size: 14px;
  color: var(--text-desc);
}
</style>