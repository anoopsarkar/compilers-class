---
layout: default
img: knuthpaper
img_link: "https://en.wikipedia.org/wiki/LR_parser"
caption: "LR parsers were invented by Donald Knuth in 1965."
title: FAQ
active_tab: faq
---

## (in) Frequently Asked Questions

### Email policy

* We will be using the discussion board on courses.cs.sfu.ca for all discussions. For homeworks, exams, or other clarification emails do not email me (the instructor) or the TA directly.
* If you email the instructor or TA directly then use your SFU email address to send the email (do not use any other provider), and use <code>cmpt379:</code> as the prefix in your subject line.

### Homework Submission and Grace Days
    
* Your group has to submit two deliverables for each homework:
    * A zip or tar file of your Source code for your homework has to be submitted electronically on [courses.cs.sfu.ca](https://courses.cs.sfu.ca/2016su-cmpt-379-d1/). Always include a `README` file in `answer/docs` that contains a documentation of your development process.
    * The output on the provided testcases has to be uploaded to the leaderboard server on [Google App Engine](http://sfu-yacc.appspot.com/).
* Only one member of the group should upload to the leaderboard and use the valid group name.
* Check your scores on the leaderboard and check that your group appears only once in the leaderboard.
* All homeworks are due by 11:59PM on the homework due date.
* Each homework comes with 2 grace days. However the grace days only apply to those who have a valid submission on the due date (a submission that scores -1 or -inf is invalid). For example, if your homework deadline is Tuesday 11:59PM and you submit a valid solution then you have until Thursday night 11:59PM to modify your homework submission.
* We will make every attempt to release grades for each homework the day after grace days are past. However, this means that after we review the source code we might have to lower your official grade. If you cheated in some way, such as copying your submission or you have violated the ground rules for each homework, your grades will be decreased from the initial value perhaps even lowered to zero.

### Groups
    
* The homework assignments will be solved in groups. Maximum group size is two. All groups must be formed before Homework 0 is due.
* Each group will create a single submission and upload it before the due date.
* If the TA or the instructor perceives there is a problem with collaboration in a group, certain group members can get zero marks. If you are pair programming, take turns in switching the user doing the commits to your git or svn or mercurial repository.
* __Effective group collaboration__: We are looking to see effective collaboration to solve the homework assignment. People can play different roles and sometimes more than one role in the same homework:
    * Designer: creates a plan for implementation and coordinates activities of the group. Should create design docs (text files or markdown or equivalent only). Put these documents in the directory `answer/docs` and mention the files in your `README` file.
    * Code reviews: write a critical view of the implementation by the group. Points out what is missing, inelegant code, etc. and produces a code review document (text files or markdown or equivalent only). Put these documents in the directory `answer/docs` and mention the files in your `README` file.
    * Development: write the code. This can be done in collaboration. 
    * Testcases: write testcases to stress test the code. Provide the testcases in your submission.

### Programming
    
* It is your responsibility to use a source code management system such as git or mercurial or svn for keeping track of changes to your code and for effective collaboration in your group.
* It is expected that your program will compile and run using the standard runtime environment on the Linux CSIL lab machines. If you are developing on a Linux, Apple or Microsoft operating system at home, you have to ensure that the code will run on the CSIL machines before you submit the assignment. Please either visit the CSIL lab machines or you can use `ssh` to login to the CSIL Linux machines and also use `scp` to copy over and test your programs on the CSIL Linux machines before you submit them. Check the [CSIL Layout Maps](http://www.sfu.ca/computing/about/support/csil.html) for the machine names.
* [Remote access to CSIL](http://www.sfu.ca/computing/about/support/csil/how-to-remote-access-to-csil.html) is allowed.
* [Linux terminal server](http://www.sfu.ca/computing/about/support/csil/unix/how-to-use-csil-linux-terminal-server.html) is currently in beta.
* CSIL computers accept SSH connections on port 24 (rather than the usual port 22). They can only be accessed from within the SFU network. If you are outside it, you need to go through a directly accessable computer, most likely fraser.sfu.ca. Here are some examples using the usual command line `ssh` and `scp` (from OpenSSH). Below $ is the command line shell on your home computer running Linux/MacosX/Cygwin. What follows is a recipe that will connect you remotely to a CSIL Linux machine: <script src="https://gist.github.com/4486532.js"></script> 
* If your local machine (e.g your laptop) has a different username from your SFU username (your username can be found by examining your SFU email address: username`sfu.ca), then prefix the SFU username to the ssh or scp command. `ssh (username)@fraser.sfu.ca`.
* You can copy files to CSIL machines via `fraser.sfu.ca` using the following script:
 <script src="https://gist.github.com/4486537.js"></script> 
* You may want to refer to a quick Unix tutorial. There are several on the web. The following one covers most of what you need to use the Linux shell effectively: [Quick Unix Tutorial](http://unlser1.unl.csi.cuny.edu/tutorials/QuickUnixTutorial.html).
*  On some CSIL Linux machines, in some rare cases, you might have to extend your CPU time limit for a process. If you are using tcsh then run the command "limit cputime 1800" to extend CPU time to 1800 secs or 30 mins. If you are using bash then use the command "ulimit -t 1800".
    
### Exams

* If you must miss an exam because of a medical problem, you should make an attempt to contact me prior to the exam either by email or a message in my mailbox. 
* To request an extension of the due date due to a medical problem, you must submit the <a href="http://students.sfu.ca/forms.html">offical SFU Health Care Provider statement</a>. 
* If you miss an exam due to valid medical reasons you will be graded on your performance on the rest of the course. 
* **Make up exams will not be given under any circumstances**. 

### Disclaimers about this web page

* All course information on this web page is tentative and could be in error. It can also change at any time. Confirm crucial dates or information with me in person during class. Double check with SFU calendar or schedule information for official class times and final exams time and location. 
* Students are expected to attend all classes: announcements about assigned readings, homeworks and exams will be made available at the start of each class. Such announcements may not be made on this web page, so don't rely on information here instead of attending class. 

### Academic Honesty

* Some examples of unacceptable behaviour:
    * Handing in assignments that are not 100% your own work (in design, implementation, wording, etc.), without proper citation. There must be a README file in your submission with citations to any external code used.
    * Using any unpermitted resources during an exam.
    * Looking at, or attempting to look at, another student's paper during an exam.
    * Submitting work that has been submitted before, for any course at any institution.
* If you are unclear on what academic honesty is, see Simon Fraser University's [Policy S10-01](https://www.sfu.ca/policies/gazette/student/s10-01.html).
* All instances of academic dishonesty will be dealt with very severely.
* In general, minimum requested penalties will be as follows:
    * For assignments: a mark of -100% on the assignment. So, academic dishonesty on an assignment worth 5% of your final mark will result in a zero on the assignment, and a penalty of 5% from your final grade.
    * For exams: an F in the course.
    * Please note that these are minimum penalties. At the instructor's option, more severe penalties may be given/requested.  All instances of academic dishonesty will be noted on your University record.
* The instructor may use, or require students to submit assignments to, an automated service that will check for plagiarism.
     
### Exams and Tests

* Midterms may be in different rooms than the lectures.  You will be notified by email.
* Exams may be written in either pen or pencil.  Calculators or other aids are not allowed unless explicitly stated.
* Midterm exams and other tests may or may not be returned, depending on the course.  If they are returned, you can get them from the instructor's office hours. You can not dispute the marking of your exam after you have taken it out of the instructor's office. 
* Final exams are not returned to students by University policy; they are kept by the instructor.
* If you miss a test or exam, you must present a note from a doctor to get a mark other than zero.  Arrangements to make up the lost marks will be made on a case-by-case basis by the instructor.  Make-up exams may be given as an oral examination.
* You must get a pass on the weighted average of the exams to pass the course.
     
### Mark Appeals

Except for final grades, this is how you can go about getting your mark changed:

* Requests for a change in your mark must come to the course instructor.  Teaching Assistants will not change your mark, except for errors in addition or data entry.
* Requests should come in the same form as you received your marks: if you got marks by email, forward that email to the instructor; if you had paper handed back, return that.
* You should give a brief explanation of why you want your mark reevaluated.
* The instructor will remark the entire assignment/test.  This will be your mark, whether it is higher or lower than the original.
* Appeals may be made up to two weeks after the mark is returned or until the final exam date, whichever is <em>first</em>.  After that deadline, you must make a formal mark appeal for any changes.
* For exams in particular, these are not reasons to get more marks:
    * I knew what I was saying here, but didn't write it.
    * This is the correct answer for some question other than the one asked, but I didn't get any marks for it.
    * I didn't understand the question.
     
### Final Exam and Final Marks Appeals

If you're concerned about your mark at the end of the course, you can see the instructor.  Here are some guidelines:

* You can come to the instructor's office at designated times to review your final exam.
* Like assignments, you can ask the instructor to reevaluate your final exam marking.
* The following are not good reasons to get a higher final mark:
    * I want it.
    * I think I deserve it.
    * I need it.
    * I'm close to the next grade cutoff.
* This is a good reason:
    * There's a marking irregularity on my final or some other piece of work.
* The marking scheme is fixed.  If you did badly on a midterm, you can't weight the final more heavily.
   
