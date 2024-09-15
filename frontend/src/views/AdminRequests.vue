<template>
  <div class="homeView">
    <AdminNav />
    <AdminSideBar />
    <PendingRequests />
  </div>
</template>

<script>
import AdminSideBar from "@/components/admin/AdminSideBar.vue";
import AdminNav from "@/components/admin/AdminNav.vue";
import PendingRequests from "@/components/admin/PendingRequests.vue";

export default {
  name: "AdminRequests",
  components: {
    AdminNav,
    AdminSideBar,
    PendingRequests,
  },
};
</script>

<style></style>
