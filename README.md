<p align="center">
  <img width="460" height="400" src="https://github.com/geekquad/AlgoBook/blob/master/project/Readme_Images/icon.png">
</p>
A beginner friendly project to help you in various open source contributions. An attempt to bring all the algorithms together.

## Overview

The goal of this project is to help the beginners with their contributions in Open Source and bring all the possible algorithms of Machine Learning and Python together. We aim to achieve this collaboratively, so feel free to contribute in any way you want, just make sure to follow the contribution guidelines.
<p> **For now, this repo is focused on the beginner frienldy contributions in Hacktoberfest 2020.** </p>

## What is Open - Soruce?
Open-source software is a type of computer software in which source code is released under a license in which the copyright holder grants users the rights to use, study, change, and distribute the software to anyone and for any purpose. Open-source software may be developed in a collaborative public manner.

Read more about it <a href="https://www.digitalocean.com/community/tutorial_series/an-introduction-to-open-source"> here. </a>

## Hactoberfest2020

<img src="https://github.com/geekquad/AlgoBook/blob/master/project/Readme_Images/header.png">
Hacktoberfest is a month-long celebration of open source software presented by Digital Ocean, Intel and DEV. Hacktoberfest is open to everyone in our global community!

### Let's Get Started:

### Step 1. Register to Hacktoberfest 2020
##### Link to register: https://hacktoberfest.digitalocean.com/

<img src="https://github.com/geekquad/AlgoBook/blob/master/project/Readme_Images/start.JPG">

### Step 2. Create a Copy of this Repository
In order to work on an open-source project, you will first need to make your own copy of the repository. To do this, you should fork the repository and then clone it so that you have a local working copy.

> **Fork :fork_and_knife: this repo. Click on the Fork button at the top right corner.**

With the repository forked, you’re ready to clone it so that you have a local working copy of the code base.

> **Clone the Repository**

To make your own local copy of the repository you would like to contribute to, let’s first open up a terminal window.

We’ll use the git clone command along with the URL that points to your fork of the repository.

* Open the Command Prompt
* Copy the url of the forked repository.
* Type this command:


```
git clone https://github.com/your_username/AlgoBook
```

<img src="https://github.com/geekquad/AlgoBook/blob/master/project/Readme_Images/clone_cmd.JPG">



### Step 3: Creating a New Branch
it is important to branch the repository so that you are able to manage the workflow, isolate your code, and control what features make it back to the main branch of the project repository.

When creating a branch, it is very important that you create your new branch off of the master branch. 
**To create our branch, from our terminal window, follow:**

```
git branch new-branch
git checkout new-branch
```
Once you enter the git checkout command, you will receive the following output:

```
Switched to branch 'new-branch'
```


### Step 4: Contribute
Make relevant changes. Add new algorithms. Add Readme files. Contribute in any way you feel like :)

### Step 5: Commiting and Pushing:
Once you have modified an existing file or added a new file to the project, you can add it to your local repository, which we can do with the git add command.

``` git add filename``` or ``` git add .``` 

You can type the command ```git add -A``` or alternatively ```git add -all``` for all new files to be staged.

**With our file staged, we’ll want to record the changes that we made to the repository with the ```git commit``` command.**
<p> The commit message is an important aspect of your code contribution; it helps the other contributors fully understand the change you have made, why you made it, and how significant it is.  </p>
 
 ```
 git commit -m "commit message"
 ```
 **Once you have saved and exited the commit message text file, you can verify what git will be committing with the following command:**
 
 ```
 git status
 ```
 
 At this point you can use the ```git push``` command to push the changes to the current branch of your forked repository:
 ```
 git push --set-upstream origin new-branch
 ```
 
 ### Step 6: Sync the Fork
Once we have configured a remote that references the upstream and original repository on GitHub, we are ready to sync our fork of the repository to keep it up-to-date.

To sync our fork, from the directory of our local repository in a terminal window, we’ll use the ```git fetch``` command to fetch the branches along with their respective commits from the upstream repository. Since we used the shortname “upstream” to refer to the upstream repository, we’ll pass that to the command:

```
git fetch upstream
```

### Step 7: Create Pull Request
At this point, you are ready to make a pull request to the original repository.

You should navigate to your forked repository, and press the “New pull request” button on your left-hand side of the page. 

GitHub will alert you that you are able to merge the two branches because there is no competing code. You should add in a **title**, a **comment**, and then press the **“Create pull request”** button.


 
























