<template>
  <div>
    <NavBar />
    <SideBar />
    <div class="book-details-block" v-if="book">
      <div class="book">
        <div id="book-image">img</div>
        <div class="book-details">
          <h2>Title : {{ book.title }}</h2>
          <h2>Author : {{ book.author }}</h2>
          <h2>Section : {{ book.section_id }}</h2>
          <h2 v-if="rating">Average Rating : {{ rating }}</h2>
          <h2 v-if="msg">Average Rating : {{ msg }}</h2>
          <h2 v-if="count">Reviews : {{ count }}</h2>
          <div class="rating">
            <button type="button" class="button-6" @click="downloadBook">
              Download
            </button>
            <button
              type="button"
              class="button-6"
              @click="showRatingForm = true"
            >
              Rate Now
            </button>
          </div>
        </div>
      </div>
      <div class="desc">
        <h1>Description</h1>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit.
          Reprehenderit ducimus, libero at labore expedita id, impedit,
          obcaecati animi rerum aliquid odit quo quis voluptatem. Nostrum sit,
          corrupti iste repellendus vitae aliquam deserunt amet quae! Nam ipsa
          vitae assumenda, eveniet earum nobis debitis ducimus asperiores
          numquam autem quaerat repellat cumque, vero facilis consequuntur
          recusandae natus deleniti accusantium tempora nostrum unde. Quisquam
          pariatur rerum impedit, in sunt aspernatur. Mollitia, reprehenderit?
          Sit non minima eius quas praesentium labore animi repudiandae deleniti
          laudantium unde ducimus in quasi explicabo soluta temporibus sunt nemo
          odio quibusdam architecto incidunt natus, consectetur possimus sed.
          Corrupti est consequatur dolor.
        </p>
      </div>
      <RatingForm
        v-if="showRatingForm"
        :bookId="book.id"
        @rating-submitted="handleRatingSubmitted"
        @cancel="showRatingForm = false"
      />
      <div class="ratings-section">
        <h2>Ratings and Reviews</h2>
        <div v-if="ratings.length">
          <div v-for="rating in ratings" :key="rating.id" class="rating-item">
            <p><strong>User Id:</strong> {{ rating.user_id }}</p>
            <p><strong>Rating:</strong> {{ rating.rating }} / 5</p>
            <p><strong>Feedback:</strong> {{ rating.feedback }}</p>
          </div>
        </div>
        <div v-else>
          <p>Be the first one to rate this book.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SideBar from "../components/layout/SideBar.vue";
import NavBar from "../components/layout/NavBar.vue";
import RatingForm from "../components/user/RatingForm.vue";
import axios from "axios";
export default {
  name: "BookDetails",
  props: ["id"],
  data() {
    return {
      book: null,
      error: null,
      msg: null,
      rating: null,
      count: null,
      ratings: [],
      showRatingForm: false,
    };
  },
  components: {
    SideBar,
    NavBar,
    RatingForm,
  },
  created() {
    this.fetchBooks();
    this.fetchRatings();
  },

  methods: {
    async fetchBooks() {
      try {
        const response = await axios.get(
          "http://localhost:5000/api/books/" + this.id,
          {
            withCredentials: true,
          }
        );
        const response2 = await axios.get(
          "http://localhost:5000/api/ratings/average/" + this.id,
          {
            withCredentials: true,
          }
        );
        console.log(response.data);
        console.log(response2.data);
        this.book = await response.data.res;
        this.rating = await response2.data.rating;
        this.count = await response2.data.ratingCount;
        this.msg = await response2.data.msg;
      } catch (error) {
        if (error.response) {
          console.log(error.response.data);
          this.msg = error.response.data.msg;
        } else {
          this.error = "An error occurred while fetching books";
        }
      }
    },
    async fetchRatings() {
      try {
        const response = await axios.get(
          "http://localhost:5000/api/ratings/" + this.id,
          {
            withCredentials: true,
          }
        );
        this.ratings = await response.data.res;
      } catch (error) {
        if (error.response) {
          console.log(error.response.data);
          this.error = error.response.data.msg;
        } else {
          this.error = "An error occurred while fetching ratings";
        }
      }
    },
    downloadBook() {
      const fileUrl = `http://localhost:5000/api/books/download/${this.book.ebook_url}`;
      window.open(fileUrl);
    },
    handleRatingSubmitted(data) {
      console.log("Rating Submitted:", data);
      this.showRatingForm = false;
      this.fetchBooks(); // Refresh book details after rating
      this.fetchRatings(); // Refresh ratings after rating
    },
  },
};
</script>

<style>
.book-details-block {
  padding: 0.2rem 0.5rem 0.5rem 1rem;
  margin: 1rem 1rem 1rem 5rem;
}
.book-details-block .desc {
  padding: 10px;
  color: #fff;
  margin: 0 50px 50px 50px;
  background: rgb(0, 65, 134);
}
.book {
  display: flex;
}
#book-image {
  align-content: center;
  color: #fff;
  text-align: center;
  height: 250px;
  width: 180px;
  background: rgb(0, 65, 134);
  border: 2px solid black;
  margin: 50px 20px 20px 50px;
}
.book-details {
  margin: 50px 0 0 0;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  height: 250px;
  background: rgb(0, 65, 134);
}
.book-details h1,
h2 {
  color: #fff;
  text-align: left;
  margin: 0;
}
.rating {
  padding: 5px 0 0 0;
}
.rating button {
  margin: 0 10px;
}
.button-6 {
  align-items: center;
  background-color: #ffffff;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 0.25rem;
  box-shadow: rgba(0, 0, 0, 0.02) 0 1px 3px 0;
  box-sizing: border-box;
  color: rgba(0, 0, 0, 0.85);
  cursor: pointer;
  display: inline-flex;
  font-family: system-ui, -apple-system, system-ui, "Helvetica Neue", Helvetica,
    Arial, sans-serif;
  font-size: 16px;
  font-weight: 600;
  justify-content: center;
  line-height: 1.25;
  margin: 0;
  min-height: 2rem;
  padding: calc(0.875rem - 1px) calc(1.5rem - 1px);
  position: relative;
  text-decoration: none;
  transition: all 250ms;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: baseline;
  width: auto;
}
.button-6:hover,
.button-6:focus {
  border-color: rgba(0, 0, 0, 0.15);
  box-shadow: rgba(0, 0, 0, 0.1) 0 4px 12px;
  color: rgba(0, 0, 0, 0.65);
}
.button-6:hover {
  transform: translateY(-1px);
}
.button-6:active {
  background-color: #f0f0f1;
  border-color: rgba(0, 0, 0, 0.15);
  box-shadow: rgba(0, 0, 0, 0.06) 0 2px 4px;
  color: rgba(0, 0, 0, 0.65);
  transform: translateY(0);
}
.error {
  color: rgb(0, 65, 134);
}
.ratings-section {
  margin: 1rem 0 0 3.5rem;
}

.rating-item {
  color: rgb(13, 30, 49);
  border-bottom: 1px solid #ddd;
  padding: 0.5rem 0;
}
</style>
