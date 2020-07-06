
<template lang="html">

  <div>


    <!--&lt;!&ndash;<p>Hi {{username}}!  Pick the track you want to play.</p>&ndash;&gt;-->

    <!--<br>-->
 <!--<br>-->
<div class="row p-3">

<div class="col-12">

    <div class="card">
    <div class="row">
        <div class="col-8">


          <div class="card-body">
            <h2 class="card-title">Welcome to PokerTrainer Tracks</h2>
            <p class="card-text py-2">This is a catalog of all the tracks we offer. Browse by topic, difficulty, and game type. Sign up today and get access to our entire library. PokerTrainer students get access to bonus content, competitions, and more.</p>
              <h5 class="card-subtitle">Ready to start winning?</h5>

                          <p class="card-text py-2">Sign up today and get access to our entire library. Treehouse students get access to workshops, bonus content, conferences, and more. Start with a free assessment which will determine at what level you should start.</p>

            <a href="#" class="btn btn-success" @click="test_three">Let's Go!</a>
          </div>
        </div>

        <div class="col-6">

        </div>

    </div>

</div>
</div>

</div>

  <br>


      <div class="row px-3">
  <template v-for="track_heading in track_headings">

    <div class="col-4 p-2">

    <tracks_cards
    :track_id = track_heading.id
    :heading =track_heading.track_title
    :description =track_heading.track_description
    :type =track_heading.track_type
    :header_background=track_heading.background_color
    >
    </tracks_cards>
 </div>

  </template>
          </div>

   </div>



</template>
<script>

import tracks_card from './tracks_card.vue';
import { mapState } from 'vuex'

export default {
  name: 'tracks',
  components: {'tracks_cards': tracks_card},
computed: mapState({
    track_headings: state => state.track_headings,
    username: state => state.player_data.username
        }),
mounted() {
     this.$store.dispatch('show_tracks_ajax', {})
  },

  methods: {
    test_one: function() {
      this.$store.dispatch('question_ajax')
    },
    test_two: function() {
      this.$store.dispatch('track_ajax', {track_id: 1})
    },
    test_three: function() {
      this.$store.dispatch('show_tracks_ajax', {})
    }
  }
}
</script>


<style scoped>
    .p_local {
        margin:0;padding:0;border:0;font-size:100%;font:inherit;vertical-align:baseline;
        font-size:14px;line-height:1.5;margin-bottom:15px;
    }

    .text_tracks {
        /*letter-spacing: 1px !important;*/
    }


</style>