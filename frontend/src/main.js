import Vue from 'vue';
import App from './App.vue';
import router from './router/router';
import store from './store/store';


Vue.component('navbar', require('./components/navbar/navbar.vue').default);

Vue.config.productionTip = true;

const vue = new Vue({
  router,
  store,
  render: h => h(App)
})

vue.$mount('#app')
