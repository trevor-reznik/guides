
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


<a name="session"/>

## Express-Session

##### Step 1

redis stores kv 

`sess:safdsafewrwsad` -> `{ userId: 32 }`

##### Step 2

`Express-Session` sets cookie on browser as a signed version of key in kv pair


e.g., `sdaf2349dfsa@3edsa`

##### Step 3

cookie id send to server on req

##### Step 4

server decrypts cookie using secret to get unsigned key 

##### Step 5

req sent to redis using the decrypted key -> receive corresponding value

##### Step 6

on every request, getting key for kv pair and accessing it again

##### Step 7

any user data that won't change you can store in session obj and it will persist as long as cookie is not cleared.

For data that is variable, you can store the id and then reference database.