import React from "react";
import axios from "axios";
import { createContext } from "react";
import { useNavigate } from "react-router-dom";

type typeAuthCxt = {
  signup: (
    email: string,
    username: string,
    fullName: string,
    password: string
  ) => Promise<void>;
  login: (username: string, password: string) => Promise<void>;
};

type typeAuthCxtProvider = {
  children: React.ReactNode;
};

export const AuthContext = createContext<typeAuthCxt>({} as typeAuthCxt);

const AuthContextProvider = ({ children }: typeAuthCxtProvider) => {
  const navigate = useNavigate();

  const signup = async (
    email: string,
    username: string,
    fullName: string,
    password: string
  ): Promise<void> => {
    axios({
      url: `${import.meta.env.VITE_API_URL}/auth/register/`,
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      data: {
        email: email,
        username: username,
        first_name: fullName,
        password: password,
      },
    }).then((res) => {
      navigate("/login");
    });
  };

  const login = async (username: string, password: string): Promise<void> => {
    axios({
      url: `${import.meta.env.VITE_API_URL}/auth/token/`,
      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },
      data: {
        username: username,
        password: password,
      },
      withCredentials: true,
    }).then((res) => {
    //   navigate("/");
    });
  };

  const value = {
    login,
    signup,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export default AuthContextProvider;
