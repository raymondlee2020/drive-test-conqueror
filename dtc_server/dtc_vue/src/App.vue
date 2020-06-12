<template>
  <div id="app">
    <MenuBar />
    <div class="cover-img">
      <div class="slogan-container">
        <span class="slogan main">Driving test is not as difficult as you think</span>
        <span
          class="slogan sub"
        >With our quiz database, practice test, sign recognition, it will never be a problem.</span>
      </div>
    </div>
    <router-view />
  </div>
</template>

<script>
import MenuBar from "@/components/MenuBar.vue";

export default {
  name: "App",
  components: {
    MenuBar
  }
};
</script>

<style lang="scss" scoped>
@import "./assets/font";
@import "./assets/color";

#app {
  font-family: "Lora", Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  .cover-img {
    width: 100%;
    height: 670px;
    display: flex;
    flex-direction: column;
    align-items: center;
    background-image: url("./assets/cover.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    .slogan-container {
      width: 100%;
      height: 100%;
      max-width: 1200px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: center;
      padding: 0 18px;
      box-sizing: border-box;
      .slogan {
        width: 100%;
        max-width: 740px;
        color: $light-blue;
      }
      .main {
        font-size: $pc-2l;
      }
      .sub {
        font-size: $pc-md;
        margin: 24px 0;
      }
    }
  }
}

@media screen and (max-width: 1024px) {
  #app {
    .cover-img {
      background-position: center;
    }
  }
}

@media screen and (max-width: 600px) {
  #app {
    .cover-img {
      background-position: 68%;
      .slogan-container {
        .main {
          font-size: $mb-xl;
        }
      }
    }
  }
}
</style>
