<template lang="html">

  <div>

    <nav class="navbar navbar-expand-lg bg-dark"  style="background-color: #3E474F;">

        <div class="container">

        <a class="navbar-brand nav-text pr-3" href="#">PokerTrainer</a>

        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">

      <ul class="navbar-nav mr-auto">

       <li class="nav-item header-nav-item px-3">
         <router-link to="/">
           <div class="navbar-brand nav-text" to="/">Tracks</div>
         </router-link>
      </li>

             <li class="nav-item header-nav-item px-3">
         <router-link to="/track_details">
           <div class="navbar-brand nav-text" to="/track_details">Tracks Details</div>
         </router-link>
      </li>

             <li class="nav-item header-nav-item px-3">
         <router-link to="/table_and_answer">
           <div class="navbar-brand nav-text" to="/table_and_answer">Table</div>
         </router-link>
      </li>

    </ul>

  </div>

            </div>

</nav>

</div>
</template>
<script>



export default {
  name: 'navbar2',
  mounted () {
    this.$router.push({ path: '/' });
  }
//    route: {
//    activate: function () {
//      console.log('hook-example activated!')
//    }},
}
</script>


<style scoped>

/*.header-nav-list {*/
    /*list-style: none;*/
    /*position: relative;*/
    /*width: 100%;*/
    /*margin: 0 auto;*/
    /*font-size: 14px;*/
/*}*/


/*! CSS Used from: https://static.teamtreehouse.com/assets/application-01a6e6e237f0dd04b55e18649ab0fc2fe14f4a7b79a6ec9ddf8ffafccbb80afc.css ; media=screen */

/*a{color:#3f8abf;cursor:pointer;transition:color 300ms 0s ease;}*/
/*a:hover{color:#326e99;}*/
/*a{cursor:pointer;text-decoration:none;}*/
.nav-text{
    display:block;
    color:#b2bbbd;
}
.header-nav-item:before,.nav-text:after{content:" ";display:table;}
.header-nav-item:after{clear:both;}
.header-nav-item:focus{color:#fff!important;}
.header-nav-item:hover .nav-text{color:#fff;}

    /*a:hover, a:visited { color:#37404e !important; }*/


</style>
