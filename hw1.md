---
layout: default
img: kenthompson
img_link: "https://en.wikipedia.org/wiki/Ken_Thompson"
caption: "Ken Thompson (sitting) with Dennis Ritchie. Ken Thompson wrote a 1968 journal paper on his regexp implementation for the QED editor which he wrote in assembly language on an IBM 7094 running the CTSS OS."
title: Homework | Lexer
active_tab: homework
---

# Lexical Analyzer for Decaf

<p class="text-muted">Start on {{ site.hwdates[1].startdate }}</p>
<p class="text-muted">Due on {{ site.hwdates[1].deadline }}</p>

Your task for this homework is to write a lexical analyzer (lexer
for short) for the [Decaf programming language](decafspec.html)
which is the programming language specifically for this course.

## Lex

We will be using a lexical analyzer generator called Lex to
do this homework. Before you start programming for this
homework it is very important you work through the 
[Lex practice problems](lex-practice.html) first.

The programming tool is called `lex` and the implementation
we will be using is GNU `flex`.

## Getting Started

You must have git and python (3.x) on your system to run the assignments.
Once you've confirmed this, run this command:

    git clone https://github.com/anoopsarkar/compilers-class-hw.git

In the `decaflex` directory you will find various python programs
which you will use to test your solution to this homework.

You will get updates to the homework files by going to the directory
where you cloned the repository and then doing:

    # go to the directory where you did a git clone for HW1
    git pull origin master

To get started with your homework do the following steps.

### Set up your repository

Make sure you have already followed the [instructions in HW0](hw0.html) to set up your gitlab repository.

### Copy over files

Clone your repository and enter that directory and copy over the files:

    git clone git@csil-git1.cs.surrey.sfu.ca:YOUR_USERNAME/CMPT379-{{ site.semcode }}-YOUR_USERNAME.git
    cd CMPT379-{{ site.semcode }}-YOUR_USERNAME
    mkdir -p decaflex
    cd decaflex
    cp -r /your-path-to/compilers-class-hw/decaflex/* .
    git add *
    git commit -m 'initial commit'
    git push

If you update my repository using `git pull` then you might have to copy over the
new files into your repository. Be careful you do not clobber your own files
in the `answer` directory.

### Default solution

Your solution must be compiled in the `answer` directory and must be called `decaflex`.
There is an incomplete solution to this homework in `answer/default.lex`. Copy
it over as your initial solution:

    cd your-repo-name/answer
    cp default.lex decaflex.lex
    make decaflex

## The Challenge

The goal of this homework is to write a lexical analyzer for the Decaf programming language.
The details of the lexical elements in Decaf are in the Decaf specification:

> [Decaf specification](decafspec.html)

You will need to refer to the [List of Tokens](http://anoopsarkar.github.io/compilers-class/decafspec.html#list-of-tokens)
to produce the output in the right format for for this homework.

Read the specification carefully at least upto the section called Decaf Program Structure.

The lexical analyzer produces a stream of tokens for a given Decaf program. The input
is taken from `stdin` (standard input) and the output token stream is sent to `stdout`
(standard output). You must issue errors on the `stderr` (standard error) stream.

For example, for the input Decaf program:

    package Test { func main() int { } }

The lexical analyzer produces the following token stream:

    T_PACKAGE package
    T_WHITESPACE  
    T_ID Test
    T_WHITESPACE  
    T_LCB {
    T_WHITESPACE  
    T_FUNC func
    T_WHITESPACE  
    T_ID main
    T_LPAREN (
    T_RPAREN )
    T_WHITESPACE  
    T_INT int
    T_WHITESPACE  
    T_LCB {
    T_WHITESPACE  
    T_RCB }
    T_WHITESPACE  
    T_RCB }
    T_WHITESPACE \n

The default lexer you were provided does work for this input. Run it and see:

    # go to the answer directory and build your binary (see instructions above)
    ./decaflex < ../testcases/dev/default-passes.decaf

The full list of tokens is provided in the section List of Tokens in the [Decaf specification](decafspec.html).

## Your Task

Using the [Decaf language specification](decafspec.html) as your guide, 
provide a lex program that is a lexical analyzer for the Decaf language.

Make sure you obey the following requirements:

1. If your program succeeds in parsing the input you should exit from your program using `exit(EXIT_SUCCESS)`. And if your program finds a lexical error you should exit using `exit(EXIT_FAILURE)`. The definitions of `EXIT_SUCCESS` and `EXIT_FAILURE` are in `cstdlib` (for C++) and in `stdlib.h` (for C).
1. Note that the token names and lexeme values should be identical to the sample output provided to you in the `testcases` directory. 
1. You must use the token names provided in the List of Tokens section of the Decaf specification.
1. You must include a special whitespace and comment token. The whitespace token should have a lexeme value that includes all the whitespace characters. The whitespace and comment lexemes should convert the newline character into the literal string `\n` so that the line number and character number of each token can be recovered from the lexical analyzer output.
1. [Provide appropriate error reporting with the line number and location in the line where the error was detected](https://gist.github.com/anoopsarkar/33ea6b0374578ec8b168860f0fdd4190).

## Development and upload procedure

Remember to push your solution source code to your git repository:

    git add decaflex.lex
    git commit -m 'initial solution'
    git push

Then each time you finish a component of your solution you can push it to the remote repository:

    git add decaflex.lex # or other files you worked on
    git commit -m 'commit message' decaflex.lex # or other files you worked on
    git push

You have been given three helper programs to help you develop your solution to this homework.

### Run your solution on testcases

Run your solution program on the testcases using the Python program `zipout.py`. 
Your solution must be compiled in the `answer` directory and must be called `decaflex`.
Run against all testcases as follows:

    # go to the directory with the file zipout.py
    python3 zipout.py

This creates a directory called `output` and a file `output.zip` which can be checked against the reference output files 
(see section on _Check your solution_ below).

If you run `zipout.py` multiple times it will overwrite your output directory and zip file which should be fine most of the time (but be careful).

### Check your solution

Check your solution accuracy using the Python program `check.py`. You must create an `output.zip` file using the above step in _Run your solution on testcases_.

    python3 check.py 
    Correct(dev): 4 / 59
    Score(dev): 4.00
    Total Score: 4.00

### Package your source for Coursys

You must also upload your source code to Coursys. You should prepare your source for upload using the Python program `zipsrc.py`.

    # go to the directory with the file zipsrc.py
    python3 zipsrc.py

This will create a zip file called `source.zip`. You should upload this file as your submission to hw1 on [Coursys]({{ site.coursys }}).

**Be careful**: `zipsrc.py` will only package files in the `answer` directory. Make sure you have put all your supporting files in that directory. In particular, put relevant documentation into `answer/README.md`. 

## Ground Rules

* You must turn in two things:
    * Your source code from the `answer` directory as a zip file `source.zip` produced by running `python3 zipsrc.py` must be uploaded to the `hw1` submission page on [Coursys]({{ site.coursys }}).
    * Your output on the testcases which is the file `output.zip` produced by running `python3 zipout.py` must be uploaded to the `hw1` submission page on [Coursys]({{ site.coursys }}). When we run `check.py` on the public testcases it should have a value higher than the output from the `default.lex` program to get any marks.
* Make sure that we can run `make decaflex` in your answer directory to create the `decaflex` binary.
* You cannot use data or code resources outside of what is provided to you. If you use external code snippets provide citations in the `answer/README.md` file.
* For future homeworks, for the written description of your solution and supporting documentation, you can use plain ASCII but for math equations it is better to use kramdown. Do not use any proprietary or binary file formats such as Microsoft Word.

## Grading

* Score for testcases both dev and test.
* Code review by TAs. Please check for comments on your code on [gitlab](http://gitlab.cs.sfu.ca).

If you have any questions or you’re confused about anything, just ask.

