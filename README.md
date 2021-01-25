# ![Algo-Book-poster.png](https://github.com/geekquad/AlgoBook/blob/master/project/Readme_Images/icon2.PNG)
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
 
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  ![first-timers-only](https://img.shields.io/badge/first--timers--only-friendly-yellow.svg?style=flat) ![contributions welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square) ![](https://img.shields.io/github/repo-size/geekquad/AlgoBook.svg?label=Repo%20size&style=flat-square)&nbsp;![GitHub contributors](https://img.shields.io/github/contributors-anon/geekquad/AlgoBook) ![Maintenance](https://img.shields.io/maintenance/yes/2021) ![GitHub forks](https://img.shields.io/github/forks/geekquad/AlgoBook?style=social) ![GitHub Repo stars](https://img.shields.io/github/stars/geekquad/AlgoBook?style=social) 
</p>
A beginner friendly project to help you in open source contributions. An attempt to bring all the algorithms together. 


**Please see the <a href="https://github.com/geekquad/AlgoBook/blob/master/CONTRIBUTING.md"> **Contributing Guidelines** </a>.**


## Overview

The goal of this project is to help the beginners with their contributions in Open Source and bring all the possible algorithms of Machine Learning and Python together. We aim to achieve this collaboratively, so feel free to contribute in any way you want, just make sure to follow the contribution guidelines.


## What is Open - Source? [![Open Source Love svg3](https://badges.frapsoft.com/os/v3/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
The open source community provides a great opportunity for aspiring programmers to distinguish themselves; and by contributing to various projects, developers can improve their skills and get inspiration and support from like-minded people. When you contribute to something you already know and love, it can have so much more meaning, because you know how the tool is used and the good it does for you. Being part of an open source community opens you up to a broader range of people to interact with. 

Read more about it <a href="https://www.digitalocean.com/community/tutorial_series/an-introduction-to-open-source"> here. </a>


## <u> Let's Get Started: </u>

### Step 1. Create a Copy of this Repository
In order to work on an open-source project, you will first need to make your own copy of the repository. To do this, you should fork the repository and then clone it so that you have a local working copy.

> **Fork :fork_and_knife: this repo. Click on the Fork button at the top right corner.**

With the repository forked, you’re ready to clone it so that you have a local working copy of the code base.

> **Clone the Repository**

To make your own local copy of the repository you would like to contribute to, let’s first open up a terminal window.

We’ll use the git clone command along with the URL that points to your fork of the repository.

* Open the Command Prompt
* Type this command:

```
git clone https://github.com/your_username/AlgoBook
```

<img src="https://github.com/geekquad/AlgoBook/blob/master/project/Readme_Images/clone_cmd.JPG">



### Step 2: Creating a New Branch
It is important to branch the repository so that you are able to manage the workflow, isolate your code, and control what features make it back to the main branch of the project repository.

When creating a branch, it is very important that you create your new branch off of the master branch. 
**To create a new branch, from your terminal window, follow:**


```
git branch new-branch
git checkout new-branch
```
Once you enter the git checkout command, you will receive the following output:

```
Switched to branch 'new-branch'
```


### Step 3: Contribute
Make relevant changes. Add new algorithms. Add Readme files. Contribute in any way you feel like :)

### Step 4: Commiting and Pushing:
Once you have modified an existing file or added a new file to the project, you can add it to your local repository, which we can do with the git add command.

``` git add filename``` or ``` git add .``` 

You can type the command ```git add -A``` or alternatively ```git add -all``` for all new files to be staged.


**With our file staged, we’ll want to record the changes that we made to the repository with the ```git commit``` command.**
<p> The commit message is an important aspect of your code contribution; it helps the other contributors fully understand the change you have made, why you made it, and how significant it is.  </p>
 
 ```
 git commit -m "commit message"
 ```
 
 
 At this point you can use the ```git push``` command to push the changes to the current branch of your forked repository:
 ```
 git push --set-upstream origin new-branch
 ```
 
### Step 6: Create Pull Request
At this point, you are ready to make a pull request to the original repository.

You should navigate to your **forked** repository, and press the “Compare & pull request” button on the page. 
<img src="https://github.com/geekquad/AlgoBook/blob/master/project/Readme_Images/pr.JPG">

GitHub will alert you that you are able to merge the two branches because there is no competing code. You should add in a **title**, a **comment**, and then press the **“Create pull request”** button.

<img src="https://github.com/geekquad/AlgoBook/blob/master/project/Readme_Images/create%20pr.JPG">

### Step 7: CONGRATULATIONS :boom: :clap: :relaxed:
You have made it till the end. Kudos to you!!

<hr> </hr>

## Contents

Our content is basically divided into 5 segments for now. Please create an issue if you wish to add code in a language that we don't currently have here. 

* <a href="https://github.com/geekquad/AlgoBook/tree/master/python"> Python</a>
* <a href="https://github.com/geekquad/AlgoBook/tree/master/ml"> ML</a>
* <a href="https://github.com/geekquad/AlgoBook/tree/master/dl"> DL</a>
* <a href="https://github.com/geekquad/AlgoBook/tree/master/cpp"> cpp </a>
* [go](https://github.com/geekquad/AlgoBook/tree/master/go)
 
### Where to upload the files

* Your files should be uploaded directly into the corresponding folder (For instance, if you wrote code for an Algorithm Implementation in Python, it goes inside the Python folder and same goes for the ML Algorithm)
* **Under no circumstances create new folders within the language folders to upload your code unless specifically told to do so.**

#### For any more issues and queries, please join our <a href="https://join.slack.com/t/geekquad/shared_invite/zt-jtdqxt2r-i9R7vvNPzveImCBBM~eahw"> Slack Channel. </a>
Feel free to reach out to us. Rememeber, collaboration is the key to open-source. 

#### Please see the <a href="https://github.com/geekquad/AlgoBook/blob/master/CONTRIBUTING.md"> **Contributing Guidelines** </a>.

<hr> </hr>

## Please STAR :star2: this repository if you liked it and had fun :)

### Maintainers! :blush:

<table>
  <tbody><tr>
    <td align="center"><a href="https://github.com/geekquad"><img alt="" src="https://avatars.githubusercontent.com/geekquad" width="100px;"><br><sub><b>Aditya Kumar Gupta</b></sub></a><br><a href="https://github.com/geekquad/AlgoBook/commits?author=geekquad" title="Code">💻 🖋</a></td> </a></td>
    <td align="center"><a href="https://github.com/major-beast"><img alt="" src="https://avatars.githubusercontent.com/major-beast" width="100px;"><br><sub><b>Paurush Tiwari</b></sub></a><br><a href="https://github.com/geekquad/AlgoBook/commits?author=major-beast" title="Code">💻 🖋</a></td></a></td>
  </tr>
</tbody></table>

## Community

Join our [Slack community](https://join.slack.com/t/geekquad/shared_invite/zt-l3t67zvr-JMKbn57PpxjEi7uC2k0etg) to get help in contributing, as well as stay up-to-date on issues and best practices.

As always, thanks to our amazing contributors!

<a href="https://github.com/geekquad/AlgoBook/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=geekquad/AlgoBook" />
</a>

## Stargazers over time

[![Stargazers over time](https://starchart.cc/geekquad/AlgoBook.svg)](https://starchart.cc/geekquad/AlgoBook)



