
<template>

  <div class="card h-100">
<div class="card-header card-header-text" v-bind:style="{ backgroundColor: header_background}">

{{type}}
  </div>

  <div class="card-body">
    <h4 class="card-title">{{heading}}</h4>
    <p class="card-text">{{description}}</p>
      <router-link to="/track_details">
    <a @click="test_two" class="btn btn-secondary text-white">Let's Play!</a>
      </router-link>
  </div>
</div>


</template>
<script>



export default {
  name: 'tracks_card',
  props: ['track_id', 'heading', 'description', 'type', 'header_background'],
      data () {
        return {
        test_mode: false,
        test_mode_redirect_id: 1
    }
    },
    mounted () {
            if (this.test_mode) {
                if (this.track_id == this.test_mode_redirect_id) {
                    this.test_two()
                    this.$router.push({ path:'/track_details' });
                }
            }
    },
  methods: {
//    test_one: function() {
//      this.$store.dispatch('question_ajax')
//    },
    test_two: function() {
      console.log(this.track_id)
      this.$store.dispatch('track_ajax', {track_id: this.track_id, heading: this.heading, description: this.description})
    }
//    test_three: function() {
//      this.$store.dispatch('show_tracks_ajax', {})
//    }
  }
}
</script>

<style scoped>

  .card-header-text {
    color: white;
  }

</style>