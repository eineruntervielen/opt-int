<template>
    <a class="text-xl px-4 my-4 text-white transition ease-in-out hover:underline hover:-translate-y-1">{{ name }}</a>
</template>

<script>
export default {
  name: "NavbarLink",
  props: {
    name: String,
  }
};
</script>