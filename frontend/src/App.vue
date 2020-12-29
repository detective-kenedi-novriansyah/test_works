<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <form v-on:submit.prevent="Submit()" v-if="!token">
      <input v-model="first_name" type="text" name="first_name" id="first_name" placeholder="First Name">
      <input v-model="last_name" type="text" name="last_name" id="first_name" placeholder="Last Name">
      <button class="knd-newbie-button">Daftar</button>
    </form>
    <router-view/>
  </div>
</template>

<script lang="ts">
import axios, { AxiosResponse } from 'axios';
import { Component, Provide, Vue } from 'vue-property-decorator'
@Component({})
export default class App extends Vue {
  @Provide() token: String = localStorage.getItem("token")
  @Provide() first_name: String = "";
  @Provide() last_name: String = "";
  Submit() {
    const data = {
      first_name: this.first_name,
      last_name: this.last_name,
    }
    this.$store.dispatch('register', data).then((res: AxiosResponse<any>) => {
      localStorage.setItem("token", res.data.message)
      window.location.reload()
    })
  }
  mounted() {
    if(localStorage.getItem('token')) {
    axios.get('http://localhost:8000/api/v1/question/question/question/question/point/', {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      }
    }).then((res: AxiosResponse<any>) => {
        this.$store.commit("POINT_QUESTION", res.data)
    })
    }
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

input {
  border: none;
  outline: none;
  box-shadow: 0 -2px 5px -2px rgba(0,0,0,0.75);
  padding: 0.80rem;
  width: 200px;
}

form {
  .knd-newbie-button {
    margin: 0.40rem;
    cursor: pointer;
    padding-left: 1rem;
    padding-right: 1rem;
    margin-right: 1rem;
    margin-left: 1rem;
    border: none;
    outline: none;
    border-radius: 10px;
    height: 40px;
    background-color: white;
    box-shadow: 0 -2px 5px -2px rgba(0,0,0,0.75);
}
}
</style>
