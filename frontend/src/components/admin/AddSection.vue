<template>
  <div>
    <h4 class="error" v-if="error">
      Please <a href="http://localhost:8080/"> Login </a> as Admin to Continue
    </h4>
    <div v-else class="section-form">
      <h2>Create New Section</h2>
      <form @submit.prevent="createSection">
        <div class="form-group">
          <label for="name">Section Name</label>
          <input type="text" id="name" v-model="name" required />
        </div>
        <div class="form-group">
          <label for="description">Description</label>
          <textarea id="description" v-model="description" required></textarea>
        </div>
        <button type="submit" class="btn">Create Section</button>
      </form>
      <div v-if="message" class="message">{{ message }}</div>
      <div v-if="err" class="err">{{ err }}</div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CreateSection",
  data() {
    return {
      name: "",
      description: "",
      message: "",
      error: "",
      err: "",
    };
  },
  methods: {
    async createSection() {
      try {
        const response = await axios.post(
          "http://localhost:5000/api/sections/",
          {
            name: this.name,
            description: this.description,
          },
          {
            withCredentials: true,
          }
        );
        console.log(response);
        this.message = response.data.message;
        this.name = "";
        this.description = "";
        this.$router.push("/admin/sections");
      } catch (error) {
        if (error.response) {
          console.log(error.response);
          this.error = error.response.data.msg;
          this.err = error.response.data.message;
          this.message = "";
        } else {
          this.error = "An error occurred while creating the section";
          this.message = "";
        }
      }
    },
  },
};
</script>

<style>
.section-form {
  max-width: 500px;
  margin: 50px auto;
  padding: 20px;
  background: rgb(0, 65, 134);
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 15px;
}

.form-group input,
textarea {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.form-group label {
  color: white;
}
.form-group textarea {
  resize: vertical;
}

.btn {
  background-color: #007bff;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn:hover {
  background-color: #003cff;
}

.section-form .message {
  margin-top: 20px;
  color: rgb(255, 255, 255);
}

.err {
  margin: 10px 0;
  color: rgb(255, 22, 22);
  font-weight: 600;
}
</style>
