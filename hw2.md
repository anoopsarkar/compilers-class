---
layout: default
img: sexpr
img_link: "https://en.wikipedia.org/wiki/S-expression"
caption: "In Lisp and programming languages related to it, s-expressions are used to represent both source code and data."
title: Homework | Parser
active_tab: homework
---

# Parser for Decaf

<p class="text-muted">Start on {{ site.hwdates[2].startdate }}</p>
<p class="text-muted">Due on {{ site.hwdates[2].deadline }}</p>

Your task for this homework is to write a parser for the [Decaf programming language](decafspec.html).

## Yacc

We will be using a parser generator called Yacc to
do this homework. Before you start programming for this
homework it is very important you work through the 
[Yacc practice problems](yacc-practice.html) first.

The programming tool is called `yacc` and the implementation
we will be using is GNU `bison`.

## Getting Started

You must have git and python (3.x) on your system to run the assignments.
Once you've confirmed this, run this command:

    git clone https://github.com/anoopsarkar/compilers-class-hw.git

In the `decafast` directory you will find various python programs
which you will use to test your solution to this homework.

If you have already cloned the repository earlier you can
get the new homework files by going to the directory
where you cloned the repository earlier and then doing:

    # go to the directory where you did a git clone earlier
    git pull origin master

To get started with your homework do the following steps.

### Copy over files to your repository

Assuming you have set up your repository using the instruction in [HW0](hw0.html), 
clone your repository and enter that directory and copy over the files:

    git clone git@csil-git1.cs.surrey.sfu.ca:YOUR_USERNAME/CMPT379-{{ site.semcode }}-YOUR_USERNAME.git
    cd CMPT379-{{ site.semcode }}-YOUR_USERNAME
    mkdir -p decafast
    cd decafast
    cp -r /your-path-to/compilers-class-hw/decafast/* .
    git add *
    git commit -m 'initial commit'
    git push

If you update my repository using `git pull` then you might have to copy over the
new files into your repository. Be careful you do not clobber your own files
in the `answer` directory.

### Default solution

Your solution must be compiled in the `answer` directory and must be called `decafast`.
There is an incomplete solution to this homework in the `answer` directory. You can create the `default`
binary as follows:

    cd your-repo-name/answer
    make default

### Creating Decafast

Make new copies of the following `default` files for `decafast`:

    cp default.cc decafast.cc
    cp default.lex decafast.lex
    cp default.y decafast.y

Modify `decafast.cc` to replace `#include "default.tab.h"` with `#include "decafast.tab.h"`.

Modify `decafast.lex` to replace `#include "default.tab.h"` with `#include "decafast.tab.h"`.

Modify `decafast.y` to replace `#include "default.cc"` with `#include "decafast.cc"`.

Build the `decafast` executable by running:

    make decafast

## The Challenge

The goal of this homework is to write a parser for the Decaf programming language.
The details of the structure of Decaf programs is given in the Decaf specification:

> [Decaf specification](decafspec.html)

Read the specification carefully before you attempt to write any code to solve
this homework.

## Your Task

Using the [Decaf language specification](decafspec.html) as your guide, 
provide a parser for the Decaf language that produces an abstract
syntax tree for valid Decaf programs.

An abstract syntax tree (AST) is a high-level representation of the
program structure without the necessity of containing all the details
in the source code; it can be thought of as an abstract representation
of the source code.

The specification for the abstract syntax tree to be produced by
your program is given below using the [Zehpyr Abstract Syntax
Definition Language](http://www.oilshell.org/blog/2016/12/11.html)
which is a method for serialization of the abstract syntax tree.

<script src="https://gist.github.com/anoopsarkar/b1dec7f4ba7e7f70bc1ee99511be4bca.js"></script>

Make sure you obey the following requirements:

1. If your program succeeds in parsing the input you should exit from your program using `exit(EXIT_SUCCESS)`. And if your program finds an error in the input Decaf program you should exit using `exit(EXIT_FAILURE)`. The definitions of `EXIT_SUCCESS` and `EXIT_FAILURE` are in `cstdlib` (for C++) and in `stdlib.h` (for C).
1. The abstract syntax tree produced by your program must be in the format specified above. The output specification is also available as the file `Decaf.asdl` in the `decafast` directory.
1. Do not add whitespace in your output. This might cause issues with matching your output to the reference output.

## Development and upload procedure

Remember to push your solution source code to your repository:

    cd answer
    git add decafast.y decafast.lex # and any other files such as decafast.cc and decafast-defs.h
    git commit -m 'initial solution'
    git push

Then each time you finish a component of your solution you can push it to the remote repository:

    git add [source-file]
    git commit -m 'commit message' [source-file]
    git push

You have been given three helper programs to help you develop your solution to this homework.

### Run your solution on testcases

Run your solution program on the testcases using the Python program `zipout.py`. 
Your solution must be compiled in the `answer` directory and must be called `decafast`.
Run against all testcases as follows:

    # go to the directory with the file zipout.py
    python3 zipout.py

This creates a directory called `output` and a file `output.zip` which can be checked against the reference output files 
(see section on _Check your solution_ below).

If you run `zipout.py` multiple times it will overwrite your output directory and zip file which should be fine most of the time (but be careful).

### Check your solution

Check your solution accuracy using the Python program `check.py`. You must create an `output.zip` file using the above step in _Run your solution on testcases_.
Note that the references are only available for the `dev` testcases. When you are graded you will be evaluated on both the `dev` and `test` testcases.
`output.zip` contains your output for both sets of testcases.

You can use the default program provided to get an initial solution to this homework. Run `python3 zipout.py -r default` to get a `source.zip` file you can score.

    python3 check.py
    Correct(dev): 34 / 134
    Score(dev): 34.00
    Total Score: 34.00

### Package your source for Coursys

You must also upload your source code to Coursys. You should prepare your source for upload using the Python program `zipsrc.py`.

    # go to the directory with the file zipsrc.py
    python3 zipsrc.py

This will create a zip file called `source.zip`. You should upload this file as your submission to `hw2` on [Coursys]({{ site.coursys }}).

**Be careful**: `zipsrc.py` will only package files in the `answer` directory. Make sure you have put all your supporting files in that directory. In particular, put relevant documentation into `answer/README.md`. 

If you add any testcases of your own please put them in the directories `answer/testcases/[your-username]/` and `answer/references/[your-username]/` using the same convention used by `zipout.py` and `check.py`.

## Ground Rules

* You must turn in two things:
    * Your source code from the `answer` directory as a zip file `source.zip` produced by running `python3 zipsrc.py` must be uploaded to the `hw2` submission page on [Coursys]({{ site.coursys }}).
    * Your output on the testcases which is the file `output.zip` produced by running `python3 zipout.py` must be uploaded to the `hw2` submission page on [Coursys]({{ site.coursys }}). When we run `check.py` on the public testcases it should have a value higher than the output from the default program to get any marks.
* Your source code from `source.zip` must be on your gitlab repository. Please commit and push often in order to get feedback on your code.
* Make sure that we can run `make decafast` in your answer directory to create the `decafast` binary.
* You cannot use data or code resources outside of what is provided to you. If you use external code snippets provide citations in the `answer/README.md` file.
* For future homeworks, for the written description of your solution and supporting documentation, you can use plain ASCII but for math equations it is better to use kramdown. Do not use any proprietary or binary file formats such as Microsoft Word.

## Grading

* Score for testcases both dev and test.
* Code review by TAs. Please check for comments on your code on [gitlab](http://gitlab.cs.sfu.ca).

If you have any questions or you’re confused about anything, just ask.

