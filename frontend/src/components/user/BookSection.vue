<template>
  <div>
    <div class="sections-container">
      <h4 class="error" v-if="error">
        {{ error }} <a href="http://localhost:8080/"> Login </a> to Continue
      </h4>
      <h4 v-if="message" class="delete-section">
        Section Deleted Successfully
      </h4>
      <h4 class="error" v-if="sections.length == 0">Loading...</h4>
      <div v-else>
        <h2 id="heading">All Sections</h2>
        <div class="sections">
          <div
            v-for="section in sections"
            :key="section.id"
            class="section-card"
          >
            <h3>{{ section.name }}</h3>
            <p>{{ section.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "SectionOfBooks",
  data() {
    return {
      sections: [],
      message: "",
      error: "",
    };
  },
  created() {
    this.fetchSections();
  },
  methods: {
    async fetchSections() {
      try {
        const response = await axios.get("http://localhost:5000/api/sections", {
          withCredentials: true,
        });
        this.sections = response.data.res;
      } catch (error) {
        this.error = error.response
          ? error.response.data.msg
          : "An error occurred while fetching sections";
      }
    },
  },
};
</script>

<style>
.sections-container {
  padding: 20px;
}

#heading {
  text-align: center;
  margin-bottom: 20px;
  color: rgb(0, 65, 134);
}

.sections {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.section-card {
  background: rgb(0, 65, 134);
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  margin: 10px;
  padding: 20px;
  width: 200px;
  text-align: center;
  color: #fff;
}
.icon-block {
  display: flex;
  justify-content: space-around;
  align-content: center;
}
.icon,
.icon a {
  cursor: pointer;
  text-decoration: none;
  color: #fff;
}
.delete-section {
  align-items: center;
  color: rgb(0, 65, 134);
}
</style>
