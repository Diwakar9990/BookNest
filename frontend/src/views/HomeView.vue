<template>
  <div class="homeView">
    <NavBar />
    <SideBar />
    <HomeCard />
  </div>
</template>

<script>
import SideBar from "../components/layout/SideBar.vue";
import NavBar from "../components/layout/NavBar.vue";
import HomeCard from "../components/user/HomeCard.vue";
export default {
  name: "HomeView",
  components: {
    SideBar,
    NavBar,
    HomeCard,
  },
};
</script>

<style></style>
