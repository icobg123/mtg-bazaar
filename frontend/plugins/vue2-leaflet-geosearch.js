import Vue from 'vue';
import * as Vue2Leaflet from 'vue2-leaflet'
import L from 'vue2-leaflet';
import {OpenStreetMapProvider} from 'leaflet-geosearch';
import VGeosearch from 'vue2-leaflet-geosearch';

// Vue.use(VGeosearch)
//
// Vue.component('v-map', Vue2Leaflet.Map);
// Vue.component('v-tilelayer', Vue2Leaflet.TileLayer);
Vue.component('v-geosearch', VGeosearch)
//
export default {
  components: {VGeosearch},
  data() {
    return {
      geosearchOptions: { // Important part Here
        provider: new OpenStreetMapProvider(),
      },
    };
  },
};
