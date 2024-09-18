<template>
  <div class="wrapper">
    <div v-if="message" class="success-message">{{ message }}</div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div class="input-box">
        <input
          type="text"
          placeholder="Enter your username"
          v-model="username"
          required
        />
      </div>
      <div class="input-box">
        <input
          type="password"
          placeholder="Password"
          v-model="password"
          required
        />
      </div>
      <div class="input-box button">
        <input type="submit" value="Sign In" />
      </div>
      <p class="alert" style="text-align: center" v-if="error">{{ error }}</p>
      <div class="text">
        <h3 style="color: rgb(0, 92, 190)">
          Don't have an account?
          <a
            href="/register"
            style="text-decoration: none; color: rgb(0, 92, 190)"
            >Register now</a
          >
        </h3>
      </div>
      <div class="text">
        <h2>
          To Login as Admin
          <a
            href="http://localhost:8080/admin-login"
            style="text-decoration: none; color: #fff"
            >Click Here</a
          >
        </h2>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      password: "",
      message: null,
      error: null,
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post(
          "https://booknest-m2z6.onrender.com/api/users/login",
          {
            username: this.username,
            password: this.password,
          },
          {
            withCredentials: true, // Include credentials with the request
          }
        );
        console.log(response.data);
        this.$router.push("/home"); // Redirect to the home page
      } catch (error) {
        if (error.response) {
          this.error = error.response.data.error;
        } else {
          this.error = "An error occurred";
        }
      }
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

.alert {
  padding: 20px;
  background-color: #f44336;
  color: white;
  opacity: 1;
  transition: opacity 0.6s;
  margin-bottom: 15px;
}

.wrapper {
  background: #fff;
  margin-left: 100px;
  padding: 10px;
  position: relative;
  width: 30%;
  height: 50%;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  border-radius: 12px;
}

.wrapper h2 {
  text-align: center;
  color: #fff;
  background: rgb(0, 92, 190);
  border-radius: 4px;
}

.wrapper form {
  margin-top: 25px;
}

.wrapper form .input-box {
  height: 52px;
  margin: 18px;
}

form .input-box input {
  height: 100%;
  width: 100%;
  padding: 0 15px;
  border: 1.5px solid black;
  border-bottom-width: 2.5px;
  border-radius: 6px;
  font-size: 17px;
  font-weight: 400;
  color: #333;
  transition: all 0.5s ease;
}

.input-box input:focus,
.input-box input:valid {
  border-color: #4070f4;
}

.input-box.button input {
  color: #fff;
  background: rgb(46, 131, 222);
}

.input-box.button input:hover {
  background: rgb(0, 92, 190);
}

.text {
  padding: 10px 0px;
  text-align: center;
}

#logo {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: linear-gradient(to right, lightblue, rgb(0, 92, 190));
  width: 440px;
}
</style>
