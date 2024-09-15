<template>
  <div class="homeView">
    <NavBar />
    <SideBar />
    <UserPage />
  </div>
</template>

<script>
import SideBar from "../components/layout/SideBar.vue";
import NavBar from "../components/layout/NavBar.vue";
import UserPage from "../components/user/UserPage.vue";

export default {
  name: "UserDetails",
  components: {
    SideBar,
    NavBar,
    UserPage,
  },
};
</script>

<style>
.homeView {
  padding: 0.2rem 0.5rem 0.5rem 1rem;
  margin: 1rem 1rem 1rem 5rem;
}
</style>
