<template>
  <div class="rating-form">
    <h3>Rate this book</h3>
    <form @submit.prevent="submitRating">
      <div>
        <label for="rate">Rating (1 to 5):</label>
        <input type="number" v-model="rate" min="1" max="5" required />
      </div>
      <div>
        <label for="feedback">Feedback:</label>
        <textarea v-model="feedback" required></textarea>
      </div>
      <button type="submit" class="button-6">Submit</button>
      <button type="button" class="button-6" @click="$emit('cancel')">
        Cancel
      </button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "RatingForm",
  props: ["bookId"],
  data() {
    return {
      rate: null,
      feedback: "",
      error: null,
    };
  },
  methods: {
    async submitRating() {
      try {
        const response = await axios.post(
          `http://localhost:5000/api/ratings/${this.bookId}`,
          { rate: this.rate, feedback: this.feedback },
          { withCredentials: true }
        );
        this.$emit("rating-submitted", response.data);
      } catch (error) {
        if (error.response) {
          this.error = error.response.data.msg;
          alert(this.error);
        } else {
          this.error = "An error occurred while submitting your rating";
        }
      }
    },
  },
};
</script>

<style>
.rating-form {
  padding: 1rem 3rem;
  background: rgb(0, 65, 134);
  border-radius: 8px;
  margin: 1rem 0;
}
.rating-form h3 {
  margin-bottom: 1rem;
  color: #fff;
}
.rating-form label {
  display: block;
  margin-bottom: 0.5rem;
  color: #fff;
}
.rating-form input,
.rating-form textarea {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;

  border: 1px solid #ccc;
  border-radius: 4px;
}

.rating-form button {
  margin-right: 1rem;
}

.error {
  color: red;
}
</style>
