<template>
    <div>
        <v-container fluid>
            <v-layout column>
                <v-flex xs12>
                    <h3 class="subject">User CURD</h3>
                </v-flex>
                <v-col cols="4" md="4">
                    <v-text-field v-model="username" :counter="15" label="Username" required></v-text-field>
                </v-col>
                <v-col cols="4" md="4">
                    <v-text-field v-model="age" label="Age" required></v-text-field>
                </v-col>
                 <v-col cols="4" md="4">
                    <v-text-field v-model="city" :counter="15" label="City" required></v-text-field>
                </v-col>
                <v-flex column>
                    <v-form ref="form" v-model="model" lazy-validation>
                        <v-text-field v-model="title" :counter="64" label="Title" required></v-text-field>
                        <v-text-field v-model="content" :counter="255" label="Content" required></v-text-field>

                        <v-btn @click="create" style="background: green">create</v-btn>
                        <v-btn @click="clear" style="background: red">clear</v-btn>
                    </v-form>
                </v-flex>

                <v-flex class="userList" column>
                    <v-card max-width="600" tile>
                        <v-list-item v-for="(data, index) in propsdata" v-bind:key="index">
                            <v-list-item-content>
                                <v-list-item-title>Name : {{data.username}}</v-list-item-title>
                                <v-list-item-subtitle>Age : {{data.age}}, Location: {{data.city}}</v-list-item-subtitle>
                            </v-list-item-content>
                        </v-list-item>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
import axios from "axios";
let url = "http://localhost:8000";

export default {
    data: () => {
        return {
            data: {
                username: "",
                age: "",
                city: "",
            },
        };
    },

    props: ["propsdata"],

    methods: {
        sendForm: function(){
            axios({
                method: "POST",
                url: url,
                data: this.data,
            })
            .then((response) => {
                this.userList = response.data;
            })
            .catch((error) => {
                console.log("Failed to get userList", error.reponse);
            });
        },
        clearForm: function() {
            (this.data.username=""), (this.data.age=""), (this.data.city= "");
        },
    },
};
</script>

<style>
    .subject {
        color:blue;
        font-style:oblique;
        padding:30px;
        text-align: center;
    }

    .userList{
        margin: 30px 0px 30px 0px
    }
</style>