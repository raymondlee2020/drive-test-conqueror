<template>
  <div class="service-card-root">
    <img class="pic" :src="require(`@/assets/${imgPath}`)" />
    <div class="text-container">
      <span class="title">{{title}}</span>
      <span class="des">{{description}}</span>
      <div class="more-container">
        <span class="more">
          <span class="more-text">More</span>
          <i class="fa fa-chevron-right" aria-hidden="true" />
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ServiceCard",
  props: {
    imgPath: String,
    title: String,
    description: String
  }
};
</script>

<style lang="scss" scoped>
@import "../assets/font";
@import "../assets/color";

.service-card-root {
  flex: 1;
  max-width: 300px;
  height: 360px;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: 3px 3px 12px rgba(0, 0, 0, 0.4);
  cursor: pointer;
  .pic {
    width: 100%;
    height: auto;
  }
  .text-container {
    width: 100%;
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 20px;
    box-sizing: border-box;
    .title {
      font-size: $pc-lg;
      color: $black;
    }
    .des {
      font-size: $pc-sm;
      color: $gray;
      margin-top: 12px;
      line-height: 1.5;
    }
    .more-container {
      width: 100%;
      flex: 1;
      display: flex;
      justify-content: flex-end;
      align-items: flex-end;
      .more {
        display: flex;
        align-items: center;
        .more-text {
          margin-right: 6px;
          margin-bottom: 2px;
        }
      }
    }
  }
}

@media screen and (max-width: 1024px) {
  .service-card-root {
    width: 100%;
    max-width: 420px;
    height: 460px;
    margin-bottom: 40px;
  }
}

@media screen and (max-width: 600px) {
  .service-card-root {
    max-width: 300px;
    height: 360px;
  }
}
</style>