import React, { ChangeEvent, useState, useContext, FormEvent } from "react";
import { AuthContext } from "../../context/AuthContext";

const RegisterPage = () => {
  const [email, setEmail] = useState<string>("");
  const [username, setUsername] = useState<string>("");
  const [fullName, setFullName] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [password2, setPassword2] = useState<string>("");

  const authCxt = useContext(AuthContext);

  const submitForm = (e: FormEvent) => {
    e.preventDefault();
    authCxt.signup(email, username, fullName, password);
  };

  return (
    <div>
      <form action="" onSubmit={submitForm}>
        <div>
          <label>Email</label>
          <input
            type="email"
            value={email}
            onChange={(e: ChangeEvent<HTMLInputElement>) =>
              setEmail(e.target.value)
            }
          />
        </div>
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
          <label>Full Name</label>
          <input
            type="text"
            value={fullName}
            onChange={(e: ChangeEvent<HTMLInputElement>) =>
              setFullName(e.target.value)
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
          <label>Confirm Password</label>
          <input
            type="password"
            value={password2}
            onChange={(e: ChangeEvent<HTMLInputElement>) =>
              setPassword2(e.target.value)
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

export default RegisterPage;
