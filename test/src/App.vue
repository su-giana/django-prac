import HeaderVue from "./components/HeaderVue.vue";
import ContentVue from "./components/ContentVue.vue";
import FooterVue from "./components/FooterVue.vue";
import axios from "axios";

<template>
    <div>
        <HeaderVue></HeaderVue>
        <ContentVue v-bind:propsdata="userList"></ContentVue>
        <FooterVue></FooterVue>
    </div>
</template>

<script>
export default {
    data: () => {
        return {
            userList: []
        };
    },

    components: {
    HeaderVue,
    ContentVue,
    FooterVue,
  },

  mounted(){
    axios({
        method: "GET",
        url: url
    })
        .then(respones =>{
            this.userList = response.data;
        })
        .catch(response => {
            console.log("Failed", response);
        });
  },

    methods: {
        getUserList: function() {},
        updateUserList: function() {},
        deleteUserList: function() {}
    }
};
</script>
