<template>
  <div class="container">
    <nav>
      <h1><a href="http://localhost:8080/home">BookNest</a></h1>
      <div class="search-box">
        <form class="search" @submit.prevent="searchBooks">
          <select class="search-input" v-model="searchType" required>
            <option value="" disabled selected>Search by</option>
            <option value="author">Author</option>
            <option value="section">Section</option>
            <option value="title">Title</option>
          </select>
          <input
            id="search-input"
            type="text"
            v-model="searchQuery"
            placeholder="Search favorite books"
            required
          />
          <input id="button" type="submit" value="Search" />
        </form>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {
      searchType: "",
      searchQuery: "",
    };
  },
  methods: {
    searchBooks() {
      const searchCriteria = {};
      searchCriteria[this.searchType] = this.searchQuery;
      this.$router.push({ path: "/search-results", query: searchCriteria });
    },
  },
};
</script>

<style>
.search {
  display: flex;
}
.search select {
  padding: 0;
}
nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: rgb(0, 65, 134);
  color: #fff;
  text-align: center;
  padding: 0 100px;
}

nav h1 a {
  font-size: 2.2rem;
  color: #fff;
  text-decoration: none;
}

.search-box input {
  padding: 5px;
  margin: 5px;
}
.search-box #search-input {
  border-radius: 6px;
  max-height: 40px;
  font-size: 0.9rem;
  font-weight: 400;
  color: black;
}
.search-box #button {
  border-radius: 6px;
  max-height: 40px;
  font-size: 0.9rem;
  font-weight: 500;
}
.search-box #button {
  background-color: #007bff;
  color: white;
  padding: 5px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.search-box #button:hover {
  background-color: #003cff;
}

@media only screen and (max-width: 550px) {
  nav {
    flex-direction: column;
    padding: 10px 0;
  }

  nav .search-box {
    margin-left: 30px;
  }

  .bookSection h2 {
    font-size: 20px;
  }
}
</style>
