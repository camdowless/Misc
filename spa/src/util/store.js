import { createStore } from "vuex";
import * as request from "./request";


const state = {
    classification: 'none'
}

const actions = {
    async Digit(canvas){
      let options = {
        method: "GET",
        data: {
            canvas
        }
      }
      await request.classifyDigit(options, (payload) => {
        commit('setClassification', payload)
      })
    },  
}

const mutations = {
    setClassification(state, payload){
        state.classification = payload
    }
}

export default createStore({
    state,
    actions,
    mutations
  });