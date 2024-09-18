<template>
  <div>
    <h4 class="error" v-if="error">
      {{ error }}
    </h4>
    <div v-if="books.length">
      <div class="book-section-block" v-if="books">
        <h2 style="color: #fff">My Books</h2>
        <div class="book-section">
          <div class="books" v-for="book in books" :key="book.id">
            <div class="img">img</div>
            <div class="book-detail">
              <h3>Title : {{ book.title }}</h3>
              <h3>Author : {{ book.author }}</h3>
              <button>
                <router-link
                  :to="{ name: 'bookDetails', params: { id: book.id } }"
                  >More Info</router-link
                >
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import axios from "axios";
export default {
  name: "BookCard",
  data() {
    return {
      books: [],
      message: null,
      error: null,
      msg: null,
    };
  },
  created() {
    this.fetchBooks();
  },
  methods: {
    async fetchBooks() {
      try {
        const response = await axios.get("https://booknest-m2z6.onrender.com/api/books/request-status-accepted", {
          withCredentials: true,
        });
        console.log(response.data);
        this.books = response.data.res;
        this.message = response.data.message;
        this.msg = response.data.msg;
      } catch (error) {
        if (error.response) {
          console.log(error.response.data.msg);
          this.error = error.response.data.msg;
        } else {
          this.error = "An error occurred while fetching books";
        }
      }
    },
  },
};
</script>

<style>
.book-section-block {
  padding: 0.5rem 0.5rem 0.5rem 1rem;
  margin: 1rem 1rem 1rem 3rem;
}
.book-section-block h2 {
  text-align: center;
  margin-bottom: 20px;
  background: rgb(0, 65, 134);
  color: rgb(0, 49, 101);
}

.book-section{
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  padding: 0 80px;
}
.books{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 1rem 0rem;
  padding: 0.4rem;
  border-radius: 4px;
}
.books .img{
  color:#fff;
  height: 230px;
  width: 170px;
  text-align: center;
  align-content: center;
  border-radius: 10px;
  background: rgb(0, 65, 134);
}
.books .book-detail{
  margin: 10px;
  padding: 6px; 
  display: flex;
  flex-direction: column;
  align-items: center;
  background: rgb(0, 65, 134);
  border-radius: 10px;
}
.books h3{
  font-size: 1rem;
  font-weight: 400;
  color:  #fff;
  padding:0 0.2rem;
}
.books button{
  background: rgb(255, 255, 255);
  border-radius: 10px;
  
}
.books button a{
  margin: 1rem;
  font-size: 1rem;
  text-decoration: none;
  border-radius: 5px;
  color:rgb(0, 65, 134);
}
.error {
  text-align: center;
  color: rgb(0, 35, 71);
  font-size: 2rem;
  margin-left: 100px;
}
.error a {
  color: #fff;
  text-decoration: none;
}

.books #moreInfo {
  font-size: 1rem;
  border-radius: 5px;
}
</style>
