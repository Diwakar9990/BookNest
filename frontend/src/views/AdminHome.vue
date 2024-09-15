<template>
  <div class="homeView">
    <AdminNav />
    <AdminSideBar />
    <AdminDash />
  </div>
</template>

<script>
import AdminSideBar from "@/components/admin/AdminSideBar.vue";
import AdminNav from "@/components/admin/AdminNav.vue";
import AdminDash from "@/components/admin/AdminDash.vue";

export default {
  name: "AdminHome",
  components: {
    AdminNav,
    AdminSideBar,
    AdminDash,
  },
};
</script>

<style></style>
