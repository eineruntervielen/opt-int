<template>
  <div id="app" class="font-sans">
    <Sidebar />
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
    created() {
    const response = fetch('/api').then(data => console.log('data', data))
      .catch(e => {
        console.error('Error:', e);
      })
    console.log(response)
  },
};
</script>