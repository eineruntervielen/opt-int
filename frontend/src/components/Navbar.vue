<template>
  <nav :class="{ 'transition shadow duration-300 ease-in-out': !view.atTopOfPage }" class=" flex fixed items-center w-screen">
    <ul class="flex flex-1 justify-center mr-auto">
      <router-link to="/lp">
        <NavbarLink name="Linear Optimization" />
      </router-link>
      <router-link to="/staffscheduling">
        <NavbarLink name="Staff Scheduling" />
      </router-link>
    </ul>
    <ul class="flex">
      <router-link to="/">
        <img alt="OR-Tools Logo" src="./../assets/LogoORTools.png"
          class="m-1 w-10 h-10 transform hover:scale-110 hover:cursor-pointer ease-in-out duration-300" />
      </router-link>
    </ul>
    <ul class="flex flex-1 justify-center ml-auto">
      <router-link to="/contact">
        <NavbarLink name="Contact" />
      </router-link>
    </ul>
  </nav>
</template>

<script>
import NavbarLink from "./NavbarLink.vue";
export default {
  name: "Navbar",
  components: { NavbarLink },
  data() {
    return {
      view: {
        atTopOfPage: true
      }
    }
  },
  beforeMount() {
    window.addEventListener('scroll', this.handleScroll);
  },

  methods: {
    handleScroll() {
      if (window.pageYOffset > 0) {
        if (this.view.atTopOfPage) this.view.atTopOfPage = false
      } else {
        if (!this.view.atTopOfPage) this.view.atTopOfPage = true
      }
    }
  }
};
</script> 