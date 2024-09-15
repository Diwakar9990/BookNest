<template>
  <div>
    <h4 class="error" v-if="error">
      Please
      <a href="http://localhost:8080/">Login</a>
      to Continue
    </h4>
    <div v-else class="section-form">
      <h2>Update Book</h2>
      <form @submit.prevent="updateBook">
        <div class="form-group">
          <label for="title">Title:</label>
          <input type="text" v-model="book.title" required />
        </div>
        <div class="form-group">
          <label for="content">Content:</label>
          <textarea id="description" v-model="book.content" required></textarea>
        </div>
        <div class="form-group">
          <label for="author">Author:</label>
          <input type="text" v-model="book.author" required />
        </div>
        <div class="form-group">
          <label for="section">Section:</label>
          <select v-model="book.section" required>
            <option
              v-for="section in sections"
              :key="section.id"
              :value="section.name"
            >
              {{ section.name }}
            </option>
          </select>
        </div>
        <button class="btn" type="submit">Update Book</button>
      </form>
      <div v-if="message" class="message">
        {{ message }}
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "EditBook",
  props: ["id"],
  data() {
    return {
      book: {
        title: "",
        content: "",
        author: "",
        section: "",
      },
      sections: [],
      message: "",
      error: "",
    };
  },
  created() {
    this.fetchSections();
    this.getBook();
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
    async getBook() {
      try {
        const response = await axios.get(
          `http://localhost:5000/api/books/${this.id}`,
          {
            withCredentials: true,
          }
        );
        this.message = response.data.message;
        this.book = {
          title: response.data.res.title,
          content: response.data.res.content,
          author: response.data.res.author,
          section: response.data.res.section,
        }; // Reset form
      } catch (error) {
        console.log(error.response.data);
        this.message = error.response.data.message;
      }
    },
    async updateBook() {
      try {
        const response = await axios.put(
          `http://localhost:5000/api/books/${this.id}`,
          {
            title: this.book.title,
            content: this.book.content,
            author: this.book.author,
            section: this.book.section,
          },
          {
            withCredentials: true,
          }
        );
        this.message = response.data.message;
        this.book = { title: "", content: "", author: "", section: "" }; // Reset form
        this.$router.push("/admin/books");
      } catch (error) {
        console.log(error.response.data);
        this.message = error.response.data.message;
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
</style>
