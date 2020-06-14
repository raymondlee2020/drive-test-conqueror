<template>
  <div class="practice-card-root">
    <div class="text-container">
      <span class="quiz">{{quiz}}</span>
      <div class="options">
        <el-radio-group v-model="choice" @change="onChange" :disabled="disabled">
          <el-radio
            class="option"
            v-for="(item, index) in options"
            :key="index"
            :label="index"
          >{{item}}</el-radio>
        </el-radio-group>
      </div>
      <span class="answer" v-if="showAns">答案: ({{answer}})</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "PracticeCard",
  props: {
    quiz: String,
    options: Array,
    answer: String,
    showAns: {
      type: Boolean,
      default: true
    },
    onChange: Function,
    disabled: {
      type: Boolean,
      default: false
    }
  },
  data: function() {
    return {
      choice: 0
    };
  }
};
</script>

<style lang="scss" scoped>
@import "../assets/font";
@import "../assets/color";

.practice-card-root {
  width: 100%;
  max-width: 1200px;
  display: flex;
  justify-content: flex-start;
  margin-bottom: 18px;
  .text-container {
    flex: 1;
    display: flex;
    flex-direction: column;
    font-size: $pc-md;
    letter-spacing: 1px;
    .quiz {
      color: $black;
      margin-bottom: 10px;
    }
    .options {
      display: flex;
      color: $gray;
      margin-bottom: 12px;
    }
    .answer {
      width: 100%;
      text-align: right;
      color: $red;
    }
  }
}

@media screen and (max-width: 600px) {
  .practice-card-root {
    .text-container {
      .options {
        flex-direction: column;
        .option {
          margin-right: 0;
          margin-bottom: 6px;
        }
      }
    }
  }
}
</style>

<style lang="scss">
@import "../assets/font";
@import "../assets/color";

@media screen and (max-width: 600px) {
  .el-radio-group {
    display: flex;
    flex-direction: column;
    .option {
      margin-bottom: 8px;
    }
  }
}
.el-radio__label {
  font-size: $pc-md;
  margin-right: 16px;
  white-space: pre-wrap;
}
.el-radio__input.is-checked + .el-radio__label {
  color: $dark-blue;
}
.el-radio__input.is-checked .el-radio__inner {
  border-color: $dark-blue;
  background: $dark-blue;
}
</style>