<template>
  <v-main class="section">
    <v-container class="container">
      <v-row>
        <v-col cols="12">
          <h1>Hey {{ loggedInUser.first_name }}</h1>
          <div class="content">
            <p>
              <strong>Email:</strong>
              {{ loggedInUser.email }}
            </p>
            <p>
              <strong>Bio:</strong>
              {{ loggedInUser.bio }}
              <strong>Trades:</strong>
              <span v-for="trade_id in loggedInUser.trades">
<!--                {{ // getCardName(trade_id) }}-->
                <!--                {{ this.cards }}-->
                {{ trade_id }}
              </span>

              <strong>Wants:</strong>
              {{ loggedInUser.wants }}
            </p>

          </div>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  middleware: 'auth',
  computed: {
    ...mapGetters(['loggedInUser'])
  }
  ,
  data() {
    return {
      cards: []
    };
  },
  methods: {
    async getCardName(card_id) {
      try {

        this.loggedInUser.trades.forEach(trade_id => {
            // let card = await this.$axios.$get(`/api/cards/${card_id}/`); // delete recipe

          }
        )
        // let newRecipes = await this.$axios.$get("/api/cards/"); // get new list of recipes
        // this.recipes = card; // update list of recipes
      } catch (e) {
        console.log(e);
      }
    }
  },
}
</script>
