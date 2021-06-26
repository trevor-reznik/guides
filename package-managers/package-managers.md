
<a name="table-of-contents"/>

# Package Managers

###### Table of Contents

### [***npm***](#npm)
- [summary](#npm-summary)
- [functional characteristics](#npm-characteristics)
- [usage](#npm-usage)
- [tips and advanced usage](#npm-tips)

### [***yarn***](#yarn)
- [summary](#yarn-summary)
- [functional characteristics](#yarn-characteristics)
- [usage](#yarn-usage)
- [tips and advanced usage](#yarn-tips)

### [***pip***](#pip)
- [summary](#pip-summary)
- [functional characteristics](#pip-characteristics)
- [usage](#pip-usage)
- [tips and advanced usage](#pip-tips)



--------------------




<a name="npm"/>

## npm



<a name="npm-summary"/>

##### Summary

##### History

<a name="npm-characteristics"/>

##### Functional Characteristics

<a name="npm-usage"/>

##### Usage

###### install [docs](https://docs.npmjs.com/cli/install)




<a name="npm-tips"/>

##### Tips




<a name="yarn"/>

## yarn


<a name="yarn-summary"/>

##### Summary

JavaScript package manager

Yarn is only a new CLI client that fetches modules from the npm registry.


##### History


Its purpose is to solve a handful of problems that these teams faced with npm, namely:
- installing packages wasn’t fast/consistent enough, and
- there were security concerns, as npm allows packages to run code on installation.

<a name="yarn-characteristics"/>

##### Functional Characteristics

###### yarn.lock 
In an ideal world of semantic versioning, patched releases won’t include any breaking changes. This, unfortunately, is not always true. The strategy employed by npm may result into two machines with the same package.json file, having different versions of a package installed, possibly introducing bugs.

To avoid package version mis-matches, an exact installed version is pinned down in a lock file. Every time a module is added, Yarn creates (or updates) a yarn.lock file. This way you can guarantee another machine installs the exact same package, while still having a range of allowed versions defined in package.json.

In npm, the npm shrinkwrap command generates a lock file as well, and npm install reads that file before reading package.json, much like how Yarn reads yarn.lock first. The important difference here is that Yarn always creates and updates yarn.lock, while npm doesn’t create one by default and only updates npm-shrinkwrap.json when it exists.


###### Parallel Installation
Whenever Yarn or npm needs to install a package, it carries out a series of tasks. In npm, these tasks are executed per package and sequentially, meaning it will wait for a package to be fully installed before moving on to the next. Yarn executes these tasks in parallel, increasing performance.


###### Cleaner Output
By default npm is very verbose. For example, it recursively lists all installed packages when running npm install <package>. Yarn on the other hand, isn’t verbose at all. When details can be obtained via other commands, it lists significantly less information with appropriate emojis (unless you’re on Windows).

<a name="yarn-usage"/>

##### Usage

###### global
Unlike npm, where global operations are performed using the -g or --global flag, Yarn commands need to be prefixed with global. Just like npm, project-specific dependencies shouldn’t need to be installed globally.

The global prefix only works for yarn add, yarn bin, yarn ls and yarn remove. With the exception of yarn add, these commands are identical to their npm equivalent.

###### install [docs](https://yarnpkg.com/en/docs/cli/install)

The npm install command will install dependencies from the package.json file and allows you to add new packages. yarn install only installs the dependencies listed in yarn.lock or package.json, in that order.

###### yarn licenses [ls|generate-disclaimer]
At the time of writing, no npm equivalent is available. yarn licenses ls lists the licenses of all installed packages. yarn licenses generate-disclaimer generates a disclaimer containing the contents of all licenses of all packages. Some licenses state that you must include the project’s license in your project, making this a rather useful tool to do that.

- [yarn licenses documentation](https://yarnpkg.com/en/docs/cli/licenses)

###### yarn why
This command peeks into the dependency graph and figures out why given package is installed in your project. Perhaps you explicitly added it, perhaps it’s a dependency of a package you installed. `yarn why` helps you figure that out.

- [yarn why documentation](https://yarnpkg.com/en/docs/cli/why)

###### yarn upgrade [package]
This command upgrades packages to the latest version conforming to the version rules set in `package.json` and recreates `yarn.lock`. This is similar to `npm update`.

Interestingly, when specifying a package, it updates that package to latest release and updates the tag defined in `package.json`. This means this command might update packages to a new major release.

- [yarn upgrade documentation](https://yarnpkg.com/en/docs/cli/upgrade)

######  yarn generate-lock-entry
The `yarn generate-lock-entry` command generates a `yarn.lock` file based on the dependencies set in `package.json`. This is similar to `npm shrinkwrap`. This command should be used with caution, as the lock file is generated and updated automatically when adding and upgrading dependencies via `yarn add` and `yarn upgrade`.

- [yarn generate-lock-entry documentation](https://yarnpkg.com/en/docs/cli/generate-lock-entry)
- [npm shrinkwrap documentation](https://yarnpkg.com/en/docs/cli/generate-lock-entry)



<a name="yarn-tips"/>

##### Tips




<a name="pip"/>

## pip




<a name="pip-summary"/>

##### Summary

##### History

<a name="pip-characteristics"/>

##### Functional Characteristics

<a name="pip-usage"/>

##### Usage

<a name="pip-tips"/>

##### Tips