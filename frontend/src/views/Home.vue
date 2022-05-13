<template>
  <!-- landing part -->
  <div class="flex flex-row h-screen justify-center items-center">
    <img src="./../assets/BackgroundHome.png" class="-z-10 fixed overflow-hidden" />
    <div class="flex flex-col">
      <h1 class="text-9xl text-gray-50 italic">spORTs➟</h1>
      <h2 class="text-xl mt-5 ml-5 text-gray-50 italic">super powerfull operations research tool suite</h2>
      <p class="mt-5 ml-5">»Use powerfull optimization techniques to bring super-powers to your business«</p>
    </div>
    <!-- first hero -->
  </div>
  <div class="h-screen bg-gray-900 grid grid-rows-6 grid-flow-col gap-52 py-32 px-72">
    <div class="row-start-1  row-span-3 shadow-xl p-5 flex flex-col">
      <h1 class="text-gray-50 text-3xl mt-5 text-amber-400">
        Linear Optimization
      </h1>
      <h1 class="text-gray-50">Check it out</h1>
      <ul class="text-gray-50">
      </ul>
    </div>
    <div class="row-start-2  row-span-3 shadow-xl p-5">
      <h1 class="text-gray-50 text-3xl mt-5 text-amber-400">Constraint Programming</h1>
    </div>
  </div>
  <!-- second hero -->
  <div class="h-screen bg-gradient-to-t from-gray-900 grid grid-rows-6 grid-flow-col gap-52 py-32 px-72">
    <div class="row-start-2  row-span-3 shadow-xl p-5">
      <h1 class="text-gray-50 text-3xl mt-5 text-gray-900">
        Routing
      </h1>
    </div>
    <div class="row-start-1  row-span-3 shadow-xl p-5">
      <h1 class="text-gray-50 text-3xl mt-5 text-gray-900">
        Scheduling
      </h1>
      <ul class="list-disc m-5">
        <li
          class="text-xl my-5 transition transform hover:list-disc hover:translate-x-5  hover:cursor-pointer delay-70 duration-300 ease-in-out">
          Plan your shifts days ahead
        </li>

        <li
          class="text-xl my-5 transition transform hover:list-disc hover:translate-x-5  hover:cursor-pointer delay-70 duration-300 ease-in-out">
          Include all your workers and co-workers work-hour-constraints
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home"
};
</script>