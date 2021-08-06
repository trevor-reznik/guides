
# Importing/Exporting Types

- [Importing/Exporting](#import)
  - [classes](#classes)
- [Ways to Import/Export](#types)
- [Notes](#notes)


<a name="import"/>

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

4. Choose export stategy. E.g, Declare passive module export and change eache type/interface declaration to an export statement

```typescript
declare module "apparel" {
  export interface ItemColors {
    colors: string[];
    weights: number[];
  }
}
```

or 

```typescript
// types/server.d.ts
import ExpressServer from "./../server";

export interface DBConfig {
  name: string;
  port: number;
  modelNames: string[];
}
```


5. Import in main ts file by using `.`+`Enter` while hovering over type references (or do manually).


```typescript
import { ItemColors } from "apparel";

const x : ItemColors = {
    ...
}
```

<a name="classes"/>

### Classes

One Option
1. move the interface that it typing the class to the `d.ts` file
2. create a new interface above the class declaration  in main that extends that imported interface

Another Option
1. Move the types/interfaces and class declaration into another normal `ts` file in `src`
2. export the class into main as the default export. 

----------------

###### Example

```typescript
// options.d.ts
import multer from "multer";
import ExcelParser from "./../excel-parser";
import Database from "./../database";
import ExpressServer from "./../server";

interface DBConfig {
  DBname: string;
  DBport: number;
  modelNames: string[];
}

interface VerboseConfig {
  log: boolean;
  verboseGap: string;
  alert: (title: string, objects?: any[]) => void;
}

export interface App extends DBConfig, VerboseConfig {
  mediaDir: string;
  db: Database;
  upload: multer.Multer;
  middleware: any[];
  http: ExpressServer;
  sessionKeys: {
    [key: string]: [number, number];
  };
  csvImporter: ExcelParser;
}
```

```typescript
// index.ts
import { App } from "options";

interface Apparel extends App {
  sessionKeys: {
    [key: string]: [number, number];
  };
}

class Apparel {
  constructor(options: App | any) {
    const config = {
      port: __prod__ ? 80 : 5000,
      ip: __prod__ ? "143.198.57.139" : "127.0.0.1",
      mediaDir: `${__dirname}/../public_html/img/user-data`,
      middleware: [],
      log: true,
    }
  }
}
```




<a name="types"/>

https://www.typescriptlang.org/docs/handbook/modules.html

[Importing Types](https://www.typescriptlang.org/docs/handbook/modules.html#importing-types)


[Export all as](https://www.typescriptlang.org/docs/handbook/modules.html#export-all-as-x)

[Ambient Modules](https://www.typescriptlang.org/docs/handbook/modules.html#ambient-modules)

In Node.js, most tasks are accomplished by loading one or more modules. We could define each module in its own .d.ts file with top-level export declarations, but it’s more convenient to write them as one larger .d.ts file. 

To do so, we use a construct similar to ambient namespaces, but we use the module keyword and the quoted name of the module which will be available to a later import. For example:

###### node.d.ts (simplified excerpt)

```typescript
declare module "url" {
  export interface Url {
    protocol?: string;
    hostname?: string;
    pathname?: string;
  }
  export function parse(
    urlStr: string,
    parseQueryString?,
    slashesDenoteHost?
  ): Url;
}
declare module "path" {
  export function normalize(p: string): string;
  export function join(...paths: any[]): string;
  export var sep: string;
}
```

Now we can `/// <reference>` `node.d.ts` and then load the modules using `import url = require("url");` or `import * as URL from "url"`.

```typescript
/// <reference path="node.d.ts"/>
import * as URL from "url";
let myUrl = URL.parse("http://www.typescriptlang.org");
```


##### [Guidance for Structuring Modules](https://www.typescriptlang.org/docs/handbook/modules.html#guidance-for-structuring-modules)

----------


<a name="notes"/>

*Notes*

Go to `node_modules` >> `@types` >> `$MODULENAME` to view the type definitions there and also how the type .d.ts files are formatted generally.