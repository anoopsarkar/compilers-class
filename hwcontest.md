---
layout: default
img: race
img_link: "http://www.flickr.com/photos/nationaalarchief/3198249977/"
caption: "Compiler Contest"
title: Compiler Contest
active_tab: homework
---

# Compiler Contest 

<p class="text-muted">Start on {{ site.hwdates[5].startdate }}</p>
<p class="text-muted">Part 1 due on {{ site.hwdates[5].deadline }}</p>
<p class="text-muted">With grace days, Part 1 due on {{ site.hwdates[5].gracedays }}</p>
<p class="text-muted">Part 2 due on {{ site.hwdates[6].deadline }}</p>

## Your Task

1. **Part 1.** Create at least 10 new testcases and at most 20 testcases that are distinct from the provided testcases for the homeworks (hw1-hw4). They must pass validation (see below).
  1. Your testcases should be valid Decaf code which is not expected to crash. Each one should produce some output when it is executed. Each main method must return `int` and not `void` or `bool`.
  1. Your grade for part 1 depends on how many of your testcases pass validation.
1. **Part 2.** After the testcases have been validated, you will receive a zipfile containing anonymized versions all of the submitted testcases which passed validation. You must run your compiler on these cases and submit the output to Coursys.
  1. Your grade for part 2 depends on how many of the testcases your compiler passes, and how difficult your testcases are for other students' compilers.

Please note:
1. Grace days are only available for Part 1. There is a hard deadline on December 10 for the submission of Part 2.
1. Both parts will be submitted to Coursys. 
1. Testcases expected to fail cannot be submitted to the contest.
1. No fuzzing allowed. The testcases are expected to be hand checked or sanitized even if you used an automated method to generate them.

## The Contest

### Part 1: Testcase format

This section specifies the testcase directory structure.

1. The testcase format must be identical to the format for the homeworks, particularly [hw3](hw3.html) and [hw4](hw4.html). 
1. In your `testcases/` directory create two new subdirectories: `testcases/your-name` and `references/your-name` where `your-name` is your SFU username.
1. The directory `testcases/your-name` should contain your new Decaf source files named with a `.decaf` file name suffix. If your programs require user input, also include `.in` files containing the inputs that will be piped to your programs.
1. The directory `references/your-name` should contain the outputs from running your testcases, named with a `.out` file name suffix.
1. You can create the contents of directory `references/your-name` by running `python zipout.py -t answer/testcases` and copying over the `.out` files to your references (sub)directory.
1. Running `python3 zipcontest.py` will produce `contest.zip` which is the file you will submit for this part of the contest.
1. An example of what `unzip -l contest.zip` should look like in terms of the directory structure is shown [in this gist](https://gist.github.com/anoopsarkar/a68e0e2249373da4be03dd0498c8bc0b). This directory structure is important for the contest auto-grading scripts to be able to read your `contest.zip` correctly.

### Validation Phase

After you have submitted your testcases, we will validate them for use in Part 2:
1. Each testcase must be in the right format (see "Testcase format" section above).
2. Each testcase must have a `main` method that returns `int`, not `void` or `bool`.
3. I will validate your testcases by running them through a reference implementation of the Decaf compiler. A testcase will pass just in case the expected output in your `.out` file matches the output from our reference compiler.
  1. All testcases must compile within 1 minute and may not require more than 256 MB memory. Cases which exceed these limits will not pass validation.
4. I can remove any testcases from your submission if they do not follow the Decaf specification or if they produce the wrong output. 
5. My decision on accepting testcases is final and cannot be contested.
6. After I remove bad testcases, each submission that has at least 10 testcases remaining will be tested in the contest.
7. If you submit more than 20 testcases which pass validation, I will take only the first 20 based on lexicographic sort.
8. You will earn 1 point for each testcase which passes validation, to a maximum of 10 points.

### Part 2: Testing Phase

1. On the morning of December 9th, I will distribute a zipfile containing all of the testcases which passed validation. Check the Coursys discussion for a pinned post with a link to the download.
1. Unzip the provided zipfile to your `testcases` directory. This will create a directory `testcases/contest` containing the (anonymized) submissions to Part 1.
1. Your only task is to run your compiler on these testcases and upload the outputs to Coursys. If you unzip the new cases to `testcases/contest`, you can run them by calling `python3 zipout.py` as usual.
1. Like the `dev` cases for past homeworks, you will not have access to the expected output for these testcases. (Except for those cases that you submitted.)
1. You will earn 1 point for each testcase on which your compiler produces the correct output. You will earn 1 bonus point each time one of your testcases causes another student's compiler to crash or produce the wrong output. The maximum number of bonus points you can earn is 10% of the overall grade.
1. You can modify you compiler as much as you like until you receive the full set of testcases from us (this is after the Validation Phase when you receive the testcases from us for the contest). 
1. This part of the contest is meant to test your compiler, and not as an opportunity to improve your compiler. Once you get the full set of testcases for the compiler contest you should run your compiler on the testcases and upload the resulting zip file to Coursys. In this short period you can debug small errors, but your main task is to finish getting the answers. If your compiler produces LLVM code that goes into an infinite loop or takes too long to finish (greater than a few minutes), it is your job to find those testcases and remove them so that you can get output on as many Decaf programs in the contest as you can. There will be no extensions or grace days provided in this stage.


### Grace Days

1. There are two grace days for Part 1 (creating the testcases). There are no grace days for Part 2 (running your code on the testcases).
1. The grace days for Part 1 will be used to provide feedback on the quality of the testcases. If your initial submission does not contain 10 valid testcases, you can revise your testcases during the grace period.

## Ground Rules

* The scripts `zipsrc.py`, `zipout.py` and `zipcontest.py` are available in the `decafcomp` directory from my `compilers-class-hw` repository. See the "Getting Started" section in [hw4](hw4.html) for details on the repository.
* For Part 1, you must turn in one thing:
    * Your testcases for the Compiler Contest (the file `contest.zip` produced by running `python3 zipcontest.py`) must be uploaded to the `Project testcases` submission page on [Coursys]({{ site.coursys }}).
* For Part 2, you must turn in two things:
    * Your source code from the `answer` directory as a zip file `source.zip` (produced by running `python3 zipsrc.py`) must be uploaded to the `Final Project` submission page on [Coursys]({{ site.coursys }}).
    * Your output on the contest testcases (which is the file `output.zip` produced by running `python3 zipout.py` after unzipping the new cases) must be uploaded to the `Final Project` submission page on [Coursys]({{ site.coursys }}). 
* Your source code from `source.zip` must also be pushed to your gitlab repository.
* Make sure that we can run `make decafcomp` in your answer directory to create the `decafcomp` binary.
* You cannot use data or code resources outside of what is provided to you. If you use external code snippets provide citations in the `answer/README.md` file.
* For the written description of your submission and supporting documentation, you can use plain ASCII but for math equations it is better to use kramdown. Do not use any proprietary or binary file formats such as Microsoft Word.

### Grading

1. In Part 1, you will earn 1 point for each testcase which passes validation, to a maximum of 10 points.
1. In Part 2, you will earn 1 point for each testcase on which your compiler produces the correct output. You will earn 1 bonus point each time one of your testcases causes another student's compiler to crash or produce the wrong output. The maximum number of bonus points you can earn is 10% of the overall grade.
