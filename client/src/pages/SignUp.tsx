import { Button } from "@radix-ui/themes";
import { Formik, Form, Field, FormikHelpers } from "formik";
import { toast } from "react-toastify";
interface IValues{
  username: string,
  password: string,
  email: string
}
function SignUp() {
  return (
    <>

      <main className="flex flex-col items-center p-5">
        <h1 className="text-3xl">Create an account</h1>
        <Formik
          initialValues={{ email: "", password: "", username: "" }}
          onSubmit={(
            values: IValues,
            { setSubmitting }: FormikHelpers<IValues>
          ) => {
            setTimeout(() => {
              alert(JSON.stringify(values, null, 2));
              setSubmitting(false);
              toast(`Welcome ${values.username} 🎉`);
            }, 500);
          }}
        >
          <Form className="bg-zinc-700/10 outline outline-1 outline-slate-500/60 rounded-lg flex flex-col p-3 items-center min-w-96">
            <span className="flex flex-col p-2">
              <label htmlFor="email">Email:</label>
              <Field
                className="outline outline-1 outline-slate-300/40 rounded-md bg-zinc-700/40 w-min"
                type="email"
                id="email"
                name="email"
                required
                aria-required="true"
                aria-label="Enter your email address"
              />
            </span>
            <span className="flex flex-col">
              <label htmlFor="username">Username:</label>
              <Field
                className="outline outline-1 outline-slate-300/40 rounded-md bg-zinc-700/40 w-min"
                type="text"
                id="username"
                name="username"
                required
                aria-required="true"
                aria-label="Enter your desired username"
              />
            </span>

            <span className="flex flex-col">
              <label htmlFor="password">Password:</label>
              <Field
                className="outline outline-1 outline-slate-300/40 rounded-md bg-zinc-700/40 w-min"
                type="password"
                id="password"
                name="password"
                required
                aria-required="true"
                aria-label="Enter a strong password"
              />
            </span>
            <span className="mt-5">
              <Button variant="surface" type="submit" size="2">
                Sign Up
              </Button>
            </span>
          </Form>
        </Formik>
      </main>
    </>
  );
}
export default SignUp;
