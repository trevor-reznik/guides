
# React



<a name="new-project"/>

## New Project



<a name="template-snippet"/>

#### Template Snippet

```typescript
import React from 'react'

interface nameProps {
    
}

export const Name: React.FC<nameProps> = ({}) => {
    return <div>hello world</div>;
}
```

Next.js

```typescript
import React from 'react'

interface nameProps {

}

const Name: React.FC<nameProps> = ({}) => {
    return ();
}

export default Name
```




------------------------------------------------------


<a name="pages"/>

## Pages

.

.

<a name="Formik"/>

### Formik

```bash
npm -i formik react
```

```typescript
import React from "react";
import { Form, Formik } from "formik";

interface registerProps {}

const Register: React.FC<registerProps> = ({}) => {
  return (
    <Formik
      initialValues={{ username: "", password: "" }}
      onSubmit={(values) => {
        console.log(values);
      }}
    >
      {() => (
        <Form>
          <div>hello world</div>
        </Form>
      )}
    </Formik>
  );
};

export default Register;
```

##### Chakra.ui Example

[Chakra formik form control docs](https://chakra-ui.com/docs/form/form-control)

```typescript
import React from "react";
import { Form, Formik } from "formik";
import {
  FormControl,
  FormLabel,
  FormErrorMessage,
  FormHelperText,
  Input,
} from "@chakra-ui/react";
import { Wrapper } from "../components/Wrapper";

interface registerProps {}

const Register: React.FC<registerProps> = ({}) => {
  return (
    <Wrapper variant="small">
      <Formik
        initialValues={{ username: "", password: "" }}
        onSubmit={(values) => {
          console.log(values);
        }}
      >
        {({ values, handleChange }) => (
          <Form>
            <FormControl>
              <FormLabel htmlFor="username">Username</FormLabel>
              <Input
                value={values.username}
                onChange={handleChange}
                id="name"
                placeholder="username"
              />
              {/* <FormErrorMessage>{form.errors.name}</FormErrorMessage> */}
            </FormControl>
          </Form>
        )}
      </Formik>
    </Wrapper>
  );
};

export default Register;
```


<a name="variants"/>

## Variants

```typescript
import React from "react";

interface WrapperProps {
    variant?: "small" | "regular";
}

export const Wrapper: React.FC<WrapperProps> = ({ children, variant = "regular", }) => {
  return (
    <Box mt={8} mx="auto" maxW={ variant === "regular" ? "800px" : "400px"} w="100%">
      {children}
    </Box>
  );
};
```

```typescript
const Register: React.FC<registerProps> = ({}) => {
  return (
    <Wrapper variant="small">
```