import React, { ChangeEvent, useState, FormEvent, useContext } from "react";
import { AuthContext } from "../../context/AuthContext";

const LoginPage = () => {
  const [username, setUsername] = useState<string>("");

  const [password, setPassword] = useState<string>("");
  const authCxt = useContext(AuthContext);
  const submitForm = (e: FormEvent) => {
    e.preventDefault();
    authCxt.login(username, password);
  };
  return (
    <div>
      <form action="" onSubmit={submitForm}>
        <div>
          <label>Username</label>
          <input
            type="username"
            value={username}
            onChange={(e: ChangeEvent<HTMLInputElement>) =>
              setUsername(e.target.value)
            }
          />
        </div>
        <div>
          <label>Password</label>
          <input
            type="password"
            value={password}
            onChange={(e: ChangeEvent<HTMLInputElement>) =>
              setPassword(e.target.value)
            }
          />
        </div>

        <div>
          <input type="submit" value="Login" />
        </div>
      </form>
    </div>
  );
};

export default LoginPage;
