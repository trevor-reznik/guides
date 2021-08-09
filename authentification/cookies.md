# Cookies

### Setting Cookies with Express

[Guide](https://stackoverflow.com/questions/46288437/set-cookies-for-cross-origin-requests)

##### Backend

- Put cookieparser before authentificaiotn middleware
- Pass middleware function in all routes. Middleware sets headers to not allow wildcards etc. (hover over CORS errors if necessary)
- Then pass the authentication middleware that validate s cookies
- `secure`: `true` 
- `sameSite`: `"none”`

```typescript
  login = (req: Request, res: Response) => {
    res.setHeader("Access-Control-Allow-Origin", "http://localhost:5000")
    res.setHeader("Access-Control-Allow-Credentials", "true")
    res.setHeader("Access-Control-Allow-Headers", "application/x-www-form-urlencoded; charset=UTF-8")
    res.cookie(
      "key", sessionKey.toString(),
      { maxAge: 200000,
        domain: ".app.localhost",
        secure: true,
        sameSite: "none"
     }
```

##### Frontend

[Guide](https://stackoverflow.com/questions/46288437/set-cookies-for-cross-origin-requests)

- [Setting withCredentials Options](https://api.jquery.com/jquery.ajax/) so that the browser can set a cookie sent in the response object

```javascript
ajaxOptions = 
    xhrFields: {
    withCredentials: true
    }
```

[On localhost](https://stackoverflow.com/questions/1134290/cookies-on-localhost-with-explicit-domain/1188145#1188145)



