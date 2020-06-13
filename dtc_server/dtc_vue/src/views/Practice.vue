<template>
  <div class="practice-root">
    <PageTitle title="Practice Test" description="Doing the practice test to find your weakness." />
    <PracticeCard
      v-for="(item, index) in quizs"
      :key="index"
      :quiz="item.quiz"
      :options="item.options"
      :answer="item.answer"
      :showAns="item.showAns"
      :onChange="(choice)=>changeChoiceHandler(index, choice)"
      :disabled="!testing"
    />
    <div class="button-container">
      <el-button v-if="testing" class="submit-button" @click="submitAns">Submit</el-button>
      <el-button v-if="!testing" class="reset-button" @click="resetQuizs">Reset</el-button>
    </div>
  </div>
</template>

<script>
import PageTitle from "@/components/PageTitle";
import PracticeCard from "@/components/PracticeCard";

export default {
  name: "Practice",
  components: {
    PageTitle,
    PracticeCard
  },
  data: function() {
    return {
      quizs: [
        {
          quiz: "1. 題目一內容",
          options: ["(1) 選項一", "(2) 選項二", "(3) 選項三"],
          answer: "1",
          ansIndex: 0,
          choice: 0,
          showAns: false
        },
        {
          quiz: "2. 題目二內容",
          options: ["(1) 選項一", "(2) 選項二", "(3) 選項三"],
          answer: "1",
          ansIndex: 0,
          choice: 0,
          showAns: false
        },
        {
          quiz: "3. 題目三內容",
          options: ["(O)", "(X)"],
          answer: "O",
          ansIndex: 0,
          choice: 0,
          showAns: false
        },
        {
          quiz: "4. 題目四內容",
          options: ["(O)", "(X)"],
          answer: "O",
          ansIndex: 0,
          choice: 0,
          showAns: false
        }
      ],
      testing: true
    };
  },
  methods: {
    changeChoiceHandler: function(index, choice) {
      this.quizs[index].choice = choice;
    },
    submitAns: function() {
      let score = 100;
      this.quizs.forEach(item => {
        if (item.ansIndex !== item.choice) {
          item.showAns = true;
          score -= 2;
        }
      });
      this.testing = false;
      console.log(score);
    },
    resetQuizs: function() {
      this.testing = true;
    }
  }
};
</script>

<style lang="scss" scoped>
@import "../assets/font";
@import "../assets/color";

.practice-root {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: "Lora", "Noto Sans TC", sans-serif;
  margin: 60px 0;
  padding: 0 18px;
  box-sizing: border-box;
  .button-container {
    width: 100%;
    display: flex;
    justify-content: center;
    margin-top: 12px;
    .submit-button {
      border-color: $dark-blue;
      color: $dark-blue;
    }
    .reset-button {
      border-color: $red;
      color: $red;
    }
    .reset-button:hover,
    .reset-button:focus {
      background-color: rgba(192, 67, 101, 0.2);
    }
  }
}
</style>