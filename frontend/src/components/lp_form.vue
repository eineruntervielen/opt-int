<template>
  <Card>
    <div v-if="lpModel.nrVars > 0">
      <h1>Decision Variables</h1>
      <p>Number of decision variables: {{ lpModel.nrVars }}</p>
      <ul v-for="i in lpModel.nrVars" :key="i">
        <div>
          <span class="m-1">Nr. {{ i }}</span>
          <label class="m-1" v>Name:</label>
          <input class="m-1" >
        </div>
      </ul>
    </div>
    <div v-if="lpModel.nrCons > 0">
      <h1>Constraints</h1>
      <p>Number of constraints: {{ lpModel.nrCons }}</p>
      <ul v-for="i in lpModel.nrCons" :key="i">
        <span class="m-1">Nr. {{ i }}</span>
        <input class="m-1"> <input class="m-1"> <input class="m-1"> </ul>
    </div>
    <button @click="solve"
      class=" shadow mx-auto border bg-slate-100 hover:bg-slate-200 rounded full text-gray-700 px-4 hover:scale-110 transition ">
      Solve
    </button>
  </Card>

</template>

<script>
export default {
  name: "LPForm",
  props: {
    lpModel: Object
  },
  methods: {
    solve() {
      this.$emit('solve')
    }
  }
};
</script>