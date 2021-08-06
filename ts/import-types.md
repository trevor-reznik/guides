
# Importing/Exporting Types

1. Set baseURL option in `tsconfig.json`

```json
    "baseUrl": "./",
```

```json
    "baseUrl": "src",
```

2. Set the location of your types in the paths property.

```json
    "paths": {
      "types": ["types"],
      "store": ["store"],
      "*": [
          "node_modules/*",
          "src/types/*" // this will make the typescript compiler find the type file
      ]
    }
  },
```

3. Make types file

```bash
mkdir src/types
touch src/types/index.d.ts
```

4. Declare and export types

```typescript
declare module "apparel" {
  export interface ItemColors {
    colors: string[];
    weights: number[];
  }
}
```


5. Import in main ts file by using `.`+`Enter` while hovering over type references (or do manually).


```typescript
import { ItemColors } from "apparel";

const x : ItemColors = {
    ...
}
```

----------


*Notes*

Go to `node_modules` >> `@types` >> `$MODULENAME` to view the type definitions there and also how the type .d.ts files are formatted generally.