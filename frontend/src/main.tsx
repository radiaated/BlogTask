import React from "react";
import ReactDOM from "react-dom/client";

import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./index.css";
import HomePage from "./pages/home/HomePage";
import RegisterPage from "./pages/register/RegisterPage";
import LoginPage from "./pages/login/LoginPage";
import Layout from "./layout/Layout";
import AuthContextProvider from "./context/AuthContext";

const router = createBrowserRouter([
  {
    path: "/",
    element: (
      <AuthContextProvider>
        <Layout />
      </AuthContextProvider>
    ),
    children: [
      {
        index: true,
        element: <HomePage />,
      },
      {
        path: "signup",
        element: <RegisterPage />,
      },
      {
        path: "login",
        element: <LoginPage />,
      },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <RouterProvider router={router} />
);
