<template>
  <div id="app" class="font-mono">
    <Navbar />
    <router-view />
    <Footer />
  </div>
</template>

<script>
import Footer from "./components/Footer.vue";
export default {
    name: "App",
    created() {
        const response = fetch("/api").then(data => console.log("data", data))
            .catch(e => {
            console.error("Error:", e);
        });
        console.log(response);
    },
    components: { Footer }
};
</script>


<style>
.background {
  /* for some reason tailwind negative z-index doesn't work */
  z-index: -1;
}
</style>
