<template>
  <div class="quiz-root">
    <PageTitle
      title="Quiz Database"
      description="Study on the quiz getting from official website."
    />
    <el-radio-group v-model="quizType">
      <el-radio-button :label="0">是非題</el-radio-button>
      <el-radio-button :label="1">選擇題</el-radio-button>
    </el-radio-group>
    <div class="quizs" v-if="quizType === 0">
      <QuizCard
        v-for="(item, index) in trueFalse"
        :key="index"
        :quiz="item.quiz"
        :options="item.options"
        :answer="item.answer"
      />
    </div>
    <div class="quizs" v-if="quizType === 1">
      <QuizCard
        v-for="(item, index) in multipleChoice"
        :key="index"
        :quiz="item.quiz"
        :options="item.options"
        :answer="item.answer"
      />
    </div>
  </div>
</template>

<script>
import PageTitle from "@/components/PageTitle";
import QuizCard from "@/components/QuizCard";
import { Get } from "@/assets/utils";

export default {
  name: "Quiz",
  components: {
    PageTitle,
    QuizCard
  },
  data: function() {
    return {
      quizType: 0,
      trueFalse: [
        {
          quiz: "1. 題目一內容",
          options: ["(1) 選項一", "(2) 選項二", "(3) 選項三"],
          answer: "1"
        },
        {
          quiz: "2. 題目二內容",
          options: ["(1) 選項一", "(2) 選項二", "(3) 選項三"],
          answer: "1"
        }
      ],
      multipleChoice: [
        {
          quiz: "1. 題目一內容",
          options: ["(O)", "(X)"],
          answer: "O"
        },
        {
          quiz: "2. 題目二內容",
          options: ["(O)", "(X)"],
          answer: "O"
        }
      ]
    };
  },
  mounted: async function() {
    const trueFalseRawData = await Get("ruletruefalse");
    const multipleChoiceRawData = await Get("rulemultiplechoice");
    this.trueFalse = trueFalseRawData.data
      .sort((a, b) => a - b)
      .map(item => {
        return {
          quiz: `${item.quizId}. ${item.quiz}`,
          options: ["(O)", "(X)"],
          answer: item.ansIndex === 0 ? "O" : "X"
        };
      });
    this.multipleChoice = multipleChoiceRawData.data
      .sort((a, b) => a - b)
      .map(item => {
        return {
          quiz: `${item.quizId}. ${item.quiz}`,
          options: [item.option1, item.option2, item.option3],
          answer: (item.ansIndex + 1).toString()
        };
      });
  }
};
</script>

<style lang="scss" scoped>
@import "../assets/font";
@import "../assets/color";

.quiz-root {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: "Lora", "Noto Sans TC", sans-serif;
  margin: 60px 0;
  padding: 0 32px;
  box-sizing: border-box;
  .quizs {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 18px;
  }
}
</style>