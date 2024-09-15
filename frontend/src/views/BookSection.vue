<template>
  <div class="homeView">
    <NavBar />
    <SideBar />
    <SectionOfBooks />
  </div>
</template>

<script>
import SideBar from "../components/layout/SideBar.vue";
import NavBar from "../components/layout/NavBar.vue";
import SectionOfBooks from "../components/user/BookSection.vue";
export default {
  name: "BookSection",
  components: {
    SideBar,
    NavBar,
    SectionOfBooks,
  },
};
</script>

<style></style>
