<template>
  <div class="container">
    <nav>
      <h1><a href="/admin-home">BookNest</a></h1>
    </nav>
  </div>
</template>

<script>
export default {
  name: "AdminNav",
};
</script>

<style>
nav {
  display: flex;
  align-items: center;
  justify-content: space-between; /* Center the content horizontally */
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

@media only screen and (max-width: 550px) {
  nav {
    flex-direction: column;
    padding: 10px 0;
  }
}
</style>
