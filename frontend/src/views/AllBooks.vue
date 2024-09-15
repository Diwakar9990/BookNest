<template>
  <div class="homeView">
    <AdminNav />
    <AdminSideBar />
    <ShowBooks />
  </div>
</template>

<script>
import AdminSideBar from "../components/admin/AdminSideBar.vue";
import AdminNav from "@/components/admin/AdminNav.vue";
import ShowBooks from "../components/admin/ShowBooks.vue";
export default {
  name: "AllBooks",
  components: {
    AdminSideBar,
    AdminNav,
    ShowBooks,
  },
};
</script>

<style></style>
