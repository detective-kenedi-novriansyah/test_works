import Vue from 'vue';
import Vuex from 'vuex';
import valueModules from './valueModules'
import questionModules from './questionModules'

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    valueModules,
    questionModules,
  }
});
