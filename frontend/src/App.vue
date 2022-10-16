<template>
  <div id="app" class="font-mono">

    <Navbar />
    <router-view />
    <div>
      <Chart class="w-96" type="pie" :data="chartData" :options="lightOptions" />
    </div>
    <Footer />
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      chartData: {
        labels: ['A', 'B', 'C'],
        datasets: [
          {
            data: [300, 50, 100],
            backgroundColor: ["#42A5F5", "#66BB6A", "#FFA726"],
            hoverBackgroundColor: ["#64B5F6", "#81C784", "#FFB74D"]
          }
        ]
      },
      lightOptions: {
        plugins: {
          legend: {
            labels: {
              color: '#495057'
            }
          }
        }
      }
    }
  }
};
</script>
