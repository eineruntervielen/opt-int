<template>
  <Menubar :model="items">
    <template #start>
      <img class="w-10" src="../assets/img/LogoTessa.png" alt="">
    </template>
<!--    <template #end>-->
<!--      <div class="flex">-->
<!--        <img class="w-10" src="../assets/img/LogoDiscord.svg" alt="">-->
<!--        <img class="w-10" src="../assets/img/LogoGithub.png" alt="">-->
<!--      </div>-->
<!--    </template>-->
  </Menubar>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      items: [
        {
          label: 'Home',
          icon: 'pi pi-home',
          to: '/'
        },
        {
          label: 'Optimizer',
          icon: 'pi pi-th-large',
          items: [
            {
              label: 'Linear Programming',
              to: '/lp'
            },
            {
              label: 'Knapsack',
              to: '/knapsack'
            },
            {
              label: 'Staffscheduling',
              to: '/staffscheduling'
            },
          ]
        },
        {
          label: 'About',
          icon: 'pi pi-fw pi-question-circle',
          to: '/about'
        },
      ]
    }
  }
}
</script>