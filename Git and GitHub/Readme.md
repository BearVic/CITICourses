# Git and GitHub

----
reference:[Version Control with Git](http://swcarpentry.github.io/git-novice/)  

## Git Basic

This part include git init, tracking changes, exploring history, commit changes and remove file in git repository.

````
git init  //cd to a dir and runing code to create a git

//git configuration
git config --global user.name "name"
git config --global user.email "@.com"
git config --global color.ui "auto"

git config --list  //list configurations

git status  //tracking changes
git add mars.txt  //adding a file to staging area
git commit -m "First commit."  //commit file from staging area to repository with description(required)

git checkout -- "mars.txt"  //discard changes
git diff  //review changes
git log  //commit log

//review difference from history version
git diff HEAD mars.txt
git diff HEAD~1 mars.txt

//show history version
git show HEAD~3 mars.txt
git show HEAD~3:mars.txt

//rollback to history version
git checkout HEAD~3 mars.txt

//rm file from repository
git rm jupiter.txt
git commit -m "delete jupiter.txt"

````

## GitIgnore

````
mkdir results
touch a.dat b.dat c.dat results/a.out results/b.out

vim .gitignore

--INSERT--
*.dat
results/
:wq

git add .gitignore
git commit -m "Add the ignore file"

````

## Remote Repository from GitHub

### Working with Remote Repository

````
git remote add origin https://github.com/BearVic/planets.git
git remote
git remote -v
git push origin master
````

### Collaborate with Other People

- Host: Settings -> Collaborators -> add username(partner)
- Partner: verify invitation
- Partner: start to work with the project(see codes below)
- Host: ``git pull origin master``


````
git clone https://github.com/wumetal/planets24

git branch

git branch experimental  //new branch
git checkout experimental  //switch branch

git merge experimental
//confilct dealing: above "======" is what this branch got, below is the merging one.
    after alter the conflict, do git add <file>, then git commit w/o any comments.

git branch -d experimental  //delete branch
````

## Pull Request

working with others in GitHub

- visit others' repository which you want to work with
- fork it and you would see it in your own page
- git clone the one in your own page
- start to work(push and pull)


## Work Flow in Git
working area{mars.txt} --add-->staging area{mars.txt}--commit-->repository