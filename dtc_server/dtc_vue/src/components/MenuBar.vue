<template>
  <div class="menu-bar-root">
    <div class="menu-bar-wrap">
      <el-container>
        <el-aside width="300px">
          <div class="logo">
            <div class="logo-main">
              <span class="black">Driving Test</span>
              <span class="orange">Conqueror</span>
            </div>
            <div class="logo-sub">
              <span class="blue">Get Driver License Easily</span>
            </div>
          </div>
        </el-aside>
        <el-main>
          <el-menu
            :default-active="activeIndex"
            mode="horizontal"
            @select="handleSelect"
            text-color="#1D1D1F"
            active-text-color="#92ACBD"
            class="pc-menu"
          >
            <el-menu-item index="1">
              <router-link to="/">Home</router-link>
            </el-menu-item>
            <el-menu-item index="2">
              <router-link to="/">Quiz Database</router-link>
            </el-menu-item>
            <el-menu-item index="3">
              <router-link to="/">Practice Test</router-link>
            </el-menu-item>
            <el-menu-item index="4">
              <router-link to="/">Sign Recognition</router-link>
            </el-menu-item>
          </el-menu>
          <el-button type="text" class="mb-menu" @click="drawer = true">
            <i class="fa fa-bars icon-size" aria-hidden="true" />
          </el-button>
          <el-drawer :visible.sync="drawer" :with-header="false" size="240px">
            <router-link
              :class="activeIndex=='1'?'active link':'link'"
              to="/"
              @click.native="()=>handleSelect('1')"
            >Home</router-link>
            <router-link
              :class="activeIndex=='2'?'active link':'link'"
              to="/"
              @click.native="()=>handleSelect('2')"
            >Quiz Database</router-link>
            <router-link
              :class="activeIndex=='3'?'active link':'link'"
              to="/"
              @click.native="()=>handleSelect('3')"
            >Practice Test</router-link>
            <router-link
              :class="activeIndex=='4'?'active link':'link'"
              to="/"
              @click.native="()=>handleSelect('4')"
            >Sign Recognition</router-link>
          </el-drawer>
        </el-main>
      </el-container>
    </div>
  </div>
</template>

<script>
export default {
  name: "MenuBar",
  props: {},
  data: function() {
    return {
      activeIndex: "1",
      drawer: false
    };
  },
  methods: {
    handleSelect: function(index) {
      this.activeIndex = index;
    }
  }
};
</script>

<style lang="scss" scoped>
@import "../assets/font";
@import "../assets/color";

.menu-bar-root {
  width: 100%;
  display: flex;
  justify-content: center;
  font-family: "Lora", sans-serif;
  .menu-bar-wrap {
    width: 100%;
    max-width: 1200px;
    margin: 0 18px;
    .logo {
      font-size: $pc-lg;
      font-weight: bold;
      letter-spacing: 1px;
      flex-direction: column;
      padding: 18px 0;
      .logo-main {
        display: flex;
        align-items: flex-end;
      }
      .logo-sub {
        display: flex;
        align-items: flex-start;
      }
      .black {
        color: $black;
        margin-right: 6px;
      }
      .orange {
        color: $orange;
      }
      .blue {
        color: $light-blue;
        font-size: $pc-sm;
        font-weight: normal;
        letter-spacing: 3.1px;
      }
    }
    .pc-menu {
      display: block;
    }
    .el-aside {
      display: flex;
      align-items: center;
    }
    .el-main {
      padding: 0;
      display: flex;
      align-items: center;
      justify-content: flex-end;
      margin-top: -12px;
    }
    .el-menu {
      float: right;
    }
    .el-menu.el-menu--horizontal {
      border-bottom: none;
    }
    .el-menu-item {
      font-size: $pc-sm;
      letter-spacing: 1.5px;
    }
    .mb-menu {
      color: $black;
      display: none;
    }
    .icon-size {
      font-size: 30px;
    }
    a {
      text-decoration: none;
    }
    .link {
      color: $black;
      padding: 12px 0;
    }
    .active {
      color: $dark-blue;
    }
  }
}

@media screen and (max-width: 1024px) {
  .menu-bar-root {
    .menu-bar-wrap {
      .pc-menu {
        display: none;
      }
      .mb-menu {
        display: block;
      }
    }
  }
}
</style>

<style lang="scss">
.menu-bar-root {
  .menu-bar-wrap {
    .el-drawer__body {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
  }
}
</style>