---
layout: default
img: kenthompson
img_link: "https://en.wikipedia.org/wiki/Ken_Thompson"
caption: "Ken Thompson (sitting) with Dennis Ritchie. Ken Thompson wrote a 1968 journal paper on his regexp implementation for the QED editor which he wrote in assembly language on an IBM 7094 running the CTSS OS."
title: Homework | Lexer
active_tab: homework
---

# Lexical Analyzer for Decaf

<p class="text-muted">Due on Tuesday, June 7, 2016</p>

Your task for this homework is to write a lexical analyzer (lexer
for short) for the [Decaf programming language](decafspec.html)
which is the programming language specifically for this course.

## Getting Started

You must have git and python (2.7) on your system to run the assignments.
Once you've confirmed this, run this command:

    git clone https://github.com/anoopsarkar/compilers-class-hw.git

In the `decaflex` directory you will find various python programs
which you will use to test your solution to this homework and to
prepare files you will upload to the 
[leaderboard for this homework]({{ site.leaderboard }}) and to
[Coursys]({{ site.coursys }}).

You will get updates to the homework files by going to the directory
where you cloned the repository and then doing:

    # go to the directory where you did a git clone for HW1
    git pull origin master

To get started with your homework do the following steps.

### Set up your repository

Follow these [instructions to set up your repository on GitLab](https://courses.cs.sfu.ca/2016sp-cmpt-470-e1/pages/GitLab)

In the above instructions, change the values of instructor and TA to `anoop` and `msiahban`.

### Copy over files

Clone your repository and enter that directory and copy over the decaflex files:

    git clone git@csil-git1.cs.surrey.sfu.ca:your-group-name/your-repo-name.git
    cd your-repo-name
    cp -r /your-path-to/compilers-class-hw/decaflex/* .
    git add *
    git commit -m 'initial commit'
    git push

If you update my repository using `git pull` then you might have to copy over the
new files into your repository. Be careful you do not clobber your own files
in the `answer` directory.

### Default solution

Your solution to this homework must be called `decaflex.lex` in the `answer` directory.
There is an incomplete solution to this homework in `answer/default.lex`. Copy
it over as your initial solution:

    cd your-repo-name/answer
    cp default.lex decaflex.lex
    make decaflex

Remember to push your solution source code to GitLab:

    git add decaflex.lex
    git commit -m 'initial solution'
    git push

## The Challenge

The goal of this homework is to write a lexical analyzer for the Decaf programming language.
The details of the lexical elements in Decaf are in the Decaf specification:

> [Decaf specification](decafspec.html)

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

    # go to the answer directory and build the default decaflex (see instructions above)
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
1. Provide appropriate error reporting with the line number and location in the line where the error was detected.

## Development and upload procedure

You have been given three helper programs to help you develop your solution to this homework.

### Run your solution on testcases

Run your solution program on the testcases using the Python program `zipout.py`. 
Your solution must be compiled in the `answer` directory and must be called `decaflex`.
Run against all testcases as follows:

    # go to the main decaflex directory with the file zipout.py
    python zipout.py

This creates a directory called `output` and a file `output.zip` which can be checked against the reference output files 
(see section on _Check Your Solution_ below).
The file `output.zip` can also be uploaded to the [leaderboard]({{ site.leaderboard }}) when you are ready.

If you run `zipout.py` multiple times it will overwrite your output directory and zip file which should be fine most of the time (but be careful).

### Check your solution

Check your solution accuracy using the Python program `check.py`. You must create an `output.zip` file using the above step in _Run your solution on testcases_.

    python check.py 
    Correct(dev): 4 / 59
    Score(dev): 4.00
    Total Score: 4.00

### Check accuracy on hidden testcases

For some testcases (those in the `testcases/test` directory) the inputs are provided but the reference output is not provided to you.
To see your performance on those testcases you must submit your `output.zip` to the [leaderboard]({{ site.leaderboard }}).
You will see your performance on test and your accuracy will be displayed on the [class leaderboard page](leaderboard.html).

### Package your source for Coursys

You must also upload your source code to Coursys. You should prepare your source for upload using the Python program `zipsrc.py`.

    # go to the main decaflex directory with the file zipsrc.py
    python zipsrc.py

This will create a zip file called `source.zip`. You should upload this file as your submission to hw1 on [Coursys]({{ site.coursys }}).

**Be careful**: `zipsrc.py` will only package files in the `answer` directory. Make sure you have put all your supporting files in that directory. In particular, put relevant documentation into `answer/docs/README.md`. 

## Ground Rules

* Each group should submit using one person as the designated uploader.
* You must turn in two things:
    * Your output on the testcases which is the file `output.zip` produced by running `python zipout.py` must be uploaded to the [leaderboard web site]({{ site.leaderboard }}). It should have a value higher than the output from `default.lex` to get any marks.
    * Your source code from the `answer` directory as a zip file `source.zip` produced by running `python zipsrc.py` must be uploaded to the HW1 submission page on [Coursys]({{ site.coursys }}).
* You cannot use data or code resources outside of what is provided to you. If you use external code snippets provide citations in the `README.md` file.
* For the written description of your solution and supporting documentation, you can use plain ASCII but for math equations it is better to use kramdown. Do not use any proprietary or binary file formats such as Microsoft Word.

If you have any questions or you’re confused about anything, just ask.

## Appendix

Practice your skills with lex before attempting to solve this homework.

> [Lex practice](LEX-practice.html)


