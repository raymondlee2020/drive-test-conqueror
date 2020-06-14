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
        action="https://drive-test-conqueror.herokuapp.com/api/signrecognition"
        list-type="picture"
        name="signImg"
        :multiple="false"
        :limit="1"
        :before-upload="beforeUploadHandler"
        :on-success="successHandler"
      >
        <div>
          <el-button slot="trigger" size="small" type="primary">Select File To Upload</el-button>
        </div>
        <div class="el-upload__tip" slot="tip">Only jpg/png format is acceptable.</div>
      </el-upload>
    </div>
    <div class="result-container" v-if="hasResult">
      <span class="result-title">Possible Results</span>
      <div class="resut-cards-wrap">
        <ResultCard v-for="(item, index) in result" :key="index" :name="item.name" :img="item.img" />
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
      hasResult: false,
      proccessing: false,
      result: []
    };
  },
  methods: {
    beforeUploadHandler: function(file) {
      const isValid =
        file.type === "image/jpeg" ||
        file.type === "image/jpg" ||
        file.type === "image/png";
      if (!isValid) {
        this.$message.error("Invalid file format");
      }
      return isValid;
    },
    successHandler: function(response) {
      this.result = []
      response.forEach(item => {
        if (item.img) {
          this.result.push({
            name: item.name,
            img: "data:image/png;base64," + item.img
          });
        }
      });
      // setTimeout(() => this.$refs.upload.clearFiles(), 1500);
      this.hasResult = true;
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