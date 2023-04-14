<template>
  <div>
    <HeaderVue />
    <ContentVue />
    <FooterVue />
  </div>
</template>

<script>
import HeaderVue from "./components/HeaderVue.vue";
import ContentVue from "./components/ContentVue.vue";
import FooterVue from "./components/FooterVue.vue";

export default {
  components: {
    HeaderVue,
    ContentVue,
    FooterVue,
  },

  data: function(){
    return {
      name: "leffept",
    };
  },

  
};
</script>

<style>

</style>