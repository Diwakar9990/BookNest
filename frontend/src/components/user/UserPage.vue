<template>
  <div class="user-page">
    <h1>User Details</h1>
    <div v-if="user" class="user-details">
      <h2><strong>Username:</strong> {{ user.username }}</h2>
      <h2><strong>Email:</strong> {{ user.email }}</h2>
      <!-- Add other user details as needed -->
    </div>
    <div v-else>
      <p>Loading user details...</p>
    </div>

    <h2>Book Request Details</h2>
    <div v-if="requests" class="cards">
      <div class="card">
        <p><strong>Total Requests:</strong></p>
        <p class="number">{{ requests.total_request }}</p>
      </div>
      <div class="card">
        <p><strong>Pending Requests:</strong></p>
        <p class="number">{{ requests.pending_request }}</p>
      </div>
      <div class="card">
        <p><strong>Accepted Requests:</strong></p>
        <p class="number">{{ requests.accepted_request }}</p>
      </div>
      <div class="card">
        <p><strong>Rejected Requests:</strong></p>
        <p class="number">{{ requests.rejected_request }}</p>
      </div>
    </div>
    <div v-else>
      <p>Loading request details...</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "UserPage",

  data() {
    return {
      user: null,
      requests: null,
      error: null,
    };
  },
  created() {
    this.fetchUserDetails();
    this.fetchUserRequests();
  },
  methods: {
    async fetchUserDetails() {
      try {
        const response = await axios.get(
          "https://booknest-m2z6.onrender.com/api/users/details",
          { withCredentials: true }
        );
        this.user = response.data.res;
      } catch (error) {
        console.error("Error fetching user details:", error);
        this.error = "Failed to load user details.";
        alert(this.error);
      }
    },
    async fetchUserRequests() {
      try {
        const response = await axios.get(
          "https://booknest-m2z6.onrender.com/api/requests/user-request-details",
          { withCredentials: true }
        );
        this.requests = response.data.result;
      } catch (error) {
        console.error("Error fetching user requests:", error);
        this.error = "Failed to load request details.";
      }
    },
  },
};
</script>

<style scoped>
.user-page {
  padding: 20px;
}

.user-page h1,
.user-page h2 {
  color: rgb(0, 65, 134);
}

.user-page p {
  font-size: 16px;
}

.user-page .loading {
  font-size: 18px;
  color: rgb(0, 65, 134);
}

.cards {
  display: flex;
  gap: 20px;
  margin-top: 20px;
}

.card {
  background-color: rgb(0, 65, 134);
  color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  flex: 1;
  text-align: center;
}

.card p {
  margin: 0;
  font-size: 1.2rem;
}

.card .number {
  font-size: 4rem;
}
</style>
