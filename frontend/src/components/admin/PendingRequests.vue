<template>
  <div>
    <h4 class="error" v-if="error">
      Please <a href="http://localhost:8080/"> Login </a> as Admin to Continue
    </h4>
    <div v-if="requests.length">
      <div class="requests-list-block" v-if="requests.length">
        <h2>{{ message }}</h2>
        <p id="status">{{ status }}</p>
        <table>
          <thead>
            <tr>
              <th>Request ID</th>
              <th>Name</th>
              <th>Book ID</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody v-for="request in requests" :key="request.id">
            <td>{{ request.id }}</td>
            <td>{{ request.username }}</td>
            <td>{{ request.book_id }}</td>
            <td>{{ request.status }}</td>
            <td>
              <button class="btn" @click="updateRequest(request.id, 'approve')">
                Accept
              </button>
            </td>
            <td>
              <button class="btn" @click="updateRequest(request.id, 'reject')">
                Reject
              </button>
            </td>
          </tbody>
        </table>
      </div>
      <h4 v-else>No requests found</h4>
    </div>
    <div class="error" v-else>
      <h4 v-if="msg">No pending requests</h4>
      <h4 v-else>Loading...</h4>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "PendingRequests",
  data() {
    return {
      requests: [],
      error: null,
      message: "",
      status: "",
      msg: "",
    };
  },
  created() {
    this.fetchPendingRequests();
  },
  methods: {
    async fetchPendingRequests() {
      try {
        const response = await axios.get(
          "https://booknest-m2z6.onrender.com/api/requests/get-pending-requests",
          {
            withCredentials: true,
          }
        );
        this.requests = response.data.res;
        this.message = response.data.message;
      } catch (error) {
        if (error.response) {
          error.response.data.msg === "No pending requests"
            ? (this.msg = error.response.data.msg)
            : (this.error = error.response.data.msg);
        } else {
          this.error = "An error occurred while fetching requests";
        }
      }
    },
    async updateRequest(id, action) {
      try {
        const response = await axios.put(
          `https://booknest-m2z6.onrender.com/api/requests/update/${id}`,
          { action: action },
          {
            withCredentials: true,
          }
        );
        this.status = response.data.message;
        this.fetchPendingRequests(); // Refresh the list after updating
      } catch (error) {
        if (error.response) {
          this.error = error.response.data.error;
        } else {
          this.error = "An error occurred while updating the request";
        }
      }
    },
  },
};
</script>

<style>
.requests-list-block {
  padding: 1rem;
  margin: 1rem;
  background: rgb(0, 65, 134);
}
.requests-list-block h2 {
  color: #ffffff;
  padding: 1rem;
}
.requests-list-block table {
  border: 2px solid rgb(245, 245, 245);
  box-shadow: 0 5px 10px rgba(255, 255, 255, 0.2);
  margin: 0 20px;
}
.requests-list-block table th,
td {
  list-style-type: none;
  text-align: center;
  color: #ffffff;
  padding: 20px 50px;
}
.requests-list-block li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem 10px;
  border-bottom: 1px solid #ccc;
}
.requests-list-block h3 {
  margin: 0px 12px;
  width: 250px;
}
.requests-list-block p {
  margin: 0.5rem 0 0 0;
}
.error {
  height: 400px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: rgb(0, 65, 134);
}

#status {
  text-align: center;
  color: rgb(255, 255, 255);
  padding: 10px;
}
.error a {
  margin: 0 6px;
}
</style>
