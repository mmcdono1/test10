import Vue from 'vue';
import VueRouter from 'vue-router';

import tracks from '../components/tracks/tracks.vue';
import track_details from '../components/tracks/track_details.vue';

Vue.use(VueRouter);

const routes = [

  { path: '/', component: tracks },
  { path: '/track_details', component: track_details },

  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
];

const router = new VueRouter({
  routes,
});

export default router;
