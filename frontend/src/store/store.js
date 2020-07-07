import Vue from 'vue';
import Vuex from 'vuex';

import axios from 'axios';
import Router from '../router/router';


Vue.use(Vuex);

export default new Vuex.Store({
  state: {
        player_data: {player_id: '', session_id: '', username: ''},
        track_headings: [],

  },
  mutations: {
        mutate_track_headings: function(state, payload) {
      state.track_headings = payload.track_headings
      state.player_data.username = payload.username
                },

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
          // session_id: context.state.player_data.session_id,
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
