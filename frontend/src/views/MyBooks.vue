<template>
  <div class="homeView">
    <NavBar />
    <SideBar />
    <BookCard />
  </div>
</template>

<script>
import SideBar from "../components/layout/SideBar.vue";
import NavBar from "../components/layout/NavBar.vue";
import BookCard from "../components/books/BookCard.vue";
export default {
  name: "MyBooks",
  components: {
    SideBar,
    NavBar,
    BookCard,
  },
};
</script>

<style></style>
