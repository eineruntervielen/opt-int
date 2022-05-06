<template>
  <div class="flex flex-col p5 m5 bg-slate-200">
    <h1>{{ title }}</h1>
    <input @keyup.enter="changeTitle" v-model="txtInput" type="text">
  </div>
</template>

<script>
export default {
  name: "Deck",
  props: {
    title: String,
  },
  data () {
    return {
      txtInput: 0,
    }

  },
  methods: {
    changeTitle() {
      console.log(this.txtInput)
      this.$emit("changeTitle", this.txtInput);
    },
  },
};
</script>

<style>
</style>