Title: Local .gitignore
Date: 2020-01-09 08:25
Category: Git
Tags: git, cli
Authors: Eric Rochow

There may be cases where you want to locally ignore a file or directory that is normally tracked by git. An example of this may be built docs. If you add the object to `.gitignore`, the ignore will be pushed to the remote repo. To ignore a file or directory, add the file/directory to `.git/info/exclude` with the same syntax as .gitignore.

For example, to ignore the `docs/` directory you can do the following:
```
# echo "docs/" | tee -a .git/info/exclude
```
If the `docs/` directory is already being tracked by git, you will need to update the index to apply the ignore:
```
# git update-index --assume-unchanged docs/
```
Now we can test to make sure the ignore works:
```
# touch docs/test.html
# git status
  On branch master
  Your branch is up to date with 'origin/master'.
   nothing to commit, working tree clean
```
Success!
