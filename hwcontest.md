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
<p class="text-muted">Due on {{ site.hwdates[5].deadline }}</p>
<p class="text-muted">With grace days due on {{ site.hwdates[5].gracedays }}</p>

## Your Task

1. Create at least 10 new testcases and at most 50 testcases that are distinct from the provided testcases for the homeworks (hw1-hw4). They must pass validation (see below).
1. Your testcases must pass and are expected to produce valid LLVM output that when compiled to binary produce some output after execution of the binary. 
1. Testcases expected to fail cannot be submitted to the contest. (_this rule might be dropped_)
1. The submission file for the Compiler Contest will be uploaded to Coursys.
1. No fuzzing allowed. The testcases are expected to be hand checked or sanitized even if you used an automated method to generate them.

## The Contest

### Testcase format

This section specifies the testcase directory structure.

1. The testcase format must be identical to the format for the homeworks, particularly [hw3](hw3.html) and [hw4](hw4.html). 
1. In your answer directory create two new directories: `testcases/your-name` and `references/your-name` where `your-name` is the name you have been using for the leaderboard.
1. The directory `testcases/your-name` should contain the Decaf source files named with a `.decaf` file name suffix.
1. The directory `references/your-name` should contain the Decaf source files named with a `.out` file name suffix.
1. You can create the contents of directory `references/your-name` by running `python zipout.py -t answer/testcases` and copying over the `.out` files to your references (sub)directory.

### Validation Phase

1. Each testcase must be in the right format (see "Testcase format" section above).
1. The first phase of the contest will be a validation phase where I examine your output and make a decision about your program and the output being consistent with the Decaf spec.
1. I can remove any testcases from your submission if I consider them to be too similar to existing testcases from previous homeworks or if they are invalid or they produce the wrong output. 
1. My decision on accepting testcases is final and cannot be contested.
1. After I remove bad testcases, each submission that has at least 10 testcases remaining will be tested in the contest.
1. If there are more than 50 remaining testcases, I will take the first 50 based on lexicographic sort.

### Grace Days

1. There are two grace days for the compiler contest. 
1. These will be used to provide some feedback on the quality of the testcases.
1. However, the submitted testcases and compiler will not be run against the entire set of testcases to provide a full auto-grade of the contest. Only the number of testcases that passed the "Validation Phase" (see above) will be reported for each submission.

## Ground Rules

* The scripts `zipsrc.py`, `zipout.py` and `zipcontest.py` are available in the `decafcomp` directory from my `compilers-class-hw` repository. See the "Getting Started" section in [hw4](hw4.html) for details on the repository.
* You must turn in three things:
    * Your source code from the `answer` directory as a zip file `source.zip` produced by running `python3 zipsrc.py` must be uploaded to the `Final Project` submission page on [Coursys]({{ site.coursys }}).
    * Your output on the testcases which is the file `output.zip` produced by running `python3 zipout.py` must be uploaded to the `Final Project` submission page on [Coursys]({{ site.coursys }}). When we run `check.py` on the public testcases it should have a value higher than the output from the default program to get any marks.
    * Your testcases for the Compiler Contest which is the file `contest.zip` produced by running `python3 zipcontest.py` must be uploaded to the `Final Project` submission page on [Coursys]({{ site.coursys }}). When we run `check.py` on the public testcases it should have a value higher than the output from the default program to get any marks.
* Your source code from `source.zip` must be on your gitlab repository.
* Make sure that we can run `make decafcomp` in your answer directory to create the `decafcomp` binary.
* You cannot use data or code resources outside of what is provided to you. If you use external code snippets provide citations in the `answer/README.md` file.
* For the written description of your submission and supporting documentation, you can use plain ASCII but for math equations it is better to use kramdown. Do not use any proprietary or binary file formats such as Microsoft Word.

### Grading

1. The compiler from each participating submission will be run on all the collected testcases. 
1. Your compiler will be graded based on how many testcases were successfully passed and how many of your testcases were failed by other compilers in the contest.

