<template>
  <div class="flex flex-row h-screen justify-center items-center">
    <img src="./../assets/web2.jpg" class="background w-screen h-screen absolute opacity-40" />
    <LPGenForm class="mx-5" @change-form="setNewValues" />
    <LPForm class="mx-5" @solve="sendToSolve" :lpModel="lpModel" />
  </div>
</template>

<script>
// import * as linearProgram from "./linearProgram";
const backendURL = "/api";


export default {
  name: "LP",
  created() {
    // solver = linearProgram.SolverType.GLOP;
    // lp = linearProgram.LinearProgramm(
    // )

  },
  data() {
    return {
      lpModel: {
        nrVars: 1,
        nrCons: 1,
      }
    };
  },
  methods: {

    setNewValues(e) {
      this.lpModel.nrVars = e.variables
      this.lpModel.nrCons = e.constraints
    },
    async getModel() {
      fetch(backendURL).then(r => r.json()).then(data => console.log('data', data))
        .catch(e => {
          console.error('Error:', e);
        })
    },
    async postModel() {
      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        }
      };
      await fetch(backendURL, requestOptions).then(data => console.log('data', data))
        .catch(e => {
          console.error('Error:', e);
        })
    },
    sendToSolve() {
      console.log('get model')
      this.getModel()
    },
  }

};
</script>