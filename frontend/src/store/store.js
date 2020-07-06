import Vue from 'vue';
import Vuex from 'vuex';

import axios from 'axios';
import Router from '../router/router';


Vue.use(Vuex);

export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
     // *** Ajax query to update tracks data *** //
    show_tracks_ajax: (context, track_id)  => {
      axios({
        method: 'POST', url: '/tracks/all/',
        headers: {
          'X-CSRFToken': CSRF_TOKEN,
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
        data: {
          session_id: context.state.player_data.session_id,
          track_id
        }
       })
        .then(response => {
        console.log(response);
        context.commit('mutate_track_headings', response.data);
      })
        .catch(error => {
        throw("Error: ", error);
      });
    },


  },
  modules: {
  },
});
