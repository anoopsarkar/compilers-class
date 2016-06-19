---
layout: default
img: green_dragon_book
img_link: "https://en.wikipedia.org/wiki/Principles_of_Compiler_Design"
caption: "Principles of Compiler Design, by Alfred Aho and Jeffrey Ullman, published in 1977, is the classic textbook on compilers."
title: LLVM Practice
active_tab: practice
---

## Code Generation with LLVM: Practice Problems

### Clone the repository

The files below and other example programs are available in a git repository

You must have git and python (2.7) on your system. Once you've confirmed this, run this command:

    git clone https://github.com/anoopsarkar/compilers-class-hw.git

If you have already cloned the repository earlier you can
get the new homework files by going to the directory
where you cloned the repository earlier and then doing:

    # go to the directory where you did a git clone earlier
    git pull origin master

Then go to the `llvm-practice` directory

    cd /your-path-to/compilers-class-hw/llvm-practice

### Install LLVM

We will be using LLVM version 3.8.0 for the homeworks in this course offering.
LLVM 3.8 has already been installed in the CSIL Linux machines. You can use
this version by using `llvm-config-3.8` in your makefile.

You can also install LLVM on your own machine by following the links on
this page:

    http://llvm.org/releases/download.html

### Decaf standard library

The file `decaf-stdlib.c` contains the standard library for Decaf and it contains
the implementation of functions like `print_int`, `read_int`, etc.

Write a C or C++ program that uses the functions defined in `decaf-stdlib.c`.

For example, add these lines to a test C or C++ program and compile by linking
with `decaf-stdlib.c`:

    int i = read_int();
    print_string("this is a test:");
    print_int(i);
    print_string("\n");

We will link the Decaf standard library with the x86 assembly that will
be generated using LLVM.

### Hello World in LLVM Assembly

LLVM is both a library for code generation and also a definition of an abstract
assembly language which is used as an intermediate representation for code
generation and code optimization that is machine independent. 

LLVM assembly is converted into x86 machine code. The file `helloworld.ll`
contains a simple Hello, World program in LLVM assembly.

    ; Declare the string constant as a global constant. 
    ; run the following command to run this LLVM assembly program:
    ; sh run-llvm-code.sh helloworld.ll 
    @LC0 = internal constant [13 x i8] c"hello world\0A\00"
    ; note how the newline character is inserted into the string

    ; External declaration of the puts function 
    declare i32 @puts(i8*)

    ; Definition of main function
    define i32 @main() {
      ; Convert [13 x i8]* to i8*
      ; this is because the function puts takes a char* which is an i8* in LLVM
      %cast = getelementptr [13 x i8], [13 x i8]* @LC0, i8 0, i8 0
      ; read up on getelementptr: http://llvm.org/docs/GetElementPtr.html

      ; Call puts function to write out the char* string to stdout. 
      call i32 @puts(i8* %cast)
      ret i32 0 
    }

`i8` is an 8-bit integer used by LLVM for ASCII characters. The `puts` function
takes an ASCII string and returns an integer return value of type `i32`.
Except for the `getelementptr` instruction the rest is easy to follow. The next
question explains the use of the `getelementptr` to access global constants.
The LLVM assembly file can be converted into executable machine code using the
following steps (also in the shell script `run-llvm-code.sh`). 

    llvmconfig=llvm-config-3.8
    b=`basename -s .ll helloworld.ll`
    `$llvmconfig --bindir`/llvm-as helloworld.ll  # convert LLVM assembly to bitcode
    `$llvmconfig --bindir`/llc helloword.bc   # convert LLVM bitcode to x86 assembly
    gcc helloworld.s -o helloworld

You can now run the binary `helloworld`.

In this case we did not need to link with the Decaf standard library
since we do not use any of the function in it, but when we implement
the Decaf compiler it will be easier to use the standard library functions instead of
a function like `puts` which take pointers as arguments.

### LLVM Assembly with Decaf Library Functions

The following LLVM assembly code defines a function `@add1` that adds
two integers and prints out the value followed by a newline.


    declare void @print_int(i32)
    declare void @print_string(i8*)
    declare i32 @read_int()

    ; store the newline as a string constant
    ; more specifically as a constant array containing i8 integers
    @.nl = constant [2 x i8] c"\0A\00"

    define i32 @add1(i32 %a, i32 %b) {
    entry:
      %tmp1 = add i32 %a, %b
      ret i32 %tmp1
    }

    define i32 @main() {
    entry:
      %tmp5 = call i32 @add1(i32 3, i32 4)
      call void @print_int(i32 %tmp5)
      ; convert the constant newline array into a pointer to i8 values
      ; using getelementptr, arg1 = @.nl, 
      ; arg2 = first element stored in @.nl which is of type [2 x i8]
      ; arg3 = the first element of the constant array
      ; getelementptr will return the pointer to the first element
      %cast.nl = getelementptr [2 x i8], [2 x i8]* @.nl, i8 0, i8 0
      call void @print_string(i8* %cast.nl)
      ret i32 0
    }

Write down a recursive version of the addition function in LLVM assembly. The
following Python program illustrates the algorithm.

    def rec_add(a, b):
        if a == 0:
            return b
        else:
            return rec_add(a-1, b+1)

The following template illustrates the use of a conditional expression
for branching and the use of a recursive function call. 

    define i32 @add2(i32 %a, i32 %b) {
    entry:
      %tmp1 = icmp eq i32 %a, 0
      br i1 %tmp1, label %done, label %recurse
    recurse:
      ; insert LLVM assembly here  
    done:
      ; insert LLVM assembly here
    }

It checks whether the first argument to the `add2` function is equal to zero
and sets a boolean location `%tmp1` to a boolean value (booleans in LLVM are of
type `i1` or integer of bit width 1).  The `br` call then branches either to
`%done` or `%recurse` based on the value in the boolean condition variable
`%tmp1`. Extend this template to write the LLVM assembly for recursive
addition.

### Factorial in LLVM 

Implement the factorial function in LLVM assembly and print out the value of
`11!` using `print_int`.

### LLVM API for Code Generation: First Steps

Before you do this practice problem, make sure you have a working symbol
table implementation as specified in [HW3](hw3.html).

The following yacc program fragment does code generation using the LLVM API.
The full source code is available in the file `sexpr-codegen.y`. 

    %union{
      class ExprAST *ast;
      int number;
    }

    %token <number> NUMBER
    %type <ast> expression
    %%
    statement: expression
               { 
                 Value *RetVal = $1->Codegen();
                 Function *print_int = gen_print_int_def();
                 Function *TheFunction = gen_main_def(RetVal, print_int);
                 verifyFunction(*TheFunction);
               }
               ;
    expression: expression '+' NUMBER 
                { 
                  $$ = new BinaryExprAST('+', $1, new NumberExprAST($3));
                }
              | expression '-' NUMBER 
                { 
                  $$ = new BinaryExprAST('-', $1, new NumberExprAST($3)); 
                }
              | NUMBER 
                { 
                  $$ = new NumberExprAST($1); 
                }
              ;
    %%

It takes simple expressions like `2+3-4` and produces LLVM assembly as output.

    declare i32 @print_int(i32)
    define i32 @main() {
    entry:
      %calltmp = call i32 @print_int(i32 1)
      ret i32 0
    }

It does this by extending your code for building an abstract syntax tree (AST).
For example, binary expressions are represented as the following AST data
structure:

    /// BinaryExprAST - Expression class for a binary operator.
    class BinaryExprAST : public ExprAST {
      char Op;
      ExprAST *LHS, *RHS;
    public:
      BinaryExprAST(char op, ExprAST *lhs, ExprAST *rhs) 
        : Op(op), LHS(lhs), RHS(rhs) {}
      virtual Value *Codegen();
    };

The code is then generated from the AST by calling functions defined in the
LLVM API. Two main data structures contain the LLVM assembly code:

static Module *TheModule;
static IRBuilder<> Builder(getGlobalContext());

    int main() {
      // initialize LLVM
      LLVMContext &Context = getGlobalContext();
      // Make the module, which holds all the code.
      TheModule = new Module("module for very simple expressions", Context);
      // parse the input and create the abstract syntax tree
      yyparse();
      // Print out all of the generated code to stderr
      TheModule->dump();
      exit(0);
    }

The generated code is produced as a pointer to a data structure
called `Value`. For example the following function is
used to generate code for binary expressions.

    Value *BinaryExprAST::Codegen() {
      Value *L = LHS->Codegen();
      Value *R = RHS->Codegen();
      if (L == 0 || R == 0) return 0;
      
      switch (Op) {
      case '+': return Builder.CreateAdd(L, R, "addtmp");
      case '-': return Builder.CreateSub(L, R, "subtmp");
      }
    }

Extend the code provided to you in `sexpr-codegen.y` in order
to handle LLVM code generation for the following grammar:

    statement_list: statement ';' statement_list
                  | /* empty */
                  ;
    statement: NAME '=' expression
             | NAME '(' expression ')'
             ;
    expression: expression '+' NUMBER 
              | expression '-' NUMBER 
              | expression '+' NAME 
              | expression '-' NAME 
              | NUMBER 
              | NAME 
              ;     

It should accept input like the following:

    a=2+3;
    b=5-2;
    c=a+b;    
    print_int(c+2);

And produce LLVM assembly:

    define i32 @main() {
    entry:
      %a = alloca i32
      store i32 5, i32* %a
      %b = alloca i32
      store i32 3, i32* %b
      %a1 = load i32* %a
      %b2 = load i32* %b
      %addtmp = add i32 %a1, %b2
      %c = alloca i32
      store i32 %addtmp, i32* %c
      %c3 = load i32* %c
      %addtmp4 = add i32 %c3, 2
      %calltmp = call i32 @print_int(i32 %addtmp4)
      ret i32 0
    }

You will need to use your symbol table implementation to store
the location of the variables. Also, use the LLVM `alloca`
instruction to create storage on the stack for the variables
in our simple programming language.


