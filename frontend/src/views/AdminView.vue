<template>
  <div class="home">
    <div id="logo">
      <img
        src="../assets/booknest-high-resolution-logo-transparent.png"
        height="100"
        width="400"
      />
    </div>
    <AdminLogin />
  </div>
</template>

<script>
import AdminLogin from "../components/admin/AdminLogin.vue";
export default {
  name: "AdminView",
  components: {
    AdminLogin,
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
