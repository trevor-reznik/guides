


###### Create Github Pages Branch in Project

**In separate folder**

```bash
cd /path/to/repo-name
git symbolic-ref HEAD refs/heads/gh-pages
rm .git/index
git clean -fdx
echo "My GitHub Page" > index.html
git add .
git commit -a -m "First pages commit"
git push origin gh-pages
```

Why do we need to do all this, instead of just calling git branch gh-pages. Well, if you are at master and you do git branch gh-pages, gh-pages will be based off master.

Here, the intention is to create a branch for github pages, which is typically not associated with the history of your repo (master and other branches) and hence the usage of git symbolic-ref. This creates a "root branch", which is one without a previous history.

Note that it is also called an orphan branch and git checkout --orphan will now do the same thing as the git symbolic-ref that was being done before. Check out this question on SO2 as well.

###### Create PAges

go to pages branch -> settings -> pages

initiate pages 

###### Upload files

upload CSS files and assets with correct reference links

###### link to the page from the Pages website base URL (not from repo path)

*Example*: https://trevor-reznik.github.io/guides/custom-fonts/bymyself-fonts.css
