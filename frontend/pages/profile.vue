<template>
  <v-main class="section">
    <v-container class="container">
      <v-row>
        <v-col cols="12 d-flex flex-column">
          <h1>Hey {{ loggedInUser.first_name }}</h1>
          <div class="content">
            <p>
              <strong>Email:</strong>
              {{ loggedInUser.email }}
            </p>
            <p>
              <strong>Bio:</strong>
              {{ loggedInUser.bio }}</p>
            <p>
              <strong>Trades:</strong> <br>
              <!--              {{ loggedInUser.trades }}-->
              <!--              {{card_names}}-->
              <span v-for="trade_id in loggedInUser.trades">
<!--                {{ // getCardName(trade_id) }}-->
                <!--                {{ this.cards }}-->
<!--                {{ trade_id }}-->
              </span>
              <span v-for="card in tradesCardNames">
<!--                {{ // getCardName(trade_id) }}-->
                <!--                {{ this.cards }}-->
                {{ card.id }} : {{ card.name }} <br>
              </span>
            </p>
            <p>
              <strong>Wants:</strong>
<!--              {{ loggedInUser.wants }}-->
              <span v-for="card in wantsCardNames">
<!--                {{ // getCardName(trade_id) }}-->
                <!--                {{ this.cards }}-->
                {{ card.id }} : {{ card.name }} <br>
              </span>
            </p>  <p>
              <strong>Shops:</strong>
              {{ loggedInUser.mtg_shops }}
              <span v-for="card in wantsCardNames">
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
      tradesCardNames: [],
      wantsCardNames: [],
      shopList: []
    };
  },
  methods: {
    async getCardsById(card_id_list, list) {
      try {

        // let trade_ids = this.loggedInUser.trades
        let card_details = await this.$axios.$get(`api/cards-ids/?ids=${card_id_list}`); // delete recipe
        // let card_names = await this.$axios.$get(`/api/cards/${card_id}/`); // delete recipe

        card_details.forEach(card => {
          this[list].push({name: card.name, id: card.id});
        })
        console.log(card_details);
        // let newRecipes = await this.$axios.$get("/api/cards/"); // get new list of recipes
        // this.recipes = card; // update list of recipes
      } catch (e) {
        console.log(e);
      }
    }, async getShopsById(shop_list_id) {
      try {

        // let trade_ids = this.loggedInUser.trades
        let shop_details = await this.$axios.$get(`api/cards-ids/?ids=${shop_list_id}`); // delete recipe
        // let card_names = await this.$axios.$get(`/api/cards/${card_id}/`); // delete recipe

        shop_details.forEach(card => {
          this.shopList.push({name: card.name, id: card.id});
        })

        console.log(shop_details);
        // let newRecipes = await this.$axios.$get("/api/cards/"); // get new list of recipes
        // this.recipes = card; // update list of recipes
      } catch (e) {
        console.log(e);
      }
    }
  },
  mounted() {
    if (Array.isArray(this.loggedInUser.trades) && this.loggedInUser.trades.length) {
      this.getCardsById(this.loggedInUser.trades, 'tradesCardNames');
    }
    if (Array.isArray(this.loggedInUser.wants) && this.loggedInUser.wants.length) {
      this.getCardsById(this.loggedInUser.wants, 'wantsCardNames');
    }
  }
}
</script>
