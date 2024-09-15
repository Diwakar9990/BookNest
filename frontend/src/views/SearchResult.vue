<template>
  <div class="homeView">
    <NavBar />
    <SideBar />
    <div class="search-results">
      <h2>Search Results</h2>
      <div v-if="error" class="error">{{ error }}</div>
      <div v-if="books.length">
        <div class="book-section-block" v-if="books">
          <h2 style="color: #fff">Books by Search Result</h2>
          <div class="book-section">
            <div class="books" v-for="book in books" :key="book.id">
              <div class="img">img</div>
              <div class="book-detail">
                <h3>Title : {{ book.title }}</h3>
                <h3>Author : {{ book.author }}</h3>
                <button
                  type="button"
                  class="button-6"
                  @click="requestBook(book.id)"
                >
                  Request
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-else>
        <p class="bnf">No books found.</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import SideBar from "../components/layout/SideBar.vue";
import NavBar from "../components/layout/NavBar.vue";

export default {
  name: "SearchResult",
  components: {
    SideBar,
    NavBar,
  },
  data() {
    return {
      books: [],
      error: null,
      requestMessage: "",
    };
  },
  created() {
    this.searchBooks();
  },
  watch: {
    "$route.query": "searchBooks",
  },
  methods: {
    async searchBooks() {
      const searchCriteria = this.$route.query;

      try {
        const response = await axios.post(
          "http://localhost:5000/api/books/search",
          searchCriteria,
          { withCredentials: true }
        );
        this.books = response.data.res;
      } catch (error) {
        this.error = error.response
          ? error.response.data.msg
          : "An error occurred while searching books";
      }
    },
    async requestBook(id) {
      try {
        const response = await axios.get(
          `http://localhost:5000/api/requests/new/${id}`,
          {
            withCredentials: true,
          }
        );
        console.log(response.data);
        this.requestMessage = response.data.message;
        alert(this.requestMessage);
      } catch (error) {
        if (error.response) {
          this.requestMessage = error.response.data.message;
        } else {
          this.requestMessage = "An error occurred while requesting the book";
        }
        alert(this.requestMessage);
      }
    },
  },
};
</script>

<style>
.search-results {
  padding: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin: 5px 0;
}

.error {
  font-weight: 600;
}

.bnf {
  font-weight: 600;
  color: rgb(0, 47, 98);
  font-size: 1.4rem;
}
</style>
