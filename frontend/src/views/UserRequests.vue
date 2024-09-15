<template>
  <div class="homeView">
    <NavBar />
    <SideBar />
    <UserRequests />
  </div>
</template>

<script>
import SideBar from "../components/layout/SideBar.vue";
import NavBar from "../components/layout/NavBar.vue";
import UserRequests from "../components/user/UserRequests.vue";

export default {
  components: {
    SideBar,
    NavBar,
    UserRequests,
  },
};
</script>

<style>
.homeView {
  padding: 0.2rem 0.5rem 0.5rem 1rem;
  margin: 1rem 1rem 1rem 5rem;
}
</style>
