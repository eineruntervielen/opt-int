<template>
  <div id="app" class="font-sans">
    <Navbar />
    <router-view />
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
export default {
    name: "App",
    created() {
        const response = fetch("/api").then(data => console.log("data", data))
            .catch(e => {
            console.error("Error:", e);
        });
        console.log(response);
    },
    components: { Navbar }
};
</script>


<style>
.background {
  /* for some reason tailwind negative z-index doesn't work */
  z-index: -1;
}
</style>
