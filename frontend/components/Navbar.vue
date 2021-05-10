<template>
  <v-app-bar :clipped-left="clipped" fixed app>
    <v-app-bar-nav-icon @click.stop="drawer = !drawer"/>
    <v-btn icon @click.stop="miniVariant = !miniVariant">
      <v-icon>mdi-{{ `chevron-${miniVariant ? 'right' : 'left'}` }}</v-icon>
    </v-btn>
    <v-btn icon @click.stop="clipped = !clipped">
      <v-icon>mdi-application</v-icon>
    </v-btn>
    <v-btn icon @click.stop="fixed = !fixed">
      <v-icon>mdi-minus</v-icon>
    </v-btn>
    <v-toolbar-title v-text="title"/>

    <v-spacer/>
    <div class="authentication-buttons">
      <div v-if="isAuthenticated">

        <v-btn light to="/profile" class="text-lowercase">
          <v-icon dark>mdi-account</v-icon>
          {{ loggedInUser.email }}
        </v-btn>


        <v-btn icon @click="logout()" class="logout-btn">

          <v-icon light>mdi-logout</v-icon>
        </v-btn>
      </div>
      <div v-else>
        <v-btn icon to="/login" class="login-btn">
          <v-icon>mdi-login</v-icon>
        </v-btn>
        <v-btn icon to="/register" class="register-btn">
          <v-icon>mdi-account-key-outline</v-icon>
        </v-btn>
      </div>
    </div>


    <v-btn icon @click.stop="rightDrawer = !rightDrawer">
      <v-icon>mdi-menu</v-icon>
    </v-btn>
  </v-app-bar>

</template>
<script>
import {mapGetters} from 'vuex'

export default {
  data() {
    return {
      title: 'Home',

      clipped: false,
      drawer: false,
      fixed: false,
      miniVariant: false,
      right: true,
      rightDrawer: false,
    }
  },
  computed: {
    ...mapGetters(['isAuthenticated', 'loggedInUser'])
  }, methods: {
    async logout() {
      await this.$auth.logout();
    },
  },
}
</script>
