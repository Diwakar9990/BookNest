<template>
  <div class="homeView">
    <AdminNav />
    <AdminSideBar />
    <RequestGranted />
  </div>
</template>

<script>
import AdminSideBar from "@/components/admin/AdminSideBar.vue";
import AdminNav from "@/components/admin/AdminNav.vue";
import RequestGranted from "@/components/admin/RequestGranted.vue";

export default {
  name: "AcceptedRequest",
  components: {
    AdminNav,
    AdminSideBar,
    RequestGranted,
  },
};
</script>

<style></style>
