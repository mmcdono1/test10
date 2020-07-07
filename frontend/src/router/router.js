import Vue from 'vue';
import VueRouter from 'vue-router';

import tracks from '../components/tracks/tracks.vue';
import track_details from '../components/tracks/track_details.vue';

Vue.use(VueRouter);

const routes = [

  { path: '/', component: tracks },
  { path: '/track_details', component: track_details },


];

const router = new VueRouter({
  routes,
});

export default router;
