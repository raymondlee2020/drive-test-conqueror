<template>
  <div class="quiz-card-root">
    <div class="text-container">
      <span class="quiz">{{quiz}}</span>
      <div class="options">
        <span class="option" v-for="(item, index) in options" :key="index">{{item}}</span>
      </div>
      <span class="answer">答案: ({{answer}})</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "QuizCard",
  props: {
    quiz: String,
    options: Array,
    answer: String
  }
};
</script>

<style lang="scss" scoped>
@import "../assets/font";
@import "../assets/color";

.quiz-card-root {
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
      margin-bottom: 8px;
    }
    .options {
      display: flex;
      color: $gray;
      margin-bottom: 12px;
      .option {
        margin-right: 16px;
      }
    }
    .answer {
      width: 100%;
      text-align: right;
      color: $dark-blue;
    }
  }
}

@media screen and (max-width: 600px) {
  .quiz-card-root {
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