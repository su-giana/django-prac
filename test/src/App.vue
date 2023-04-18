

<template>
    <div>
        <HeaderVue></HeaderVue>
        <ContentVue v-bind:propsdata="userList" v-on:saved="getUserList" v-on:deleted="getUserList" v-on:patched="getUserList"></ContentVue>
        <!-- v-bind:propsdata="what we want to put" -->
        <!-- get save event through v-on -->
        <FooterVue></FooterVue>
    </div>
</template>

<script>
import HeaderVue from "./components/HeaderVue.vue";
import ContentVue from "./components/ContentVue.vue";
import FooterVue from "./components/FooterVue.vue";
import axios from "axios";

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

let url = "http://127.0.0.1:8000";


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
    axios({     // get userList from DRF server and store it
        method: "GET",
        url: url
    })
    .then(response => {
        for(var index in response.data){
            response.data[index].is_hidden = false; // add is_hidden = false to data from backend
        }
        this.userList=response.data;
        console.log("Success", response);
    })
    .catch(error => {
        console.log("Failed to get userList", error.response);
    });

    axios({
        method: "GET",
        url: url
    })
    .then(response =>{
        this.userList = response.data;
    })
    .catch(response => {
        console.log("Failed", response);
    });
  },

    methods: {
        getUserList: function() {
            axios({
                method: "GET",
                url: url,
            })
            .then((response) => {
                for(var index in response.data){
                    response.data[index].is_hidden = false; // add is_hidden = false to data from backend
                }
                this.userList = response.data;
                console.log("Success", response.data);
            })
            .catch((error) => {
                console.log("Failed to get userList", error.response)
            });
        },
        updateUserList: function() {},
        deleteUserList: function() {}
    }
};
</script>
