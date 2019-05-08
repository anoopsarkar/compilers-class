---
layout: default
img: hopper_univac 
img_link: "https://en.wikipedia.org/wiki/Grace_Hopper"
caption: "Grace Hopper developed the first compiler for a computer programming language."
title: Homework | Setup
active_tab: homework
---

# Homework & Leaderboard setup

<p class="text-muted">Start on {{ site.hwdates[0].startdate }}</p>
<p class="text-muted">Due on {{ site.hwdates[0].deadline }}</p>

For this course, we use [an automated homework submission
system](http://sfu-yacc.appspot.com)[^1] built on [Google App
Engine](https://appengine.google.com). One component of this system
is the [leaderboard](leaderboard.html) which allows you to
check on your progress. It is not intended to be a competition.

[^1]: In this case, `yacc` stands for Yet Another Compilers Course.

You should follow the steps in this document to make sure that
everything is working for you.

1. Visit the course submission page at
[sfu-yacc.appspot.com](http://sfu-yacc.appspot.com). You 
will need a valid Google account.

2. This system is used to upload all homework assignments. You
should use a handle when you submit your
assignment. By default the leaderboard will use your Google nickname
which cannot be used to assign you a grade.

3. Homework 0 (this one) has been activated. Create a file called `hw0.txt` with a single number in it. 
Use the file submission dialog to upload your submission. Check your status on the [leaderboard](leaderboard.html)

4. Create a tar.gz or zip file called `hw0.tgz` or `hw0.zip` containing the text file you uploaded. Upload your archive file as the HW0 submission on [Coursys](https://courses.cs.sfu.ca/2016su-cmpt-379-d1/+hw0/).  In future assignments you will be uploading your source code and documentation as your submission.

## Homework 0

The Homework 0 leaderboard upload expects a text file containing a
single number. The leaderboard displays a simple nonmonotonic
function of this number, and sorts the entries according to the
highest value.

To get full marks, you must do the following:

* Upload your file on [the upload page](http://sfu-yacc.appspot.com/). **Do not use multiple logins to submit your assignment.**

<!-- There will be a dialog
that says this is the final submission (you can no longer upload
after you _Submit_ your final answer. Do __not__ press _Submit_ if
you plan to keep uploading new submissions. 
-->

* You **must** use a valid handle.

* You must upload your text file inside a zip file as the HW0
submission on [Coursys](https://courses.cs.sfu.ca). You can create a zip file like this:

    zip hw0coursys.zip your-file.txt

In future homeworks, you will submit your output files to the [upload page on Google](http://sfu-yacc.appspot.com) and submit your
source code to the submission page on [Coursys](https://courses.cs.sfu.ca).

