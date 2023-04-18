<template>
    <div>
        <v-container fluid>
            <v-layout column>
                <v-flex xs12>
                    <h3 class="subject">User CURD</h3>
                </v-flex>
                
                <v-flex column>
                    <v-form ref="form" v-model="userList" lazy-validation>
                        <v-col cols="4" md="4">
                    <v-text-field v-model="data.username" :counter="15" label="Username" required></v-text-field>
                    </v-col>
                    <v-col cols="4" md="4">
                        <v-text-field v-model="data.age" label="Age" required></v-text-field>
                    </v-col>
                    <v-col cols="4" md="4">
                        <v-text-field v-model="data.city" :counter="15" label="City" required></v-text-field>
                    </v-col>    

                        <v-btn @click="sendForm" style="background: green">create</v-btn>
                        <v-btn @click="clearForm" style="background: red">clear</v-btn>
                    </v-form>
                </v-flex>

                <v-flex class="userList" column>
                    <v-card max-width="600" tile>
                        <v-list-item v-for="(data, index) in propsdata" v-bind:key="index">
                            <v-list-item-content>
                                <v-list-item-title>Name : {{data.username}}</v-list-item-title>
                                <v-list-item-subtitle>Age : {{data.age}}, Location: {{data.city}}</v-list-item-subtitle>
                            </v-list-item-content>
                             <!-- form which update data if is_hidden = true -->
                             <v-form v-show="data.is_hidden">
                                <v-container>
                                    <v-row>
                                        <v-col col="12" md="4">
                                            <v-text-field v-model="data.username" :counter="15" label="Username" required>
                                            </v-text-field>
                                        </v-col>
                                        <v-col cols="12" md="4">
                                            <v-text-field v-model="data.age" label="Age" disabled></v-text-field>
                                        </v-col>
                                        <v-col cols="12" md="4">
                                            <v-text-field v-model="data.city" label="City" required></v-text-field>
                                        </v-col>
                                        <v-col cols="12" md="4">
                                            <v-btn class="ma-2" @click="
                                            data.is_hidden = !data.is_hidden;
                                            updateUser(data);
                                            "
                                            v-show="data.is_hidden"
                                            color="#4CAF50"
                                            >Save</v-btn>
                                            <v-btn class="ma-2" @click="
                                            deleteUser(data);
                                            "
                                            color="#F443326"
                                            >Delete</v-btn>
                                        </v-col>
                                    </v-row>
                                </v-container>
                             </v-form>
                        </v-list-item>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
import axios from "axios";

let url = "http://localhost:8000/";


export default {
    data: () => {
        return {
            data: {
                username: "",
                age: "",
                city: "",
                xsrfCookieName: 'csrftoken', 
                xrfHeaderName: 'X-CSRFToken',
                withCredentials: true,
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
                // execute get if suceed
                this.$emit('saved');
            })
            .catch((error) => {
                console.log("Failed to get userList", error.reponse);
            });
        },
         
        clearForm: function() {
            (this.data.username=""), (this.data.age=""), (this.data.city= "");
        },

        deleteUser: function(id) {
            axios({
                method: "DELETE",
                url: url + id + "/",
            })
            .then((response) => {
                this.$emit("deleted");  // send deleted event to super componenet
                console.log("Success", response);
            })
            .catch((error) => {
                console.log("Failed to get userList", error.response);
            })
        },

        updateUser: function(data) {
            axios({
                method:"PATCH",
                url: url+data.id+"/",
                data: data,
            })
            .then((response) => {
                this.$emit("patched");
                console.log("Success", response);
            })
            .catch((error) => {
                console.log("Failed to patched userList", error.response);
            })
        },
        onlyUserListCard: function(data, propsdata) {
            for(var index in propsdata) {
                data.id != propsdata[index].id ? (propsdata[index].is_hiddent = false): "";
            }
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