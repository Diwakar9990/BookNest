<template>
  <div class="homeView">
    <AdminNav />
    <AdminSideBar />
    <UpdateSection :id="id" />
  </div>
</template>

<script>
import AdminSideBar from "../components/admin/AdminSideBar.vue";
import AdminNav from "@/components/admin/AdminNav.vue";
import UpdateSection from "../components/admin/UpdateSection.vue";
export default {
  name: "SectionView",
  props: ["id"],
  components: {
    AdminSideBar,
    AdminNav,
    UpdateSection,
  },
};
</script>

<style></style>
