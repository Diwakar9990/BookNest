<template>
  <div class="home">
    <div id="logo">
      <img
        src="../assets/booknest-high-resolution-logo-transparent.png"
        height="100"
        width="400"
      />
    </div>
    <RegisterPage />
  </div>
</template>

<script>
import RegisterPage from "../components/user/RegisterPage.vue";

export default {
  name: "RegisterView",
  components: {
    RegisterPage,
  },
};
</script>
<style>
home {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
}
</style>
