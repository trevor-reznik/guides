# New TS Project

1. npm init

```bash
npm init -y
vim package.json
npm install $DEPENDENCIES
``` 

2. install typescript

```bash
npm install typescript
npm install --save @types/node   # type definitions for Node.js
npx tsconfig.json                # typescript config file somehow
```

3. ts-node testing 

```bash
# ts-node test
npm install ts-node
vim package.json
  "scripts": {
    "start": "ts-node src/index.ts"
  },

mkdir src
touch src/index.ts
npm start                        # runs src/index.ts

# watch mode
vim package.json
  "scripts": {
    "watch" : "tsc -w",
npm run watch                    # compiles src/index.ts to js -> create dist folder with index.js
```

4. start scripts

```bash
# new terminal
node dist/index.js               # executes js code in index.js
vim package.json
  "scripts": {
    "watch" : "tsc -w",
    "start" : "node dist/index.js",
    "start2": "ts-node src/index.ts"
  },
# start2 runs ts-node on typscript file
# start runs node on js file
# watch compiles live
```

5. nodemon

```bash
vim package.json 
  "scripts": {
    "dev" : "nodemon dist/index.js",
npm install nodemon              # listens for any changes to file and reruns file

# nodemon with ts
vim package.json 
  "scripts": {
    "dev2" : "nodemon --exec ts-node src/index.ts",   # live with ts instead

npm run dev                      # runs live-updating that re-executes on save file
```

- **Terminal 1** (npm run watch) -> live compiling changes to ts file to index.js
- **Terminal 2** (npm run dev) -> re-running index.js on changes