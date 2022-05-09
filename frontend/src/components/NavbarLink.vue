<template>
  <a class="px-4 my-4 text-gray-300 hover:underline focus:translate-x-1">

    <!-- class="my-4 px-4 py-1 text shadow-xl text-gray-100 bg-gray-800 hover:cursor-pointer hover:text-gray-100 hover:bg-gray-600 "> -->
    {{ name }}
  </a>
</template>

<script>
export default {
  name: "NavbarLink",
  props: {
    name: String,
  }
};
</script>