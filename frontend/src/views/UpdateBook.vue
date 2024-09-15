<template>
  <div class="homeView">
    <AdminNav />
    <AdminSideBar />
    <EditBook :id="id" />
  </div>
</template>

<script>
import AdminSideBar from "../components/admin/AdminSideBar.vue";
import AdminNav from "@/components/admin/AdminNav.vue";
import EditBook from "../components/admin/UpdateBook.vue";
export default {
  name: "UpdateBook",
  props: ["id"],
  components: {
    AdminSideBar,
    AdminNav,
    EditBook,
  },
};
</script>

<style></style>
