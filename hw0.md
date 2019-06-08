---
layout: default
img: hopper_univac 
img_link: "https://en.wikipedia.org/wiki/Grace_Hopper"
caption: "Grace Hopper developed the first compiler for a computer programming language."
title: Homework | Setup
active_tab: homework
---

# Homework Setup

<p class="text-muted">Start on {{ site.hwdates[0].startdate }}</p>
<p class="text-muted">Due on {{ site.hwdates[0].deadline }}</p>

Your task for this homework is to setup your gitlab repository and
get used to the routine we will be using in this course. This
homework will have the following steps:

* set up your [gitlab repository](http://gitlab.cs.sfu.ca) for the course
* get the homework files to get started on your homework, 
* to write your solution for each homework, 
* to test your solution, and 
* to submit your homework solution for grading.

## Getting Started

### Set up your repository

Go to [the SFU Gitlab server](http://gitlab.cs.sfu.ca){:target="_blank"} which is on the web at [gitlab.cs.sfu.ca](http://gitlab.cs.sfu.ca){:target="_blank"}.
Log in with your SFU username and password, the same one you use to check your
e-mail on SFU Mail. For the rest of this page we will refer to your SFU username 
as `YOUR_USERNAME`.

Once logged in, you will see a list of your existing repos. You may
have some from previous courses or you may have none right now, so
let's create one for CMPT379 by clicking the `New Project` button
at the top right of the page.

On the `New Project` page, give your repo a name to the right of
the `Project name` field. Name your repo: `CMPT379-{{ site.semcode }}-YOUR_USERNAME`

It's important to name the repo exactly as you see here. Leave all
other settings as they are and click the `Create Project`
button at the bottom left of the page.

Make sure you do not change the default setting of
`Private`. Your repo must be visible only to yourself.
In other words, no other student can access it by default.
**You must not give access to your repo to any other students - plagiarism is a serious
academic offense, which applies as much to code as it
does to essays and exams.**

Your repo has now been created. You will be taken to a web page for
your newly created repo.

### Add instructor and TAs to your repository

The course instructor needs access to your repository in order to view
code. Add the instructor as a member of your
repo by clicking on the Settings menu which looks like a gear icon <i class="fa fa-gear"></i>
and selecting `Members` from the dropdown menu. On the page that loads up
type in `{{ site.instructor }}` {% for ta in site.tas %} and `{{ ta.email }}` {% endfor %}
 in the `Add new user` box and then change the role permissions from
`Guest` to `Developer` in the dropdown menu. Click on `Add to Project` to add
the instructor and the TAs to your gitlab project for this course. 

**This step is crucial. If you do not provide Developer access to
the instructor and the TAs you will earn zero marks for your
homeworks.**

### Set up SSH keys on gitlab

Next we will set up the Secure Shell (ssh) keys so you can access
your repo without a password. First follow [the instructions on
setting up your SSH key pair](https://csil-git1.cs.surrey.sfu.ca/help/ssh/README)
available at [csil-git1.cs.surrey.sfu.ca/help/ssh/README](https://csil-git1.cs.surrey.sfu.ca/help/ssh/README).
Follow the instructions for Linux.

Now we have to copy your public key to the GitLab server.
The [instructions](https://csil-git1.cs.surrey.sfu.ca/help/ssh/README) ask
you to use `xclip` which may not be installed on all the CSIL machines.
If you cannot find `xclip` ("Command not found") then do the
following steps.

If you have set up your SSH key correctly then you will have a public key. View it

    cat ~/.ssh/id_rsa.pub

This will show you the public key. Use the `Terminal` copy command to copy
this into your clipboard.

Then go to [this page](https://csil-git1.cs.surrey.sfu.ca/profile): [csil-git1.cs.surrey.sfu.ca/profile](https://csil-git1.cs.surrey.sfu.ca/profile)
and select `SSH Keys` from the left menu.

Use the web browser to paste command to paste your public key into the `Key`
box and give it a `Title` (e.g. 'CSIL' is a reasonable title) and then `Add key`.

### Using git

If you have not set up your git configuration then in a terminal window, enter the following commands:

    git config --global user.name YOUR_USERNAME
    git config --global user.email YOUR_USERNAME@sfu.ca
    git config --global core.editor nano
    git config --global push.default current
    cd $HOME

If you prefer another editor instead of `nano` set up that one as the default editor.

You should use the following command to clone your git repository for this course:

    git clone git@csil-git1.cs.surrey.sfu.ca:YOUR_USERNAME/CMPT379-{{ site.semcode }}-YOUR_USERNAME.git

(copy and paste might be helpful here) and press return. If you did
skipped any of the above steps in setting up your GitLab repo this command will not work.
The system might prompt you for a username/password combo.  Supply the usual
answers. To avoid entering your username/password over and over again you can
set up [passwordless ssh](http://www.linuxproblem.org/art_9.html).

The project page itself gives more complete instructions for the first interactions with the repository: you get a very empty repository that requires some bootstrapping.

A Git manual is beyond the scope of this page, but here are the bare basics:

    git pull                     # get changes from the gitlab server
    text_editor some/file.txt    # do some work
    git add some/file.txt        # stage those changes for commit
    text_editor other/file.txt   # do some more work
    git add other/file.txt       # stage more changes for commit
    git commit                   # commit the changes
    git push                     # push to the remote server to save your work

Here are some Git tutorials for more information:

* [The standard Git tutorial](https://git-scm.com/docs/gittutorial)
* [Interactive Git basics](http://try.github.io)
* [Pro Git book](https://git-scm.com/book/en/v2), which has a good intro (and more)
* [Writing better commit messages](http://lbrandy.com/blog/2009/03/writing-better-commit-messages/)

### Getting homework files

You must have git and python (3.x) on your system to run the assignments.
Once you've confirmed this, run this command:

    git clone https://github.com/anoopsarkar/compilers-class-hw.git

In the `rmprefix` directory you will find various python programs
which you will use to test your solution to this homework and to
prepare files you will upload to [Coursys]({{ site.coursys }}).

You will get updates to the homework files by going to the directory
where you cloned the repository and then doing:

    # go to the directory where you did a git clone
    git pull origin master

Before you start a new homework make sure you do a `git pull`
to get the latest homework files.

To get started with your homework do the following steps.

### Copy over files

Clone your gitlab repository and enter that directory and copy over the files:

    git clone git@csil-git1.cs.surrey.sfu.ca:YOUR_USERNAME/CMPT379-{{ site.semcode }}-YOUR_USERNAME.git
    cd CMPT379-{{ site.semcode }}-YOUR_USERNAME
    mkdir -p rmprefix
    cd rmprefix
    cp -r /your-path-to/compilers-class-hw/rmprefix/* .
    git add *
    git commit -m 'initial commit'
    git push

If you update my repository using `git pull` then you might have to copy over the
new files into your repository. Be careful you do not clobber your own files
in the `answer` directory.

### Default solution

Your solution must be compiled in the `answer` directory and must be called `rmprefix`.
There is an incomplete solution to this homework in `answer/default.cc`. Copy
it over as your initial solution:

    cd CMPT379-{{ site.semcode }}-YOUR_USERNAME/rmprefix/answer
    cp default.cc rmprefix.cc
    make rmprefix

## The Challenge

The objective of this homework is to lay out the development
and testing methodology for the rest of the homeworks so it
is designed to be a trivial task that can be tested.

Your task for this homework is to write a very simple C++ program
that trims the leading whitespace (if any) from each line read from
the standard input stream `std:cin`. Any other whitespace should
be left untouched. For this homework we define whitespace to be
only the ASCII space `' '` and tab `'\t'` characters. 

For example, for the following input:

      line1
           line2
                line3

The output on standard output `std::cout` should be:

    line1
    line2
    line3

Make sure only leading whitespace is removed. Any other
whitespace should be preserved in the output.

## Your Task

Write a C++ program called `rmprefix.cc` that does the task that
is described above and add it to your git repository in the `answer`
directory.

If your program succeeds you should exit from your program using
`exit(EXIT_SUCCESS)`. In this homework this should not happen but
if your program exits with an error you should exit using
`exit(EXIT_FAILURE)`. The definitions of `EXIT_SUCCESS` and
`EXIT_FAILURE` are in `cstdlib` (for C++) and in `stdlib.h` (for
C).

## Development and upload procedure

Remember to push your solution source code to your git repository:

    cd CMPT379-{{ site.semcode }}-YOUR_USERNAME/rmprefix/answer
    git add rmprefix.cc
    git commit -m 'initial solution'
    git push

Then each time you finish a component of your solution you can push it to the remote repository:

    git add answer/rmprefix.cc # or other files you worked on
    git commit -m 'commit message'
    git push

You have been given three helper programs to help you develop your solution to this homework.

### Run your solution on testcases

Run your solution program on the testcases using the Python program `zipout.py`. 
Your solution must be compiled in the `answer` directory and must be called `rmprefix`.
Run against all testcases as follows:

    # go to the directory with the file zipout.py
    python3 zipout.py

This creates a directory called `output` and a file `output.zip` which can be checked against the reference output files 
(see section on _Check your solution_ below).

If you run `zipout.py` multiple times it will overwrite your output directory and zip file which should be fine most of the time (but be careful).

For this homework the program `zipout.py` uses the binary `answer/rmprefix` by default. To discover the
command line options for this program, run:

    python3 zipout.py -h

The option to log verbose debugging information to a log file will be very useful in future homeworks to debug your own code.

### Check your solution

Check your solution accuracy using the Python program `check.py`. You must create an `output.zip` file using the above step in _Run your solution on testcases_.
Note that the references are only available for the `dev` testcases. When you are graded you will be evaluated on both the `dev` and `test` testcases.
`output.zip` contains your output for both sets of testcases.

    python3 check.py
    Correct(dev): 4 / 6
    Score(dev): 4.00
    Total Score: 4.00

### Package your output and source for Coursys

You must upload your output zipfile and source code to Coursys. You should prepare your source for upload using the Python program `zipsrc.py`.

    # go to the directory with the file zipsrc.py
    python3 zipsrc.py

This will create a zip file called `source.zip`. You should upload this file as your submission to `hw0` on [Coursys]({{ site.coursys }}).

**Be careful**: `zipsrc.py` will only package files in the `answer` directory. Make sure you have put all your supporting files in that directory. In particular, put relevant documentation into `answer/README.md`. 

If you add any testcases of your own please put them in the directories `answer/testcases/[your-username]/` and `answer/references/[your-username]/` using the same convention used by `zipout.py` and `check.py`.

## Ground Rules

* You must turn in two things:
    * Your source code from the `answer` directory as a zip file `source.zip` produced by running `python3 zipsrc.py` must be uploaded to the `hw0` submission page on [Coursys]({{ site.coursys }}).
    * Your output on the testcases which is the file `output.zip` produced by running `python3 zipout.py` must be uploaded to the `hw0` submission page on [Coursys]({{ site.coursys }}). When we run `check.py` on the public testcases it should have a value higher than the output from the `default.cc` program to get any marks.
* Your source code from `source.zip` must be on your gitlab repository. Please commit and push often in order to get feedback on your code.
* You cannot use data or code resources outside of what is provided to you. If you use external code snippets provide citations in the `answer/README.md` file.
* For future homeworks, for the written description of your solution and supporting documentation, you can use plain ASCII but for math equations it is better to use kramdown. Do not use any proprietary or binary file formats such as Microsoft Word.

If you have any questions or you’re confused about anything, just ask.

