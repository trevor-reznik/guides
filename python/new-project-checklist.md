# New Python Project


### Git

```bash
mkdir $PROJECT
cd $PROJECT
git init
touch README.md
touch .gitignore
echo $STUFF > .gitignore
```
github.com/new

```bash
git remote add origin git@github.com:username/repo_name.git
git remote add origin https://github.com/username/new_repo

git add .
git commit -m "init"
git push -u origin master
```

### Virtual Environment

```bash
python -m venv env
```

### Dependencies

```bash
touch requirements.txt
pip3 install $DEPENDENCIES
echo "$DEPENDENCIES" >> requirements.txt
```