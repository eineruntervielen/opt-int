<template>
  <div class="flex flex-col h-screen justify-center items-center">
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