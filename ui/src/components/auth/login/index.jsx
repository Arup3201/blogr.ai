import { Card } from "../../widgets/card";
import Logo from "../../../assets/logo.png";
import { Field } from "../../widgets/field";
import { Form } from "../../widgets/form";
import { Button } from "../../widgets/button";
import { Input, Password } from "../../widgets/input";
import { Auth } from "../../../services/auth.service";

/*
Best UX Practices for LogIn and Signup: https://medium.com/@fiona.chiaraviglio/best-practices-for-login-sign-up-from-a-ux-perspective-e5d14b6ffce0

Provide login using Google and Apple
Email Validation
Password Hide Button
*/

function Login() {
  function handleLogin(event) {
    event.preventDefault();

    const fd = new FormData(event.target);

    const data = Object.fromEntries(fd.entries());
    Auth.login(data)
      .then((res) => console.log(res))
      .catch((err) => console.log(err));
  }

  return (
    <Card>
      <img src={Logo} className="mx-auto w-12" />
      <p className="text-lg font-bold text-gray-900">
        Welcome Back To Blogr, Resume Your Journey With Us
      </p>
      <Form onSubmit={handleLogin}>
        <Field label="Email" htmlFor="email">
          <Input
            id="email"
            type="email"
            name="email"
            placeholder="me@example.com"
          />
        </Field>
        <Field label="Password" htmlFor="password">
          <Password
            id="password"
            name="password"
            rules={[
              {
                message: "Password is required",
                type: "required",
              },
            ]}
          />
        </Field>
        <Button type="submit">Login</Button>
      </Form>
    </Card>
  );
}

export default Login;
