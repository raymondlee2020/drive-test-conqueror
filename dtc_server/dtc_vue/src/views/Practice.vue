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
    <el-dialog title="Your Score" :visible.sync="dialogVisible" width="300px">
      <div class="score">{{score}}</div>
    </el-dialog>
  </div>
</template>

<script>
import PageTitle from "@/components/PageTitle";
import PracticeCard from "@/components/PracticeCard";
import { Get } from "@/assets/utils";

export default {
  name: "Practice",
  components: {
    PageTitle,
    PracticeCard
  },
  data: function() {
    return {
      dialogVisible: false,
      trueFalse: [],
      multipleChoice: [],
      quizs: [],
      testing: true,
      score: 100
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
      this.score = score;
      this.testing = false;
      this.dialogVisible = true;
    },
    resetQuizs: function() {
      this.testing = true;
      this.shuffle(this.trueFalse);
      this.shuffle(this.multipleChoice);
      this.quizs = [];
      if (this.trueFalse.length < 25) {
        this.quizs = this.quizs.concat(
          this.trueFalse.map((item, index) => {
            return {
              quiz: `${index + 1}. ${item.quiz}`,
              options: item.options,
              answer: item.answer,
              ansIndex: item.ansIndex,
              choice: 0,
              showAns: false
            };
          })
        );
      } else {
        this.quizs = this.quizs.concat(
          this.trueFalse.slice(24).map((item, index) => {
            return {
              quiz: `${index + 1}. ${item.quiz}`,
              options: item.options,
              answer: item.answer,
              ansIndex: item.ansIndex,
              choice: 0,
              showAns: false
            };
          })
        );
      }
      if (this.multipleChoice.length < 25) {
        this.quizs = this.quizs.concat(
          this.multipleChoice.map((item, index) => {
            return {
              quiz: `${index + 26}. ${item.quiz}`,
              options: item.options,
              answer: item.answer,
              ansIndex: item.ansIndex,
              choice: 0,
              showAns: false
            };
          })
        );
      } else {
        this.quizs = this.quizs.concat(
          this.multipleChoice.slice(24).map((item, index) => {
            return {
              quiz: `${index + 26}. ${item.quiz}`,
              options: item.options,
              answer: item.answer,
              ansIndex: item.ansIndex,
              choice: 0,
              showAns: false
            };
          })
        );
      }
    },
    shuffle: function(array) {
      for (let i = array.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
    }
  },
  mounted: async function() {
    const trueFalseRawData = await Get("ruletruefalse");
    const multipleChoiceRawData = await Get("rulemultiplechoice");
    this.trueFalse = trueFalseRawData.data
      .sort((a, b) => a.quizId - b.quizId)
      .map(item => {
        return {
          quiz: item.quiz,
          options: ["(O)", "(X)"],
          answer: item.ansIndex === 0 ? "O" : "X",
          ansIndex: item.ansIndex
        };
      });
    this.multipleChoice = multipleChoiceRawData.data
      .sort((a, b) => a.quizId - b.quizId)
      .map(item => {
        return {
          quiz: item.quiz,
          options: [item.option1, item.option2, item.option3],
          answer: (item.ansIndex + 1).toString(),
          ansIndex: item.ansIndex
        };
      });
    this.resetQuizs();
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
  .score {
    width: 100%;
    display: flex;
    justify-content: center;
    font-size: 80px;
    font-weight: bold;
  }
}
</style>

<style lang="scss">
@import "../assets/font";
@import "../assets/color";

.el-dialog__title {
  font-size: $pc-lg;
  font-weight: bold;
}
</style>