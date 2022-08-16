<template>
  <Card>
    <h1 class="my-2 text-2xl font-light py-2 text-gray-700">LP-Generator</h1>
    <div class="my-3">
      <label class="px-1 text-sm font-bold text-gray-700">Nr. of decision variables</label><br />
      <input class="shadow border rounded text-gray-700 py-1 px-3 hover:shadow-inner transition " type="number" min="1"
        step="1" v-model="nrVariables" @keyup="changeForm" @click="changeForm" />
    </div>
    <div class="my-3">
      <label class="px-1 text-sm font-bold text-gray-700">Nr. of constraints</label><br />
      <input class="shadow border rounded text-gray-700 py-1 px-3 hover:shadow-inner transition " type="number" min="0"
        step="1" v-model="nrConstraints" @keyup="changeForm" @click="changeForm" />
    </div>
  </Card>
</template>

<script>
export default {
  name: "LPGenForm",
  data() {
    return {
      nrVariables: 1,
      nrConstraints: 1,
    };
  },
  methods: {
    changeForm() {
      this.$emit('changeForm', {
        variables: this.nrVariables,
        constraints: this.nrConstraints
      });
    },
  },
};
</script>