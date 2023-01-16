<template>
  <div id="app" class="flex flex-col h-screen bg-slate-200 text-slate-900">
    <Navbar/>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: "App"
};
</script>
