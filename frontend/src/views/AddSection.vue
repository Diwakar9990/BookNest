<template>
  <div class="homeView">
    <AdminNav />
    <AdminSideBar />
    <CreateSection />
  </div>
</template>

<script>
import AdminSideBar from "../components/admin/AdminSideBar.vue";
import AdminNav from "@/components/admin/AdminNav.vue";
import CreateSection from "../components/admin/AddSection.vue";
export default {
  name: "AddSection",
  components: {
    AdminNav,
    AdminSideBar,
    CreateSection,
  },
};
</script>

<style></style>
