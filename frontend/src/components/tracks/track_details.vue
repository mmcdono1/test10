
<template lang="html">

  <div>
  <br>
<!--hello test-->
<div class="row p-3">

<div class="col-12">

    <div class="card">
    <div class="row">
        <div class="col-8">


          <div class="card-body">
            <h2 class="card-title">Welcome to {{active_track.heading}}</h2>
            <p class="card-text py-2">{{active_track.description}}</p>

              <h5 class="card-subtitle">Ready to start winning? Hello</h5>

              <p class="card-text py-2">Sign up today and get access to our entire library. Treehouse students get access to workshops, bonus content, conferences, and more. Start with a free assessment which will determine at what level you should start.</p>

              <template v-if="quiz_by_tracks.track_quiz_taken_check == false">
               <p class="card-text py-2">Before we start on the track {{active_track.heading}} lets have a look at your skill level.  This will serve as a baseline to see how your training is progressign and will allow training to focus on your weak points.  As you progress through traniing you will constantly be reeevaluated to check where we are at and what we should be concentrating on to bring our game to the next level.</p>

              </template>

           <button class="btn btn-success" v-on:click="addAll">Add all topics</button>

        <router-link to="/table_and_answer">
        <button class="btn btn-success" v-on:click="start_session(1)">Let's Do Training</button>
         </router-link>

        <router-link to="/table_and_answer">
        <button class="btn btn-success" v-on:click="start_session(2)">Let's Do Evaluation</button>
        </router-link>
          </div>
        </div>

        <div class="col-6">

        </div>

    </div>

</div>
</div>

</div>

<div>

	<ul>
		<li v-for="(active_topic_names, index) in active_topics.topic_names">
			{{active_topic_names}}
			<button v-on:click="rmTodo(index)">&Chi;</button>
		</li>
	</ul>
</div>

<br>
<div class="row">
  <template v-for="core_topic in core_topics">

      <div class="col-4 p-1">

    <topics_cards
    :topic_id = core_topic.core_topic_id
    :topic_name = core_topic.core_topic_name
    :topic_score = core_topic.score
    :topic_entries = core_topic.entries
    :betting_round = core_topic.betting_rounds
    :betting_round_id = core_topic.betting_round_id
    :play_order = core_topic.play_order
    :allowed_positions = core_topic.allowed_positions
    >
    </topics_cards>

          </div>

    </template>

    </div>
</div>
</template>
<script>

import { mapState } from 'vuex'
import topics_card from './topics_card.vue';

export default {
  name: 'track_details',
   data () {
        return {
        newtodo: '',
		todos: []
        }},
  components: {'topics_cards': topics_card},
  computed: mapState({
    active_track: state => state.active_track,
    core_topics: state => state.core_topics,
    active_topics: state => state.active_topics,
    quiz_by_tracks: state => state.quiz_by_tracks
  }),
  methods: {
  	start_session: function (mode_id) {
  	    if (mode_id == 2) {
  	     this.addAll()
        }
        this.$store.dispatch('start_new_round', {'mode_id': mode_id})

	},
    addTodo: function () {
      if (this.newtodo) {
        this.todos.push({
          text: this.newtodo
        });
      }
      this.newtodo = '';
    },
    rmTodo: function (index) {
      this.todos.splice(index, 1);
    },
      addAll: function() {
        this.todos = []
        for (var i = 0; i < this.core_topics.length; i++) {
        this.$store.dispatch('update_active_topics', {topic_id: this.core_topics[i].core_topic_id, topic_name: this.core_topics[i].core_topic_name,
            topic_score: this.core_topics[i].score, betting_round_id: this.core_topics[i].betting_round_id, play_order: this.core_topics[i].play_order,
            entries: this.core_topics[i].entries, allowed_positions: this.core_topics[i].allowed_positions})
        }
      }
  }
}
</script>
