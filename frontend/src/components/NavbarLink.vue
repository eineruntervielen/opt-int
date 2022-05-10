<template>
  <a class="text-xl px-4 my-4 text-white no-underline hover:underline">{{ name }}</a>
</template>

<script>
export default {
  name: "NavbarLink",
  props: {
    name: String,
  }
};
</script>