
## Abridged


```shell
git add .; git commit -m $msg; git push
```

```shell
info git-[push|commit|add|] | grep $KEYWORD

info git

man [-k] git-$KEYWORD
```


## New Repo
```shell
cd $PROJECT_NAME

git init

touch .gitinogre

git add .

git commit -m $MSG
```


Create repo @ github.com/new


```shell
git remote add origin git@github.com:username/repo_name.git

git remote add origin https://github.com/username/new_repo

git push -u origin master
```


## Cloning


##### Basic


1. Get link for HTTP, GitHubCLI, or SSH
2. cd to preferred DL location
3. $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY


## Repairing


if only the local repo is corrupted, and you know the url to the remote, you can use this to re-set your .git to match the remote (replacing ${url} with the remote url):


```bash
mv -v .git .git_old &&            # remove old git
git init &&                       # initialise new repo
git remote add origin "${url}" && # link to old repo
git fetch &&                      # get old history
git reset origin/master --mixed   # force update to old history
```

This leaves your working tree intact, and only affects git's bookkeeping.