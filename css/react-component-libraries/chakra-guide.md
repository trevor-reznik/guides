# Chakra UI
. 

## Setup

1. bootstrap the example page

```bash
npx create-next-app --example with-chakra-ui $NAME_FRONTEND
# or
yarn create next-app --example with-chakra-ui $NAME
```

2. run

```bash
cd $NAME_FRONTEND
npm run dev
xdg-open http://localhost:3000
```

3. carve/create `index.js`

```bash
code src/pages/index.js
```

```javascript
import { Text, Divider } from '@chakra-ui/react'

const Index = () => <Text>Hello World</Text>;

export default Index
```

4. convert to typescript

```bash
cd src/pages
mv index.js index.tsx
mv _app.js _app.tsx
mv ../theme.js ../theme.tsx
.....
```

5. remove components

```bash
cd src
rm components/$UNWANTED
```

6. add components from website


```bash
xdg-open https://chakra-ui.com/docs/getting-started

xdg-open https://chakra-ui.com/docs/features/style-props

xdg-open https://chakra-ui.com/docs/form/form-control
xdg-open https://chakra-ui.com/docs/data-display/divider
xdg-open https://chakra-ui.com/docs/media-and-icons/avatar
...
```




