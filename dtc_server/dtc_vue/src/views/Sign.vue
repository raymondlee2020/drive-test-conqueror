<template>
  <div class="sign-root">
    <PageTitle
      title="Sign Recognition"
      description="Unfamiliar sign on the road? Get the answer here!"
    />
    <div class="upload-container">
      <el-upload
        class="upload-demo"
        ref="upload"
        action="https://"
        list-type="picture"
        :auto-upload="false"
        :multiple="false"
        :limit="1"
      >
        <div>
          <el-button slot="trigger" size="small" type="primary">Select File</el-button>
          <el-button
            style="margin-left: 10px;"
            size="small"
            type="success"
            @click="submitUpload"
          >Upload</el-button>
        </div>
        <div class="el-upload__tip" slot="tip">Only jpg/png format is acceptable.</div>
      </el-upload>
    </div>
    <div class="result-container" v-if="hasResult">
      <span class="result-title">Possible Results</span>
      <div class="resut-cards-wrap">
        <ResultCard name="當心行人" />
        <ResultCard name="當心行人" />
        <ResultCard name="當心行人" />
        <ResultCard name="當心行人" />
        <ResultCard name="當心行人" />
        <ResultCard name="當心行人" />
        <ResultCard name="當心行人" />
        <div class="space" />
        <div class="space" />
        <div class="space" />
      </div>
    </div>
  </div>
</template>

<script>
import PageTitle from "@/components/PageTitle";
import ResultCard from "@/components/ResultCard";

export default {
  name: "Sign",
  components: {
    PageTitle,
    ResultCard
  },
  data: function() {
    return {
      hasResult: true
    };
  },
  methods: {
    submitUpload: function() {
      this.$refs.upload.submit();
    }
  }
};
</script>

<style lang="scss" scoped>
@import "../assets/font";
@import "../assets/color";

.sign-root {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: "Lora", "Noto Sans TC", sans-serif;
  margin: 60px 0;
  padding: 0 18px;
  box-sizing: border-box;
  .upload-container {
    width: 100%;
    max-width: 1200px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 28px;
    .upload-demo {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
  }
  .result-container {
    width: 100%;
    max-width: 1200px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    .result-title {
      color: $black;
      font-size: $pc-lg;
      font-weight: bold;
      margin-bottom: 18px;
    }
    .resut-cards-wrap {
      display: flex;
      justify-content: space-around;
      flex-wrap: wrap;
      .space {
        width: 25%;
      }
    }
  }
}
</style>