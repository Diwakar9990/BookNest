<template>
  <div class="home">
    <div id="logo">
      <img
        src="../assets/booknest-high-resolution-logo-transparent.png"
        height="100"
        width="400"
      />
    </div>
    <LoginPage />
  </div>
</template>

<script>
import LoginPage from "../components/user/LoginPage.vue";

export default {
  name: "LoginView",
  components: {
    LoginPage,
  },
};
</script>
<style>
.home {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
}
</style>
