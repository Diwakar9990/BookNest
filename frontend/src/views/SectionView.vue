<template>
  <div class="homeView">
    <AdminNav />
    <AdminSideBar />
    <SectionComponent />
  </div>
</template>

<script>
import AdminSideBar from "../components/admin/AdminSideBar.vue";
import AdminNav from "@/components/admin/AdminNav.vue";
import SectionComponent from "../components/admin/SectionComponent.vue";
export default {
  name: "SectionView",
  components: {
    AdminSideBar,
    AdminNav,
    SectionComponent,
  },
};
</script>

<style></style>
