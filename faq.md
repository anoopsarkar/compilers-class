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

* We will be using the [discussion board on Coursys]({{ site.coursys }}discussion/) exclusively for **all** discussions including asking for help. 
* For syllabus, practice, homeworks, exams, or other clarification emails **do not** email me (the instructor) or the TA(s) directly.
* If you email the instructor directly for personal matters that are inappropriate for the discussion board, use your SFU email address to send the email (do not use any other provider), and use <code>cmpt379:</code> as the prefix in your subject line.
* Do not email the TAs directly (without cc:ing the instructor) under any circumstance.
* Before you email or post to the discussion board **read this FAQ**.

### How to ask a question

How to ask a question on the [discussion board on Coursys]({{ site.coursys }}discussion/):

* Do not ask two or more questions about different issues in the same topic. Ask each question as a separate topic.
* First check your code on a CSIL Linux machine. If the problem goes away then the issue is with your development environment.
* Describe your computing environment, e.g. Running Ubuntu Linux 16.04 and gcc version 5.4 on a VirtualBox VM. Depending on the complexity of your problem, more details might be required. If you are using a CSIL Linux machine just the hostname is sufficient.
* If you are using a Windows machine then installing Ubuntu on a virtual machine as using that as your dev environment is a good idea. We cannot offer help debugging your home computing environment.
* Do tell us what steps you take to invoke the problem, as well as what you've tried so far to fix it.
* Do not open a new issue if there already exists an older one that asks the same question. First read through any issues that seem related to your own question before you post on the discussion board. This will save everybody time.
* One skill to develop is how to ask a question that has a higher chance of being answered. In any situation, no matter how frustrated you might feel, it does not hurt to ask your question politely.  Read what you have written before you hit "Post" or "Reply". Add one polite word to one sentence if there are none. This will always help you in the long run.

### Grading

* The grade for the course is computed using the final marks which are a weighted average of each activity as defined on the [main page](index.html).
* The grade cutoff are as follows:

  | **Final Grade** | **Final marks** |
  | A+ | >95 |
  | A  | >90 |
  | A- | >85 |
  | B+ | >80 |
  | B  | >75 |
  | B- | >70 |
  | C+ | >65 |
  | C  | >60 |
  | C- | >55 |
  | D  | >50 |
  | F  | &le;50 |
  {: .table}

### Homework Submission and Grace Days
    
* You have to submit several deliverables for each homework as specified on the homework pages.
* Your homework solution will be submitted electronically on <a href="{{ site.coursys }}">Coursys</a>.
* Please include an `answer/README.md` file for any documentation outside of the source code especially for code obtained from elsewhere.
* All homeworks are due by 11:59PM on the homework due date.
* Each homework comes with 2 grace days. However the grace days only apply to those who have a valid submission on the due date. The default is usually a valid submission. For example, if your homework deadline is Tuesday 11:59PM and you submit a valid solution then you have until Thursday night 11:59PM to modify your homework submission.
* We will make every attempt to release grades for each homework as soon as possible. However, this means that after we review the source code we might have to lower your official grade. If you cheated in some way, such as copying your submission or you have violated the ground rules for each homework, your grades will be decreased from the initial value.
* To request an extension of the due date due to a medical problem, you must submit the [official SFU Certificate of Illness](http://www.sfu.ca/content/dam/sfu/students/pdf/certificate-of-illness.pdf). Depending on the circumstances you may still lose part of your marks if your medical problem was only for a small portion of the entire homework duration.

### CSIL
    
* [Remote access to CSIL](http://www.sfu.ca/computing/about/support/csil/unix/how-to-use-csil-linux-cpu-server.html) is allowed.
* CSIL computers accept SSH connections on port 24 (rather than the usual port 22) so use `ssh -p 24 csil-cpu1.csil.sfu.ca` to connect.
* If your local machine (e.g your laptop) has a different username from your SFU username (your username can be found by examining your SFU email address: username`sfu.ca), then prefix the SFU username to the ssh or scp command. `ssh (username)@fraser.sfu.ca`.
* You may want to refer to a quick Unix tutorial. There are several on the web. The following one covers most of what you need to use the Linux shell effectively: [Quick Unix Tutorial](http://www.ee.surrey.ac.uk/Teaching/Unix/index.html).
*  On some CSIL Linux machines, in some rare cases, you might have to extend your CPU time limit for a process. If you are using tcsh then run the command "limit cputime 1800" to extend CPU time to 1800 secs or 30 mins. If you are using bash then use the command "ulimit -t 1800".

#### Using the computer from the command line shell

In the instructions that follow, you will operate the computer using
the text-based command-line interface, known as the "shell". Start
off by reading [the CSIL guide to Linux](http://www.sfu.ca/computing/about/support/csil/unix.html){:target="_blank"}

Are you confident you know how to use the shell? Do [the shell challenge](shell_fu.txt)
to prove to yourself that you really know how to use the command shell.

Stop! We know that students skip over links! If you are
new to Linux, you really need to read up on some basics.
Read [the CSIL guide to Linux](http://www.sfu.ca/computing/about/support/csil/unix.html){:target="_blank"} now!

#### Logging in to CSIL

It's time to get yourself set up in the CSIL Lab.

CSIL is open starting the second week
of the semester, 24 hours a day, 7 days a week. 
Log in to the **Linux** machines.  

If you use the terminal server to login to Linux, you should see a familiar desktop interface.
In order to manipulate most of your work, you will need a terminal
window which runs the "shell". Your default shell will be "bash".

If you are using the terminal server, click the launcher in the upper-left corner of the desktop interface
and start the "Terminal Emulator" application, or Terminal for short.
It should be under the Accessories submenu.  If you can't find it,
then try searching for `Terminal` in the search box.

If you are using `ssh` to log into Linux at CSIL you will automatically
be on a Terminal, typically running `bash` as your shell.

The Terminal will allow you to type commands to manipulate, run and
test programs in your labs.  But there will be no programming in this lab.
In this lab you are going to use Git.

Just a heads up about the directory `$HOME/sfuhome` on CSIL machines. 
You should clone your repo inside your `$HOME` directory. You should not work inside your
`$HOME/sfuhome` directory.

### Exams

* If you must miss a quiz or exam because of a medical problem, you should make an attempt to contact me prior to the exam either by email or a message in my mailbox and you must submit the [official SFU Certificate of Illness](http://www.sfu.ca/content/dam/sfu/students/pdf/certificate-of-illness.pdf).
* If you miss an exam due to valid medical reasons you will be graded on your performance on the rest of the course. 
* **Make up exams will not be given under any circumstances**. 

### Academic Honesty

* Some examples of unacceptable behaviour:
    * Copying code from another student in your class.
    * Copying code from GitHub.
    * Copying code from Stack Overflow or other coding help websites.
    * Handing in assignments that are not 100% your own work (in design, implementation, wording, etc.), without proper citation. There must be a README file in your submission with citations to any external code used.
    * Using any unpermitted resources during an exam.
    * Looking at, or attempting to look at, another student's code or work during an exam or quiz.
    * Submitting work that has been submitted before, for any course at any institution.
* If you are unclear on what academic honesty is, see Simon Fraser University's [Policy S10-01](https://www.sfu.ca/policies/gazette/student/s10-01.html).
* All instances of academic dishonesty will be dealt with very severely.
* In general, minimum requested penalties will be as follows:
    * For assignments: a mark of -100% on the assignment. So, academic dishonesty on an assignment worth 5% of your final mark will result in a zero on the assignment, and a penalty of 5% from your final grade.
    * For exams: an F in the course.
    * Please note that these are minimum penalties. At the instructor's option, more severe penalties may be given/requested.  All instances of academic dishonesty will be noted on your University record.
* The instructor may use, or require students to submit assignments to, an automated service that will check for plagiarism.

### Exams and Tests

* If you miss a test or exam, you must present a note from a doctor to get a mark other than zero.  Arrangements to make up the lost marks will be made on a case-by-case basis by the instructor.  Make-up exams may be given as an oral examination.
* You must get a pass on the weighted average of the exams to pass the course.
* Disregard the following for this semester which has all activities online.
* For in-person exams:
    * Midterms may be in different rooms than the lectures.  You will be notified by email.
    * In person exams may be written in either pen or pencil.  Calculators or other aids are not allowed unless explicitly stated.
    * Midterm exams and other tests may or may not be returned, depending on the course.  If they are returned, you can get them from the instructor's office hours. You can not dispute the marking of your exam after you have taken it out of the instructor's office. 
    * Final exams are not returned to students by University policy; they are kept by the instructor.

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

### Final and Final Marks Appeals

If you're concerned about your mark at the end of the course, you can see the instructor.  Here are some guidelines:

* Like assignments, you can ask the instructor to reevaluate your final marking.
* The following are not good reasons to get a higher final mark:
    * I want it.
    * I think I deserve it.
    * I need it.
    * I'm close to the next grade cutoff.
* This is a good reason:
    * There's a marking irregularity on my final or some other piece of work.
* The marking scheme is fixed.  If you did badly on a midterm, you can't weight the final more heavily.
   
### Disclaimers about this web page

* All course information on this web page is tentative and could be in error. It can also change at any time. Confirm crucial dates or information with me in person during class. Double check with SFU calendar or schedule information for official class times and final exams time and location. 
* Students are expected to attend all classes: announcements about assigned readings, homeworks and exams will be made available at the start of each class. Such announcements may not be made on this web page, so don't rely on information here instead of attending class. 

### Easter egg

<img src="{{ site.baseurl }}/assets/img/puzzle.png" alt="Easter egg image" width="400"/>
