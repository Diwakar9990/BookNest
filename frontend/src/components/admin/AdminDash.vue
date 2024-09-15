<template>
  <div>
    <h4 class="error" v-if="error">
      {{ error }} Please <a href="http://localhost:8080/"> Login </a> as Admin
      to Continue
    </h4>

    <div v-else class="dashboard">
      <h1>Dashboard</h1>
      <div class="cards">
        <div class="card">
          <h3>Total Books</h3>
          <p>{{ stats.total_books }}</p>
        </div>
        <div class="card">
          <h3>Total Users</h3>
          <p>{{ stats.total_users }}</p>
        </div>
        <div class="card">
          <h3>Total Sections</h3>
          <p>{{ stats.total_sections }}</p>
        </div>
        <div class="card">
          <h3>Total Requests</h3>
          <p>{{ stats.total_requests }}</p>
        </div>
        <div class="card">
          <h3>Pending Requests</h3>
          <p>{{ stats.pending_requests }}</p>
        </div>
        <div class="card">
          <h3>Accepted Requests</h3>
          <p>{{ stats.accepted_requests }}</p>
        </div>
        <div class="card">
          <h3>Rejected Requests</h3>
          <p>{{ stats.rejected_requests }}</p>
        </div>
        <div class="card">
          <h3>Revoked Requests</h3>
          <p>{{ stats.rejected_requests }}</p>
        </div>
      </div>
      <div class="charts">
        <div id="booksBySectionChart"></div>
        <div id="mostRatedBooksChart"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Plotly from "plotly.js-dist";

export default {
  name: "AdminDash",
  data() {
    return {
      stats: {},
      booksBySection: { labels: [], counts: [] },
      mostRatedBooks: { titles: [], counts: [] },
      error: null,
    };
  },
  created() {
    this.fetchStats();
    this.fetchBooksBySection();
    this.fetchMostRatedBooks();
  },
  methods: {
    async fetchStats() {
      try {
        const response = await axios.get(
          "http://localhost:5000/api/books/stats",
          {
            withCredentials: true,
          }
        );
        this.stats = response.data;
      } catch (error) {
        this.error = error.response.data.msg;
        console.error("Error fetching stats:", error.response);
      }
    },
    async fetchBooksBySection() {
      try {
        const response = await axios.get(
          "http://localhost:5000/api/books/section_counts",
          {
            withCredentials: true,
          }
        );
        this.booksBySection = response.data.res;
        this.plotBooksBySection();
      } catch (error) {
        console.error("Error fetching books by section:", error.response);
      }
    },
    async fetchMostRatedBooks() {
      try {
        const response = await axios.get(
          "http://localhost:5000/api/books/most_rated",
          {
            withCredentials: true,
          }
        );
        this.mostRatedBooks = response.data.res;
        this.plotMostRatedBooks();
      } catch (error) {
        console.error("Error fetching most-rated books:", error.response);
      }
    },
    plotBooksBySection() {
      const data = [
        {
          type: "pie",
          values: this.booksBySection.counts,
          labels: this.booksBySection.labels,
          textinfo: "label+percent",
          textposition: "outside",
          automargin: true,
        },
      ];

      const layout = {
        title: "Books by Section",
        height: 400,
        width: 500,
      };

      Plotly.newPlot("booksBySectionChart", data, layout);
    },
    plotMostRatedBooks() {
      const data = [
        {
          type: "bar",
          x: this.mostRatedBooks.titles,
          y: this.mostRatedBooks.counts,
          marker: {
            color: "rgb(0, 65, 134)",
          },
        },
      ];

      const layout = {
        title: "Most Rated Books",
        height: 400,
        width: 500,
      };

      Plotly.newPlot("mostRatedBooksChart", data, layout);
    },
  },
};
</script>

<style>
.dashboard {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

.dashboard h1 {
  color: rgb(0, 65, 134);
}

.cards {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-bottom: 20px;
}

.card {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: rgb(0, 65, 134);
  color: white;
  font-size: 1rem;
  padding: 20px;
  margin: 30px 40px;
  border-radius: 10px;
  width: 200px;
  text-align: center;
}

.card p {
  font-size: 5rem;
}
.charts {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}

#booksBySectionChart,
#mostRatedBooksChart {
  margin: 20px;
}
</style>
