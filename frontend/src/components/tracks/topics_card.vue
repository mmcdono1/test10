
<template lang="html">

  <div>

<div class="card" style="width: 20rem;">

  <div class="card-body">
    <h4 class="card-title">{{topic_name}}</h4>
  </div>
      <ul class="list-group list-group-flush">
    <li class="list-group-item">topic score: {{topic_score}}</li>
    <li class="list-group-item">topic entries: {{topic_entries}}</li>
  </ul>
    <div class="card-body">

       <router-link to="/track_details">
          <button class="btn btn-secondary text-white" @click="add_topic">Add</button>
          </router-link>
</div>



    </div>

   </div>

</template>
<script>
export default {
  name: 'topics_card',
  props: ['topic_name','topic_id','topic_score', 'topic_entries', 'betting_round', 'betting_round_id', 'play_order', 'allowed_positions'],
   data () {
        return {
        newtodo: '',
		todos: [],
        test_mode: true,
        test_mode_redirect_id: [1]
        }},
    mounted() {
            if (this.test_mode) {
                if (this.test_mode_redirect_id.includes(this.topic_id)) {
                    this.add_topic()
                }
            }
     this.$store.dispatch('show_tracks_ajax', {})
  },
  methods: {
    test_two: function() {
      console.log(this.track_id)
      this.$store.dispatch('track_ajax', {track_id: this.track_id, heading: this.heading, description: this.description})
    },
    add_topic: function() {
        console.log(this.topic_name);
        this.$store.dispatch('update_active_topics', {topic_id: this.topic_id, topic_name: this.topic_name,
            topic_score: this.topic_score, betting_round_id: this.betting_round_id, play_order: this.play_order,
            entries: this.topic_entries, allowed_positions: this.allowed_positions})
    }
	}
}
</script>
