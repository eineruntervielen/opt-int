<template>
  <Card>
    <div v-if="lpModel.nrVars > 0">
      <h1 class="my-2 text-xl">Decision Variables</h1>
      <table>
        <thead>
          <th>Id</th>
          <th>lower bound</th>
          <th>Name</th>
          <th>upper bound</th>
        </thead>
        <tbody>
          <tr v-for="i in lpModel.nrVars" :key="i">
            <td>
              <label class="mx-3">{{ i }}</label>
            </td>
            <td>
              <TInput class="mx-3 w-20" />
            </td>
            <td>
              <TInput class="mx-3 w-40" />
            </td>
            <td>
              <TInput class="mx-3 w-20" />
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <hr class="m-5">
    <div v-if="lpModel.nrCons > 0">
      <h1 class="my-2 text-xl">Constraints</h1>
      <table>
        <thead>
          <th>Id</th>
          <th>lower bound</th>
          <th>variable</th>
          <th>upper bound</th>
        </thead>
        <tbody>
          <tr v-for="i in lpModel.nrCons" :key="i">
            <td>
              <label class="mx-3">{{ i }}</label>
            </td>
            <td>
              <TInput class="mx-3 w-20" />
            </td>
            <td>
              <TInput class="mx-3 w-40" />
            </td>
            <td>
              <TInput class="mx-3 w-20" />
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-if="lpModel.nrCons == 0">
      <p>No constraints in this model</p>
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