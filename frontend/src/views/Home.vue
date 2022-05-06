<template>
  <div class="flex flex-col h-screen justify-center items-center">
    <img
      src="./../assets/world.avif"
      class="w-screen h-screen absolute opacity-40 -z-10"
    />
    <Card>
      <Deck :title="title" @changeTitle="title = $event" />
    </Card>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      title: "Main Component",
    };
  },
};
</script>