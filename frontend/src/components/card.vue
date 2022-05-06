<template>
  <div class="p-4 flex flex-col bg-gray-100 shadow-xl rounded-md">
      <slot></slot>
  </div>
</template>

<script>
export default {
    name: "Card",
    props: {
        content: String,
    }
};
</script>

<style>
</style>