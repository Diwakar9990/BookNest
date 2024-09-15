<template>
  <div class="homeView">
    <AdminNav />
    <AdminSideBar />
    <CreateBook />
  </div>
</template>

<script>
import AdminNav from "@/components/admin/AdminNav.vue";
import AdminSideBar from "../components/admin/AdminSideBar.vue";
import CreateBook from "../components/admin/AddBook.vue";
export default {
  name: "AddBook",
  components: {
    AdminNav,
    AdminSideBar,
    CreateBook,
  },
};
</script>

<style></style>
