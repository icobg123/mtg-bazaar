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
              <!--              {{ loggedInUser.trades }}-->
              <!--              {{card_names}}-->
              <span v-for="trade_id in loggedInUser.trades">
<!--                {{ // getCardName(trade_id) }}-->
                <!--                {{ this.cards }}-->
                {{ trade_id }}
              </span>
              <span v-for="card in trades_card_names">
<!--                {{ // getCardName(trade_id) }}-->
                <!--                {{ this.cards }}-->
                {{ card.id }} : {{ card.name }} <br>
              </span>

              <strong>Wants:</strong>
              {{ loggedInUser.wants }}
              <span v-for="card in wants_card_names">
<!--                {{ // getCardName(trade_id) }}-->
                <!--                {{ this.cards }}-->
                {{ card.id }} : {{ card.name }} <br>
              </span>
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
  },

  /*async asyncData({$axios, params}) {
    try {
      // = await axios.get("########")
      console.log(params);
      let trade_ids = this.loggedInUser.trades
      const {card_names} = await $axios.$get(`api/cards-ids/?ids=${trade_ids}`); // delete recipe
      // let card_names = await this.$axios.$get(`/api/cards/${card_id}/`); // delete recipe

      console.log(card_names);
      // let newRecipes = await this.$axios.$get("/api/cards/"); // get new list of recipes
      // this.recipes = card; // update list of recipes
      return card_names
    } catch (e) {
      console.log(e);
    }
  }*/
  // ,
  data() {
    return {
      cards: [],
      trades_card_names: [],
      wants_card_names: [],
    };
  },
  methods: {
    async getCardsById(card_id_list, list) {
      try {

        // let trade_ids = this.loggedInUser.trades
        let card_names = await this.$axios.$get(`api/cards-ids/?ids=${card_id_list}`); // delete recipe
        // let card_names = await this.$axios.$get(`/api/cards/${card_id}/`); // delete recipe

        card_names.forEach(card => {
          this[list].push({name: card.name, id: card.id});
        })
        console.log(card_names);
        // let newRecipes = await this.$axios.$get("/api/cards/"); // get new list of recipes
        // this.recipes = card; // update list of recipes
      } catch (e) {
        console.log(e);
      }
    }
  },
  mounted() {


    if (Array.isArray(this.loggedInUser.trades) && this.loggedInUser.trades.length) {
      this.getCardsById(this.loggedInUser.trades, 'trades_card_names');
    }
    if (Array.isArray(this.loggedInUser.want) && this.loggedInUser.wants.length) {
      this.getCardsById(this.loggedInUser.wants, 'wants_card_names');
    }
  }
}
</script>
