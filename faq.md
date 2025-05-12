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

* We will be using the [discussion forum on Coursys]({{ site.coursys }}forum/) exclusively for **all** discussions including asking for help. 
* For syllabus, practice, homeworks, exams, or other clarification emails **do not** email me (the instructor) or the TA(s) directly.
* If you email the instructor directly for personal matters that you do not wish to share with the TA then you must use your SFU email address to send the email (do not use any other provider), and use <code>cmpt379:</code> as the prefix in your subject line.
* Do not email the TAs directly (without cc:ing the instructor) under any circumstance.
* Before you email or post to the discussion forum **read this FAQ**.

### How to ask a question

How to ask a question on the [discussion forum on Coursys]({{ site.coursys }}forum/):

* Do not ask two or more questions about different issues in the same topic. Ask each question as a separate topic.
* First check your code on a CSIL Linux machine. If the problem goes away then the issue is with your development environment.
* Describe your computing environment, e.g. Running Ubuntu Linux 22.04 and gcc version 5.4 on a VirtualBox VM. Depending on the complexity of your problem, more details might be required. If you are using a CSIL Linux machine just the hostname is sufficient.
* If you are using a Windows machine then installing Ubuntu on a virtual machine as using that as your dev environment is a good idea. We cannot offer help debugging your home computing environment.
* Do tell us what steps you take to invoke the problem, as well as what you've tried so far to fix it.
* Do not open a new issue if there already exists an older one that asks the same question. First read through any issues that seem related to your own question before you post on the discussion forum. This will save everybody time.
* One skill to develop is how to ask a question that has a higher chance of being answered. In any situation, no matter how frustrated you might feel, it does not hurt to ask your question politely.  Read what you have written before you hit "Post" or "Reply". Add one polite word to one sentence if there are none. This will always help you in the long run.
* Remember that there is part of the grade dedicated to being helpful on the discussion board.

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
* Each homework comes with 2 grace days unless otherwise specified. However the grace days only apply to those who have a valid submission on the due date. The default is usually a valid submission. For example, if your homework deadline is Monday 11:59PM and you submit a valid solution then you have until Wednesday night 11:59PM to modify your homework submission. The only exception is the final project submission that has no grace days.
* We will make every attempt to release grades for each homework as soon as possible. However, this means that after we review the source code we might have to lower your official grade. If you cheated in some way, such as copying your submission or you have violated the ground rules for each homework, your grades will be decreased from the initial value.
* To request an extension of the due date due to a medical problem, you must submit the [official SFU Certificate of Illness](https://www.sfu.ca/content/dam/sfu/students/academicsuccess/academicconcessions/2022-SFU_AcademicConcession_SelfDeclarationForm.pdf). Depending on the circumstances you may still lose part of your marks if your medical problem was only for a small portion of the entire homework duration.

### Groups

* The homework assignments will be solved in groups. Groups are upto 3 people. All groups must be formed before the Homework 0 due date.
* You are allowed to leave a group and form a group of size one at the start of each homework but not at the end.
* Each group will create a single submission and upload it to Coursys on or before the due date.
* Each group member will be graded on their self report and any commit logs that are submitted. If the TA or the instructor perceives there is a problem with collaboration in a group, certain group members can get zero marks. If you are pair programming, take turns in switching the user doing the commits to the repository.
* __Effective group collaboration__: We are looking to see effective collaboration to solve the homework assignment. People can play different roles and sometimes more than one role in the same homework:
    * Designer: creates a plan for implementation and coordinates activities of the group. Should create design docs (text files or markdown or equivalent only). Put these documents in the directory `docs` and mention the files in your `README.username` file (where `username` is your SFU login username).
    * Code reviews: write a critical view of the implementation by the group. Points out what is missing, inelegant code, etc. and produces a code review document (text files or markdown or equivalent only). Put these documents in the directory `docs` and mention the files in your `README.username` file.
    * Development: write the code. This can be done in collaboration.
    * Testcases: write testcases to stress test the code. Provide the testcases in your submission.
* **Warning**: if you are missing a `README.username` file in your group source submission then that `username` might get zero marks.
* Use `git` for version control and effective collaboration. See the section below on setting up `git` for this course.
* Keep an eye out for comments from the instructor or TAs on your GitLab code repository for each homework.

### Academic Honesty

* Some examples of unacceptable behaviour in homeworks:
    * Handing in assignments that are not 100% your own work (in design, implementation, wording, etc.), without proper citation. There must be a README file in your submission with citations to any external code used.
    * Sharing code fragments with others in class is not allowed.
    * Keep discussions to high level information rather than specific code hints.
    * Copying and then obfuscating code is a serious academic honesty violation.
    * Submitting work that has been submitted before, for any course at any institution.
* Some examples of unacceptable behaviour in exams:
    * Using any unpermitted resources during an exam.
    * Looking at, or attempting to look at, another student's paper during an exam.
* If you are unclear on what academic honesty is, see Simon Fraser University's [Policy S10-01](https://www.sfu.ca/policies/gazette/student/s10-01.html).
* All instances of academic dishonesty will be dealt with very severely.
* In general, minimum requested penalties will be as follows:
    * For assignments: a mark of -100% on the assignment. So, academic dishonesty on an assignment worth 5% of your final mark will result in a zero on the assignment, and a penalty of 5% from your final grade.
    * For exams: an F in the course.
    * Please note that these are minimum penalties. At the instructor's option, more severe penalties may be given/requested.  All instances of academic dishonesty will be noted on your University record.
* The instructor may use an automated service that will check for plagiarism.

### CSIL

* SSH via the SFU VPN is the [remote access method](https://www.sfu.ca/computing/about/support/csil/remote-access.html) support.
* CSIL computers sometimes accept SSH connections on port 24 (rather than the usual port 22) so use `ssh -p 24 csil-cpu1.csil.sfu.ca` to connect.
* If your local machine (e.g your laptop) has a different username from your SFU username (your username can be found by examining your SFU email address: username`sfu.ca), then prefix the SFU username to the ssh or scp command. `ssh (username)@(machinename).sfu.ca`.
* You may want to refer to a quick Unix tutorial. There are several on the web. The following one covers most of what you need to use the Linux shell effectively: [Quick Unix Tutorial](http://www.ee.surrey.ac.uk/Teaching/Unix/index.html).
*  On some CSIL Linux machines, in some rare cases, you might have to extend your CPU time limit for a process. If you are using tcsh then run the command "limit cputime 1800" to extend CPU time to 1800 secs or 30 mins. If you are using bash then use the command "ulimit -t 1800".
* Professional Masters students have access to the lab machines in SECB 1010 and SECB 1013. Those machines have RTX 4000 GPUs. See [Computing Support](https://www.sfu.ca/computing/about/support/csil/change-log.html).

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

CSIL is open starting the second week of the semester, 24 hours a day, 7 days a week. Log in to the **Linux** machines.  Use
the same username and password as before.

The machines in these rooms have Linux and Windows installed. If you a machine running Windows, simply restart the machine and select Linux when prompted.

Once logged into Linux, you should see a familiar desktop interface.  In order to manipulate most of your work, you will need a terminal window which runs the "shell".

Click the launcher in the upper-left corner of the desktop interface and start the "Terminal Emulator" application, or Terminal for short.  It should be under the Accessories submenu.  If you can't find it, then try searching for `Terminal` in the search box.

The Terminal will allow you to type commands to manipulate, run and test programs in your labs.  But there will be no programming in this lab.  In this lab you are going to use Git.

Just a heads up about the directory `$HOME/sfuhome` on CSIL machines.  You should clone your repo inside your `$HOME` directory. You should not work inside your `$HOME/sfuhome` directory.

### Exams

* If you must miss an quiz or homework because of a medical problem, you should make an attempt to contact me prior to the exam either by email or a message in my mailbox and you must submit the [official SFU Certificate of Illness](http://www.sfu.ca/content/dam/sfu/students/pdf/certificate-of-illness.pdf).
* If you miss an activity due to valid medical reasons you will be graded on your performance on the rest of the course.
* **Make up exams will not be given under any circumstances**.

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

### Final Marks Appeals

If you're concerned about your mark at the end of the course, you can talk to the instructor.  Here are some guidelines:

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

### Disclaimers about this web page

* All course information on this web page is tentative and could be in error. It can also change at any time. Confirm crucial dates or information with me in person during class. Double check with SFU calendar or schedule information for official class times and final exams time and location.
* Students are expected to attend all classes: announcements about assigned readings, homeworks and exams will be made available at the start of each class. Such announcements may not be made on this web page, so don't rely on information here instead of attending class.

### Easter egg

<img src="{{ site.baseurl }}/assets/img/emesida.png" alt="Easter egg image" width="400"/>
