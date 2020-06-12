<template>
  <div class="home-root">
    <PageTitle
      title="Amazing Services"
      description="Use these amazing services to beat the driving test."
    />
    <div class="home-wrap">
      <ServiceCard
        imgPath="database.jpg"
        title="Quiz Database"
        description="Study on the quiz getting from official website."
        @click.native="()=>$router.push('quiz')"
      />
      <ServiceCard
        imgPath="test.jpg"
        title="Practice test"
        description="Doing the practice test to find your weakness."
        @click.native="()=>$router.push('practice')"
      />
      <ServiceCard
        imgPath="sign.jpg"
        title="Sign Recognition"
        description="Unfamiliar sign on the road? Get the answer here!"
        @click.native="()=>$router.push('sign')"
      />
    </div>
  </div>
</template>

<script>
import ServiceCard from "@/components/ServiceCard";
import PageTitle from "@/components/PageTitle";

export default {
  name: "Home",
  components: {
    ServiceCard,
    PageTitle
  }
};
</script>

<style lang="scss" scoped>
@import "../assets/font";
@import "../assets/color";

.home-root {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: "Lora", sans-serif;
  margin: 60px 0;
  padding: 0 18px;
  box-sizing: border-box;
  .home-wrap {
    width: 100%;
    max-width: 1200px;
    display: flex;
    align-items: center;
    justify-content: space-around;
  }
}

@media screen and (max-width: 1024px) {
  .home-root {
    .home-wrap {
      flex-direction: column;
    }
  }
}
</style>