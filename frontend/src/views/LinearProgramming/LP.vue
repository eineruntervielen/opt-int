<template>
  <div class="flex flex-row h-screen justify-center items-center">
    <LPGenForm class="mx-5" @change-form="setNewValues" />
    <LPForm class="mx-5" @solve="sendToSolve" :lpModel="lpModel" />
    <Transition>
      <Card v-if="view.show">Your Result is: 5</Card>
    </Transition>
  </div>
</template>

<script>
// import * as linearProgram from "./linearProgram";
const backendURL = "/api";
export default {

  name: "LP",
  data() {
    return {
      view: {
        show: false
      },
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
      console.log('calling backend solver');
      this.getModel();
      this.view.show = true;
    },
  }

};
</script>

<style>
/* we will explain what these classes do next! */
.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>