<template>
  <nav class=" flex fixed items-center w-screen bg-gray-700 opacity-95">
    <ul class="flex flex-1 justify-center mr-auto">
      <router-link to="/home">
        <NavbarLink name="Home" />
      </router-link>
      <router-link to="/lp">
        <NavbarLink name="Linear Optimization" />
      </router-link>
    </ul>
    <ul class="flex">
      <li>
        <img alt="OR-Tools Logo" src="./../assets/orLogo.png" class="m-1 w-20 h-20" />
      </li>
    </ul>
    <ul class="flex flex-1 justify-center ml-auto">
      <router-link to="/info">
        <NavbarLink name="Info" />
      </router-link>
    </ul>
  </nav>
</template>

<script>
import NavbarLink from "./NavbarLink.vue";
export default {
  name: "Navbar",
  components: { NavbarLink }
};
</script>