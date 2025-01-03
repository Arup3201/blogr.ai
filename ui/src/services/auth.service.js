import { post } from "./service";

const Auth = {
  login: (data = {}) => {
    return post("api/auth/login", data);
  },
  googleLogin: (data = {}) => {
    return post("api/auth/google-login", data);
  },
  signup: (data = {}) => {
    return post("api/auth/signup", data);
  },
  googleSignup: (data = {}) => {
    return post("api/auth/google-signup", data);
  },
};

export { Auth };
