---
layout: default
img: sexpr
img_link: "https://en.wikipedia.org/wiki/S-expression"
caption: "In Lisp and programming languages related to it, s-expressions are used to represent both source code and data."
title: Homework | Parser
active_tab: homework
---

# Parser for Decaf

<p class="text-muted">Due on Tuesday, June 21, 2016</p>

Your task for this homework is to write a parser for the [Decaf programming language](decafspec.html).

## Getting Started

You must have git and python (2.7) on your system to run the assignments.
Once you've confirmed this, run this command:

    git clone https://github.com/anoopsarkar/compilers-class-hw.git

In the `decafast` directory you will find various python programs
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

### Set up your repository

Follow these [instructions to set up your repository on GitLab](https://courses.cs.sfu.ca/2016sp-cmpt-470-e1/pages/GitLab)

In the above instructions, change the values of instructor and TA to `anoop` and `msiahban`.

### Copy over files to your repository

Assuming you have set up your repository using the instruction in [HW1](hw1.html), 
clone your repository and enter that directory and copy over the decaflex files:

    git clone git@csil-git1.cs.surrey.sfu.ca:your-group-name/your-repo-name.git
    cd your-repo-name
    cp -r /your-path-to/compilers-class-hw/decafast/* .
    git add *
    git commit -m 'initial commit'
    git push

If you update my repository using `git pull` then you might have to copy over the
new files into your repository. Be careful you do not clobber your own files
in the `answer` directory.

### Default solution

Your solution to this homework must be called `decafast.y` and `decafast.lex` in the `answer` directory.
There is an incomplete solution to this homework in `answer/default.lex`.  You can create the `default`
binary as follows:

    cd your-repo-name/answer
    make default

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

Remember to push your solution source code to GitLab or other private repository:

    git add decafast.y decafast.lex # and any other files such as decafast.cc and decafast-defs.h
    git commit -m 'initial solution'
    git push


An abstract syntax tree (AST) is a high-level representation of the
program structure without the necessity of containing all the details
in the source code; it can be thought of as an abstract representation
of the source code.

The specification for the abstract syntax tree to be produced by your program is 
given below using the [Zehpyr Abstract Syntax Definition Language][1] (ASDL).

Modifiers on the argument type specify the number of values
needed; `?` means it is optional, `*` means 0 or more, no modifier
means only one value for the argument and it is required.

For `*` print a singleton for one element, or multiple
elements seperated by commas, or None for the zero element.

    module Decaf
    {
        prog = Program(extern* extern_list, package body)

        extern = ExternFunction(identifier name, method_type return_type, extern_type* typelist)

        decaf_type = IntType | BoolType

        method_type = VoidType | decaf_type

        extern_type  = StringType | decaf_type

        package = Package(identifier name, field_decl* field_list, method_decl* method_list)

        field_decl = FieldDecl(identifier name, decaf_type type, field_size size)
            | AssignGlobalVar(identifier name, decaf_type type, expr value)

        field_size = Scalar | Array(int array_size)

        method_decl = Method(identifier name, method_type return_type, typed_symbol* param_list, method_block block)

        typed_symbol = VarDef(identifier name, decaf_type type)

        method_block = MethodBlock(typed_symbol* var_decl_list, statement* statement_list)

        block = Block(typed_symbol* var_decl_list, statement* statement_list)

        statement = assign
            | method_call
            | IfStmt(expr condition, block if_block, block? else_block)
            | WhileStmt(expr condition, block while_block)
            | ForStmt(assign* pre_assign_list, expr condition, assign* loop_assign_list)
            | ReturnStmt(expr? return_value)
            | BreakStmt
            | ContinueStmt

        assign = AssignVar(identifier name, expr value)
            | AssignArrayLoc(identifier name, expr index, expr value)

        method_call = MethodCall(identifier name, method_arg* method_arg_list)

        method_arg = StringConstant(string value)
            | expr

        expr = rvalue
            | method_call
            | NumberExpr(int value)
            | BoolExpr(bool value)
            | BinaryExpr(binary_operator op, expr left_value, expr right_value)
            | UnaryExpr(unary_operator op, expr value)

        rvalue = VariableExpr(identifier name)
            | ArrayLocExpr(identifier name, expr index, expr value)

        bool = True | False

        binary_operator = Plus | Minus | Mult | Div | Leftshift | Rightshift | Mod | Lt | Gt | Leq | Geq | Eq | Neq | And | Or

        unary_operator = UnaryMinus | Not

    }

[1] Daniel C. Wang, Andrew W. Appel, Jeff L. Korn, and Chris S. Serra. The Zephyr Abstract Syntax Description Language. In Proceedings of the Conference on Domain-Specific Languages, pp.  213--227, 1997.

Make sure you obey the following requirements:

1. If your program succeeds in parsing the input you should exit from your program using `exit(EXIT_SUCCESS)`. And if your program finds an error in the input Decaf program you should exit using `exit(EXIT_FAILURE)`. The definitions of `EXIT_SUCCESS` and `EXIT_FAILURE` are in `cstdlib` (for C++) and in `stdlib.h` (for C).
1. The abstract syntax tree produced by your program must be in the format specified above. The output specification is also available as the file `Decaf.asdl` in the `decafast` directory.

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

You can use the default program provided to get an initial solution to this homework. Run `python zipout.py -r default` to get a `source.zip` file you can score.

    python check.py 
    Correct(dev): 39 / 124
    Score(dev): 39.00
    Total Score: 39.00

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

