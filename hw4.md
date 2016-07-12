---
layout: default
llvmver: 3.8
img: caffeine
img_link: "https://en.wikipedia.org/wiki/Decaffeination"
caption: "The Swiss Water Method uses water and osmosis to decaffeinate coffee beans. Developed in Switzerland in 1933 and turned into a commercially viable method by Coffex S.A. in 1980, in 1988 it became a product sold by The Swiss Water Decaffeinated Coffee Company of Burnaby, British Columbia, Canada."
title: Homework | Decaf Compiler
active_tab: homework
---

# The Decaf Compiler

<p class="text-muted">Due on Tuesday, August 2, 2016</p>

Your task for this homework is to use [LLVM](http://llvm.org) for code generation in order to
write a fully working compiler, including semantic checks, for the [Decaf
programming language](decafspec.html).

## LLVM

We will be using a code generation and compiler toolkit called
[LLVM](http://llvm.org/)  for this homework. We will be using LLVM version 
{{ page.llvmver }}. 

Revisit the [LLVM practice problems](llvm-practice.html) before starting
on this homework.

## Getting Started

You must have git and python (2.7) on your system to run the assignments.
Once you've confirmed this, run this command:

    git clone https://github.com/anoopsarkar/compilers-class-hw.git

In the `decafcomp` directory you will find various python programs
which you will use to test your solution to this homework and to
prepare files you will upload to the 
[leaderboard for this homework]({{ site.leaderboard }}) and to
[Coursys]({{ site.coursys }}).

If you have already cloned the repository earlier you can
get the new homework files by going to the directory
where you cloned the repository earlier and then doing:

    # go to the directory where you did a git clone earlier
    git pull origin master

To get started with your homework do the following steps.

### Copy over files to your repository

Assuming you have set up your repository using the instruction in [HW1](hw1.html), 
clone your repository and enter that directory and copy over the decafcomp files:

    git clone git@csil-git1.cs.surrey.sfu.ca:your-group-name/your-repo-name.git
    cd your-repo-name/decafcomp
    cp -r /your-path-to/compilers-class-hw/decafcomp/* .
    git add *
    git commit -m 'initial commit'
    git push

If you update my repository using `git pull` then you might have to copy over the
new files into your repository. Be careful you do not clobber your own files
in the `answer` directory.

### Default solution

Your solution must be compiled in the `answer` directory and must be called `decafcomp`.
There is an incomplete solution to this homework in the `answer` directory. You can create the `default`
binary as follows:

    cd your-repo-name/answer
    make default

## The Challenge

The goal of this homework is to write a full working compiler for the Decaf
programming language. The structure of Decaf and code generation hints are
given in the Decaf specification:

> [Decaf specification](decafspec.html)

Read the specification carefully before you attempt to write any code to solve
this homework.

## Your Task

Extend your solution for [HW3](hw3.html) to complete a fully working
compiler for the [Decaf language specification](decafspec.html).

#### Step 1: Global Variables

Add support for global variables also known as field variables.  Decaf supports
definition of integer and boolean arrays only as global variables.

You will need to add code generation for assignment and modification
of array locations in expressions.

#### Step 2: Zero initialize all variables

Make sure that all variables, including arrays, are zero initialized.

#### Step 3: Control flow and Loops

Add support for control flow (`if` statements) and loops (`while` and `for` statements).
You will need to understand the static single assignment (SSA) form of a basic block
in the control flow graph for the program and how to implement SSA form using the 
LLVM API.

You also have to implement `else` blocks that can optionally follow `if` statements
as well as `break` and `continue` statements. 

To complete control flow and loops you will need to implement backpatching
using the symbol table to mark the entry, continue and exit points for the
control flow and loops.

#### Step 4: Short Circuit

Implement [short-circuit evaluation](https://en.wikipedia.org/wiki/Short-circuit_evaluation) for boolean expressions. 
Short circuiting is implemented using control flow, very similar to an `if` statement.

#### Step 5: Semantics

Perform at least the following semantic checks for any syntactically 
valid input Decaf program:

* A method called `main` has to exist in the Decaf program.
* Find all cases where there is a type mismatch between the definition of the type of a variable and a value assigned to that variable. e.g. `bool x; x = 10;` is an example of a type mismatch. 
* Find all cases where an expression is well-formed, where binary and unary operators are distinguished from relational and equality operators. e.g. `true + false` is an example of a mismatch but `true != true` is not a mismatch. 
* Check that all variables are defined in the proper scope before they are used as an lvalue or rvalue in a Decaf program. 
* Check that the return statement in a method matches the return type in the method definition. e.g. `func foo() bool { return(10); }` is an example of a mismatch. 

Raise a semantic error if the input Decaf program does not pass any of the above semantic checks.

Your program should take a syntactically valid Decaf program as input and perform all the semantic checks listed above. You can optionally include any other semantic checks that seem reasonable based on your analysis of the language. Provide a readme file with a description of any additional semantic checks.

#### Step 6: Error reporting

Your program should reject any syntactically or semantically invalid Decaf
program and provide a helpful error message. The quality of the error reporting
is up to you but you should at least report the line and character number where
the syntax error is thrown.

#### Step 7: Code optimization (Optional)

Optionally implement the following optimization passes:

* Convert stack allocation usage (Alloca) into register usage (mem2reg).
* Simple peephole optimization (instruction combining pass).
* Re-associate expresssions.
* Eliminate common sub-expressions (GVN).
* Simplify the control flow graph (CFG simplification).

You can implement this using the LLVM `opt` binary which can be used to run all
of the above optimization passes on the LLVM bitcode output for a Decaf
program.

Instead of using `opt` you could use the `FunctionPassManager` LLVM API call to
add optimization passes. You can even [write your own LLVM
pass](http://llvm.org/docs/WritingAnLLVMPass.html).

#### Step 8: Add source-level debug info (Optional)

Add source level debug information using DWARF annotations to your LLVM assembly. 

LLVM assembly has support for [debug instructions](http://llvm.org/docs/SourceLevelDebugging.html).
Also see how to use the LLVM API to add debug annotations by reading through the
[LLVM Kaleidoscope tutorial on DWARF emission](http://llvm.org/docs/tutorial/LangImpl8.html).

More details about the task is provided by examining the testcases for this homework.

The output should be in LLVM assembly which can be compiled to x86
assembly using the LLVM tools and run as a binary. We will use the binary
`llvm-run` in the answer directory to create and run the binary from the 
Decaf programs in the testcases directory.

Make sure you obey the following requirements:

1. If your program succeeds in parsing the input you should exit from your program using `exit(EXIT_SUCCESS)`. And if your program finds an error in the input Decaf program you should exit using `exit(EXIT_FAILURE)`. The definitions of `EXIT_SUCCESS` and `EXIT_FAILURE` are in `cstdlib` (for C++) and in `stdlib.h` (for C).
1. You must dump the LLVM assembly by calling `TheModule->dump()` where `TheModule` is of type `llvm::Module*`.

## Development and upload procedure

Remember to push your solution source code to your repository:

    cd answer
    git add decafcomp.y decafcomp.lex # and any other files you need for the solution
    git commit -m 'initial solution'
    git push

Then each time you finish a component of your solution you can push it to the remote repository:

    git add [source-file]
    git commit -m 'commit message' [source-file]
    git push

You have been given three helper programs to help you develop your solution to this homework.

### Run your solution on testcases

Run your solution program on the testcases using the Python program `zipout.py`. 
Your solution must be compiled in the `answer` directory and must be called `decafcomp`.
Run against all testcases as follows:

    # go to the directory with the file zipout.py
    python zipout.py

This creates a directory called `output` and a file `output.zip` which can be checked against the reference output files 
(see section on _Check your solution_ below).
The file `output.zip` can also be uploaded to the [leaderboard]({{ site.leaderboard }}) when you are ready.

If you run `zipout.py` multiple times it will overwrite your output directory and zip file which should be fine most of the time (but be careful).

### Check your solution

Check your solution accuracy using the Python program `check.py`. You must
create an `output.zip` file using the above step in _Run your solution on
testcases_.

You can use the default program provided to get an initial solution to this
homework. Run `python zipout.py -r default` to get a `source.zip` file you can
score using `check.py`.

    python check.py 
    Correct(dev): 19 / 212
    Score(dev): 19.00
    Total Score: 19.00

### Check accuracy on hidden testcases

For some testcases (those in the `testcases/test` directory) the inputs are
provided but the reference output is not provided to you.  To see your
performance on those testcases you must submit your `output.zip` to the
[leaderboard]({{ site.leaderboard }}).
You will see your performance on test and your accuracy will be displayed on
the [class leaderboard page](leaderboard.html).

### Package your source for Coursys

You must also upload your source code to Coursys. You should prepare your
source for upload using the Python program `zipsrc.py`.

    # go to the directory with the file zipsrc.py
    python zipsrc.py

This will create a zip file called `source.zip`. You should upload this file as
your submission to hw1 on [Coursys]({{ site.coursys }}).

**Be careful**: `zipsrc.py` will only package files in the `answer` directory.
Make sure you have put all your supporting files in that directory. In
particular, put relevant documentation into `answer/docs/README.md`. 

### Use your own code

For this homework we will reward those who have implemented all the stages of
the compiler themselves.  If you have used the source code from the provided
solution of a previous homework to implement your compiler for this homework,
you will lose 20% of the marks for this homework for each solution used. For
example, if you use the provided solution for HW1, HW2 and HW3 to solve this
homework then you can get at most 40% of the total marks for HW4.

You will **not** incur a penalty if you wrote your own source code for the
solution to a previous homework after having examined the solution for a
previous homework.

## Ground Rules

* Each group should submit using one person as the designated uploader.
* You must turn in two things:
    * Your output on the testcases which is the file `output.zip` produced by running `python zipout.py` must be uploaded to the [leaderboard web site]({{ site.leaderboard }}). It should have a value higher than the output from `default.lex` to get any marks.
    * Your source code from the `answer` directory as a zip file `source.zip` produced by running `python zipsrc.py` must be uploaded to the HW4 submission page on [Coursys]({{ site.coursys }}).
* You cannot use data or code resources outside of what is provided to you. If you use external code snippets provide citations in the `README.md` file.
* For the written description of your solution and supporting documentation, you can use plain ASCII but for math equations it is better to use kramdown. Do not use any proprietary or binary file formats such as Microsoft Word.

If you have any questions or you’re confused about anything, just ask.

