<template>
  <div class="sidebar">
    <div class="sidebar-header">
      <img
        src="../../assets/booknest-favicon-white.png"
        height="50px"
        width="50px"
      />
    </div>
    <ul class="sidebar-links">
      <h4>
        <span> Main Menu </span>
        <div class="menu-seprator"></div>
      </h4>
      <li>
        <a href="http://localhost:8080/admin-home">
          <span class="material-symbols-outlined"> Dashboard </span> Dashboard
        </a>
      </li>
      <li>
        <a href="http://localhost:8080/admin/books">
          <span class="material-symbols-outlined"> Book </span> All books
        </a>
      </li>
      <li>
        <a href="http://localhost:8080/admin/sections">
          <span class="material-symbols-outlined"> Menu </span> Sections
        </a>
      </li>
      <li>
        <a href="http://localhost:8080/admin/pending-requests">
          <span class="material-symbols-outlined"> Label </span> Pending
          Requests
        </a>
      </li>
      <li>
        <a href="http://localhost:8080/admin/accepted-requests">
          <span class="material-symbols-outlined"> Task </span> Requests Granted
        </a>
      </li>
      <h4>
        <span> Library </span>
        <div class="menu-seprator"></div>
      </h4>
      <li>
        <a href="http://localhost:8080/add-book">
          <span class="material-symbols-outlined"> Edit </span> Add Books
        </a>
      </li>
      <li>
        <a href="http://localhost:8080/add-section">
          <span class="material-symbols-outlined"> Add </span> Add Sections
        </a>
      </li>
      <h4>
        <span> Account </span>
        <div class="menu-seprator"></div>
      </h4>
      <li>
        <a @click.prevent="logout">
          <span class="material-symbols-outlined"> Logout </span> Logout
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SideBar",
  methods: {
    async logout() {
      try {
        const response = await axios.post(
          "https://booknest-m2z6.onrender.com/api/users/logout",
          {},
          {
            withCredentials: true,
          }
        );
        if (response.data.logout) {
          this.$router.push("/");
        }
      } catch (error) {
        console.error("An error occurred during logout:", error);
        // Optionally handle the error, e.g., show a notification to the user
      }
    },
  },
};
</script>

<style>
.sidebar {
  z-index: 2;
  position: fixed;
  display: flex;
  flex-direction: column;
  overflow-x: hidden;
  top: 0;
  left: 0;
  height: 100%;
  width: 80px;
  background: linear-gradient(to right, rgb(15, 126, 164), rgb(0, 65, 134));
  box-shadow: 0 5px 30px rgba(0, 0, 0, 0.4);
  padding: 20px 10px;
  transition: all 0.4s ease;
}

.sidebar:hover {
  width: 250px;
}

.sidebar-links h4 span {
  opacity: 0;
  margin-left: 18px;
}

.sidebar:hover .sidebar-links h4 span {
  opacity: 1;
  margin-left: 18px;
}

.sidebar .sidebar-header {
  margin-left: 6px;
  display: flex;
}

.sidebar .sidebar-header h1 {
  margin-left: 12px;
  color: #fff;
}

.sidebar-links {
  list-style: none;
  margin-top: 10px;
  height: 90%;
  overflow-y: auto;
  scrollbar-width: none;
}

.sidebar-links .menu-seprator {
  position: absolute;
  left: 0;
  top: 50%;
  width: 100%;
  height: 1px;
  transform: scaleX(1);
  transform: translateY(-50%);
  background: rgb(65, 132, 203);
}

.sidebar:hover .sidebar-links .menu-seprator {
  transition-delay: 0s;
  transform: scaleX(0);
}

.sidebar-links h4 {
  position: relative;
  font-size: 1.1rem;
  color: #fff;
  font-weight: 600;
  margin: 10px 0;
  white-space: nowrap;
}

.sidebar-links li {
  display: flex;
  padding: 5px 10px;
}

.sidebar-links li a {
  display: "flex";
  font-size: 90%;
  flex-direction: column;
  align-items: center;
  gap: 0% 20%;
  font-weight: 500;
  white-space: nowrap;
  text-decoration: none;
  padding: 3px 7px;
  color: #d5d5d5;
  cursor: pointer;
}

span.material-symbols-outlined {
  margin-right: 20px;
  display: inline;
}

.sidebar-links li a span {
  padding: 4px;
  margin: 0px 0px;
}

.sidebar-links li a:hover {
  color: #fff;
  background: rgb(105, 155, 209);
  border-radius: 4px;
}
</style>
