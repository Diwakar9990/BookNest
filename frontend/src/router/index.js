import { createRouter, createWebHistory } from "vue-router";
import LoginView from "../views/LoginView.vue";
import RegisterView from "../views/RegisterView.vue";
import MyBooks from "../views/MyBooks.vue";
import BookDetails from "../views/BookDetails.vue";
import UserRequests from "../views/UserRequests.vue";
import AdminView from "../views/AdminView.vue";
import AdminHome from "../views/AdminHome.vue";
import SectionView from "../views/SectionView.vue";
import AddSection from "../views/AddSection.vue";
import UpdateSection from "../views/UpdateSection.vue";
import AddBook from "../views/AddBook.vue";
import AllBooks from "../views/AllBooks.vue";
import UpdateBook from "../views/UpdateBook.vue";
import AdminRequests from "@/views/AdminRequests.vue";
import HomeView from "@/views/HomeView.vue";
import BookSection from "@/views/BookSection.vue";
import AcceptedRequest from "@/views/AcceptedRequest.vue";
import SearchResult from "@/views/SearchResult.vue";
import UserDetails from "@/views/UserDetails.vue";

const routes = [
  {
    path: "/",
    name: "login",
    component: LoginView,
  },
  {
    path: "/search-results",
    name: "searchResult",
    component: SearchResult,
  },
  {
    path: "/admin-login",
    name: "adminlogin",
    component: AdminView,
  },
  {
    path: "/admin-home",
    name: "adminhome",
    component: AdminHome,
  },
  {
    path: "/register",
    name: "register",
    component: RegisterView,
  },
  {
    path: "/my-books",
    name: "myBooks",
    component: MyBooks,
  },
  {
    path: "/home",
    name: "homeView",
    component: HomeView,
  },
  {
    path: "/user-details",
    name: "userDetails",
    component: UserDetails,
  },
  {
    path: "/sections",
    name: "bookSections",
    component: BookSection,
  },
  {
    path: "/books/:id",
    name: "bookDetails",
    component: BookDetails,
    props: true,
  },
  {
    path: "/user-requests",
    name: "userRequests",
    component: UserRequests,
  },
  {
    path: "/admin/sections",
    name: "sectionView",
    component: SectionView,
  },
  {
    path: "/add-section",
    name: "addSection",
    component: AddSection,
  },
  {
    path: "/add-book",
    name: "addBook",
    component: AddBook,
  },
  {
    path: "/admin/books",
    name: "allBooks",
    component: AllBooks,
  },
  {
    path: "/admin/pending-requests",
    name: "pendingRequests",
    component: AdminRequests,
  },
  {
    path: "/admin/accepted-requests",
    name: "acceptedRequests",
    component: AcceptedRequest,
  },
  {
    path: "/update-section/:id",
    name: "updateSection",
    component: UpdateSection,
    props: true,
  },
  {
    path: "/update-book/:id",
    name: "updateBook",
    component: UpdateBook,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
