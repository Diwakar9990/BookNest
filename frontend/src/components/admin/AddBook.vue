<template>
  <div>
    <h4 class="error" v-if="error">
      Please <a href="http://localhost:8080/"> Login </a> as Admin to Continue
    </h4>
    <div v-else class="section-form">
      <h2>Add a New Book</h2>
      <form @submit.prevent="addBook" enctype="multipart/form-data">
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
          <label for="file">Upload eBook:</label>
          <input type="file" @change="handleFileUpload" required />
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
        <button class="btn" type="submit">Add Book</button>
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
  name: "CreateBook",
  data() {
    return {
      book: {
        title: "",
        content: "",
        author: "",
        section: "",
      },
      file: null,
      sections: [],
      message: "",
      error: null,
    };
  },
  created() {
    this.fetchSections();
  },
  methods: {
    async fetchSections() {
      try {
        const response = await axios.get(
          "https://booknest-m2z6.onrender.com/api/sections",
          {
            withCredentials: true,
          }
        );
        this.sections = response.data.res;
      } catch (error) {
        this.error = error.response
          ? error.response.data.msg
          : "An error occurred while fetching sections";
      }
    },
    handleFileUpload(event) {
      this.file = event.target.files[0];
    },
    async addBook() {
      const formData = new FormData();
      formData.append("title", this.book.title);
      formData.append("content", this.book.content);
      formData.append("author", this.book.author);
      formData.append("section", this.book.section);
      formData.append("file", this.file);

      try {
        const response = await axios.post(
          "https://booknest-m2z6.onrender.com/api/books/",
          formData,
          {
            withCredentials: true,
          }
        );
        console.log(response.data);
        this.message = response.data.message;
        this.$router.push("/admin/books");
        this.book = { title: "", content: "", author: "", section: "" }; // Reset form
        this.file = null; // Reset file input
      } catch (error) {
        console.log(error.response);
        this.error = error.response
          ? error.response.data.error
          : "An error occurred while adding the book";
        this.message = "";
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
textarea,
select {
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
