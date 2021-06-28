
# Express


<a name="setup"/>

## Setup

1. install

```bash
npm install express  
npm install @types/express
```

2. import
```typescript
import express from "express"
```

3. construct

```typescript
const app = express();
```

4. set endpoints

```typescript
app.get("/", (req, res) => {

})
```

5. listen

```typescript
app.listen(4000, () => {

});
```

<a name="usage"/>

## Usage