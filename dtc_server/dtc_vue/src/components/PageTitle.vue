<template>
  <div class="page-title-root">
    <span class="title">{{title}}</span>
    <div class="divide" />
    <span class="des">{{description}}</span>
  </div>
</template>

<script>
export default {
  name: "PageTitle",
  props: {
    title: String,
    description: String
  }
};
</script>

<style lang="scss" scoped>
@import "../assets/font";
@import "../assets/color";

.page-title-root {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: "Lora", sans-serif;
  margin-bottom: 36px;
  .title {
    font-size: $pc-xl;
    font-weight: bold;
    color: $black;
  }
  .divide {
    width: 60px;
    height: 2px;
    background-color: $dark-blue;
    margin: 12px 0 6px;
  }
  .des {
    font-size: $pc-sm;
    color: $gray;
    text-align: center;
  }
}
</style>