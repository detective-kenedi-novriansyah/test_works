<template>
  <div class="hello">
    <h1>Hello There</h1>
    <div class="knd-newbie-button-group">
      <button class="knd-newbie-button" v-on:click="handleClickAdd()">
        Add
      </button>
      <button class="knd-newbie-button" v-on:click="handleClickOdd()">
        Odd
      </button>
    </div>
    <h1>{{value}}</h1>
    <div class="knd-newbie-grid">
    <div v-for="quest in question" :key="quest.id" class="knd-newbie-temp-grid">
      <div class="knd-newbie-card">
        <p>{{quest.quest}}</p>
        <button class="knd-newbie-button" v-on:click="handleClickRouter(quest.id)">Answer</button>
      </div>
    </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import { mapGetters } from 'vuex'
import { AxiosResponse } from 'axios'

@Component({
  computed: mapGetters(['value','question'])
})
export default class HelloWorld extends Vue {
  @Prop() private msg!: string;

  $router: any;

  handleClickAdd() {
    this.$store.dispatch("addPlus")
  }
  handleClickOdd() {
    this.$store.dispatch('addOdd')
  }
  handleClickRouter(newValue: number) {
    this.$store.dispatch('detailQuestion', newValue).then((res: AxiosResponse) => {
      this.$router.push({
        name: "answeers",
        params: {
          id: res.data.id
        }
      })
    })
  }
  mounted() {
    this.$store.dispatch("fetchQuestion");
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.knd-newbie-button-group {
  display: flex;
  align-items: center;
  justify-content: center;
  .knd-newbie-button {
    cursor: pointer;
    border: none;
    outline: none;
    width: 100px;
    height: 40px;
    background-color: white;
    box-shadow: 0 -2px 5px -2px rgba(0,0,0,0.75);
    margin-right: 0.20rem;
    &:last-child {
      margin-left: 0.20rem;
    }
  }
}
.knd-newbie-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  width: 100%;
  .knd-newbie-temp-grid {
    width: 40%;
    background-color: #42b983;
    color: white;
    padding: 1rem;
    box-shadow: 0 -2px 5px -2px rgba(0,0,0,0.75);
    margin: 0.40rem;
    padding: rem;
    border-radius: 10px;
    .knd-newbie-card {
      word-wrap: break-word;
      .knd-newbie-button {
        cursor: pointer;
        border: none;
        outline: none;
        width: 100px;
        border-radius: 10px;
        height: 40px;
        background-color: white;
        box-shadow: 0 -2px 5px -2px rgba(0,0,0,0.75);
      }
  }
  }
}
</style>
