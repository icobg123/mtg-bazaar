<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="12" md="12">

      <!-- <div class="text-center">
         <logo />
         <vuetify-logo />
       </div>
       <v-card>
         <v-card-title class="headline">
           Welcome to the Vuetify + Nuxt.js template
         </v-card-title>
         <v-card-text>
           <p>
             Vuetify is a progressive Material Design component framework for
             Vue.js. It was designed to empower developers to create amazing
             applications.
           </p>
           <p>
             For more information on Vuetify, check out the
             <a
               href="https://vuetifyjs.com"
               target="_blank"
               rel="noopener noreferrer"
             >
               documentation </a
             >.
           </p>
           <p>
             If you have questions, please join the official
             <a
               href="https://chat.vuetifyjs.com/"
               target="_blank"
               rel="noopener noreferrer"
               title="chat"
             >
               discord </a
             >.
           </p>
           <p>
             Find a bug? Report it on the github
             <a
               href="https://github.com/vuetifyjs/vuetify/issues"
               target="_blank"
               rel="noopener noreferrer"
               title="contribute"
             >
               issue board </a
             >.
           </p>
           <p>
             Thank you for developing with Vuetify and I look forward to bringing
             more exciting features in the future.
           </p>
           <div class="text-xs-right">
             <em><small>&mdash; John Leider</small></em>
           </div>
           <hr class="my-3" />
           <a
             href="https://nuxtjs.org/"
             target="_blank"
             rel="noopener noreferrer"
           >
             Nuxt Documentation
           </a>
           <br />
           <a
             href="https://github.com/nuxt/nuxt.js"
             target="_blank"
             rel="noopener noreferrer"
           >
             Nuxt GitHub
           </a>
         </v-card-text>
         <v-card-actions>
           <v-spacer />
           <v-btn color="primary" nuxt to="/inspire"> Continue </v-btn>
         </v-card-actions>
       </v-card>-->
      <v-autocomplete
        v-model="select"
        :loading="loading"
        :items="locations"
        :search-input.sync="search"
        cache-items
        class="mx-4"
        flat
        hide-no-data
        hide-details
        label="In which city do you play magic?"
        solo-inverted
        dense
        clearable
        @change="getShops"
      ></v-autocomplete>
      <div v-model="location_x">{{ location_x }}</div>
      <div v-model="location_y">{{ location_y }}</div>
      <!--      <div v-model="shops">{{ shops }}</div>-->
      <!--      <v-form @submit.prevent="">-->
      <!--            <div class="form-group">-->
      <!--              <label for>Recipe Name</label>-->

      <!-- <v-autocomplete
         :items="cities"
         dense
         clearable
         solo
         filled
         label="Filled"
         @change="getCoords"
       ></v-autocomplete>-->


      <!--        <v-text-field label="City" type="text" v-model="city"></v-text-field>-->
      <!--        <v-btn type="submit" class="btn btn-primary">Submit</v-btn>-->
      <!---->
      <!--      </v-form>-->
      <div id="map-wrap" style="height: 100vh">
        <client-only>
          <l-map :zoom="zoom" :center="map_center" ref="map">
            <l-tile-layer url='https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png'></l-tile-layer>
            <!--            <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>-->
            <!-- IMPORTANT PART HERE -->
            <v-geosearch :options="geosearchOptions"></v-geosearch>
            <!-- /IMPORTANT PART HERE -->
            <span v-if="markers" v-for="marker in markers">
              <l-marker :lat-lng="[marker.latitude,marker.longitude]">
                <l-tooltip>
                  <span class="d-flex flex-column">
                    <span>{{ marker.name }}</span>
<!--                  <span>{{ marker.email }}</span>-->
                  <span>{{ marker.postalAddress }}</span>
                  <span>{{ marker.phoneNumber }}</span>
                  <span>{{ marker.emailAddress }}</span>
                    </span>
                </l-tooltip>
              </l-marker>
            </span>
            <!--            <l-marker :lat-lng="map_center"></l-marker>-->
          </l-map>
        </client-only>
      </div>
    </v-col>
  </v-row>
</template>

<script>
import Logo from '~/components/Logo.vue'
import VuetifyLogo from '~/components/VuetifyLogo.vue'
// import {OpenStreetMapProvider} from 'leaflet-geosearch';

export default {
  components: {
    Logo,
    VuetifyLogo,
  },
  data() {
    return {
      loading: false,
      locations: [],
      search: null,
      select: null,
      //
      zoom: 13,
      map_center: [42.6978634, 23.3221789],
      markers: [],
      location_x: 0,
      location_y: 0,
      shops: [],
      cities: [''],
      geosearchOptions: { // Important part Here
        provider: '',

        showMarker: false, // optional: true|false  - default true
        // showPopup: false, // optional: true|false  - default false
        // marker: {
        //   // optional: L.Marker    - default L.Icon.Default
        //   icon: new L.Icon.Default(),
        //   draggable: false,
        // },
        // popupFormat: ({query, result}) => result.label, // optional: function    - default returns result label,
        // resultFormat: ({result}) => result.label, // optional: function    - default returns result label
        // maxMarkers: 1, // optional: number      - default 1
        // retainZoomLevel: false, // optional: true|false  - default false
        // animateZoom: true, // optional: true|false  - default true
        // autoClose: false, // optional: true|false  - default false
        // searchLabel: 'Enter address', // optional: string      - default 'Enter address'
        // keepResult: false, // optional: true|false  - default false
        // updateMap: true, // optional: true|false  - default true
      },
    };
  }
  ,
  watch: {
    search(val) {
      console.log(val);
      val && val !== this.select && this.getCoords(val)
      // val && val !== this.select && this.querySelections(val)
    },
  },
  methods: {
    querySelections(v) {
      this.loading = true
      // Simulated ajax query
      setTimeout(() => {
        this.locations = this.states.filter(e => {
          return (e || '').toLowerCase().indexOf((v || '').toLowerCase()) > -1
        })
        this.loading = false
      }, 500)
    },
    async getCoords(input) {


      console.log(input)
      if (process.browser) {
        this.loading = true

        let city;
        if (input !== null) {
          city = input;
        } else {
          city = "New York";
        }
        // if (this.city !== null) {
        //   city = this.city;
        // } else {
        //   city = "New York";
        // }

        console.log('in : ' + city)
        const lgeo = require('leaflet-geosearch')
        let provider = new lgeo.OpenStreetMapProvider;
        // let icara = new lgeo.AlgoliaProvider();

        try {
          let results = await provider.search({query: city});
          console.log(results);
          // this.$router.push("/recipes/");
          let cities = []
          results.forEach(result => {
            cities.push(result.label)
          })

          console.log(results[0].x);
          this.locations = cities;
          this.location_x = results[0]['x'];
          this.location_y = results[0]['y'];

          this.loading = false;


        } catch (e) {
          console.log(e);
        }

        /* try {
           fetch(`https://api.tabletop.wizards.com/ogre-battledriver/Organizations/by-location?lat=42.6978634&lng=23.3221789&maxMeters=25000&pageSize=10000&isPremium=false`)
             // fetch(`https://api.tabletop.wizards.com/ogre-battledriver/Organizations/by-location?lat=${this.location_x}&lng=${this.location_y}&maxMeters=50000&pageSize=10000&isPremium=false`)
             .then(response => response.json())
             .then(data => console.log(data));

           // let response = await this.$axios.$get(`https://api.tabletop.wizards.com/ogre-battledriver/Organizations/by-location?lat=${this.location_x}&lng=${this.location_y}&maxMeters=25000&pageSize=10000&isPremium=false`);
           // let response = await this.$axios.$get(`https://api.tabletop.wizards.com/ogre-battledriver/Organizations/by-location?lat=${this.location_x}&lng=${this.location_y}&maxMeters=25000&pageSize=10000&isPremium=false`);
           // let response = await this.$axios.$get(`/api/recipes/${editedRecipe.id}/`, formData, config);


           // console.log(response);
           // this.$router.push("/recipes/");
           // this.shops = response

         } catch (e) {
           console.log(e);
         }*/

        // let geosearchOptions = {
        //   provider: icara,
        //   style: 'button',
        //   showMarker: true, // optional: true|false  - default true
        //   autoClose: true, // optional: true|false  - default false
        //
        // }
        // console.log(geosearchOptions)
        // this.geosearchOptions = geosearchOptions;
        // return geosearchOptions;
      }

    },
    async getShops() {
      // async getShops(x, y) {
      // if (process.browser) {
      let x = this.location_x;
      let y = this.location_y;

      this.map_center = [y, x]


      console.log(x);
      console.log(y);

      try {
        // let response = fetch(`https://api.tabletop.wizards.com/ogre-battledriver/Organizations/by-location?lat=42.6978634&lng=23.3221789&maxMeters=25000&pageSize=10000&isPremium=false`)
        /*fetch(`https://api.tabletop.wizards.com/ogre-battledriver/Organizations/by-location?lat=${x}&lng=${y}&maxMeters=50000&pageSize=10000&isPremium=false`).then((response) => {
          return response.json();
        }).then((data) => {
          console.log(data);
        });*/
        let shop_data;

        fetch(`https://api.tabletop.wizards.com/ogre-battledriver/Organizations/by-location?lat=${y}&lng=${x}&maxMeters=25000&pageSize=10000&isPremium=false`).then((response) => {
        // fetch(`https://api.tabletop.wizards.com/ogre-battledriver/Organizations/by-location?lat=${y}&lng=${x}&maxMeters=10000&pageSize=10000&isPremium=false`).then((response) => {
          console.log(response);
          response.json().then((data) => {
            shop_data = data.results;

            console.log(shop_data);
            this.markers = shop_data;
            //

            if (Array.isArray(this.markers) && this.markers.length) {
              this.$refs.map.mapObject.fitBounds(this.markers.map(m => {
                return [m.latitude, m.longitude]
              }))
            }


            console.log(shop_data);
          });
        });

        // let response = fetch(`https://api.tabletop.wizards.com/ogre-battledriver/Organizations/by-location?lat=${x}&lng=${y}&maxMeters=50000&pageSize=10000&isPremium=false`)
        //   .then(response => response.json())
        //   .then(data => console.log(data));
        // let response = await this.$axios.$get(`https://api.tabletop.wizards.com/ogre-battledriver/Organizations/by-location?lat=${x}&lng=${y}&maxMeters=25000&pageSize=10000&isPremium=false`);
        // let response = await this.$axios.$get(`/api/recipes/${editedRecipe.id}/`, formData, config);


        // console.log(response);
        // this.$router.push("/recipes/");
        // this.shops = response

      } catch (e) {
        console.log(e);
      }
      // }
    },
  },
  mounted() {
    // import {OpenStreetMapProvider} from 'leaflet-geosearch';
    console.log('icara')
    //check if window is loaded then import the lib and assign the new provider
    if (process.browser) {
      console.log('in')
      const lgeo = require('leaflet-geosearch')
      let icara = new lgeo.OpenStreetMapProvider;
      // let icara = new lgeo.AlgoliaProvider();
      let geosearchOptions = {
        provider: icara,
        style: 'bar',
        showMarker: true, // optional: true|false  - default true
        autoClose: true, // optional: true|false  - default false
        animateZoom: true,

      }
      console.log(geosearchOptions)
      this.geosearchOptions = geosearchOptions;
      // return geosearchOptions;
    }
  }
  ,


}
</script>
<style>
.geosearch .results {
  color: black;
}

.v-autocomplete__content.v-menu__content {
  z-index: 400 !important;
}
</style>



