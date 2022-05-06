<template>
  <button
    class="
      rounded
      my-4
      px-4
      py-1
      text-sm
      shadow-xl
      text-gray-100
      bg-gray-800
      hover:cursor-pointer hover:text-gray-100 hover:bg-gray-600
    "
  >
  {{ name }}
  </button>
</template>

<script>
export default {
    name: "SBBtn",
    props: {
        name: String,
    }
};
</script>