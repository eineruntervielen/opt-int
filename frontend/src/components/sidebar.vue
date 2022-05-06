<template>
  <div
    class="
      flex flex-col
      justify-between
      bg-gray-700
      opacity-95
      fixed
      top-0
      left-0
      m-0
      p-3
      min-h-screen min-w-max
    "
  >
    <ul class="flex flex-col">
      <router-link to="/home" class="flex flex-col">
        <SBBtn name="Home" />
      </router-link>
      <router-link to="/lp" class="flex flex-col">
        <SBBtn name="Linear Optimization" />
      </router-link>
      <!-- <router-link to="/ip" class="flex flex-col">
        <SBBtn name="Integer Optimization" />
      </router-link>
      <router-link to="/cp" class="flex flex-col">
        <SBBtn name="Constraint Optimization" />
      </router-link>
      <router-link to="/routing" class="flex flex-col">
        <SBBtn name="Routing" />
      </router-link>
      <router-link to="/scheduling" class="flex flex-col">
        <SBBtn name="Scheduling" />
      </router-link> -->
    </ul>
    <ul class="flex flex-col">
      <router-link to="/info" class="flex flex-col">
        <SBBtn name="Info" />
      </router-link>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Sidebar",
};
</script>