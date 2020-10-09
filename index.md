---
layout: default
img: llvm
img_link: "http://llvm.org/"
caption: "The LLVM Project is a collection of modular and reusable compiler and toolchain technologies. "
title: Course Information
active_tab: main_page 
---

## Compilers <span class="text-muted">Fall 2020</span>

As [Steve Yegge said](http://steve-yegge.blogspot.ca/2007/06/rich-programmer-food.html), "If you don't know how compilers work, then you don't know how computers work."  This is a course for those who are interested in the design and implementation of programming languages. Compilers let us use a high-level programming language by translating programs into low-level machine code. Understanding how compilers work is essential if you want to be a good programmer. In this course, you will build a working compiler using lex, yacc and LLVM (it's ok if you don't know what those terms mean).

#### Instructor
* [Anoop Sarkar](https://anoopsarkar.github.io) 

#### Time and place
* Mon-Wed-Fri 09:30-10:20am PST on Zoom (link will be posted on the course <a href="{{ site.coursys }}discussion/">discussion board</a>).
* Last day of classes: {{ site.lastday }}

#### Teaching Assistants
<ul>
<li> Do <b>not</b> email TAs directly. Use the <a href="{{ site.coursys }}discussion/">discussion board</a> only.</li>
{% for ta in site.tas %}
<li>{{ ta.name }}, <code>{{ ta.email }}</code>, Office hour: {{ ta.officehour }}</li>
{% endfor %}
</ul>

#### News
* [News feed on Coursys](https://coursys.sfu.ca/news/)

#### Calendar
* [View Calendar](https://coursys.sfu.ca/calendar/)
* [Subscribe](https://coursys.sfu.ca/news/75221d0252e1cdacf94dac56b78600e9/anoop)
* Subscribe to the URL in your calendaring app rather than saving the file and adding it manually.

#### Asking for help
* Ask for help on [the discussion board]({{ site.coursys }}/discussion)
* TA office hours listed above
* Use the discussion board for all interaction with the instructor and TAs (except personal issues)
* Do **not** email the TAs directly (without cc:ing the instructor) under any circumstance. 
* Use only SFU email address while sending emails and use `cmpt379:` as subject prefix

#### Textbook
* No required textbook. Online readings provided in Syllabus.
* [List of reference books](textbook.html)

#### Grading
* Submit homework source code and check your grades on [Coursys]({{ site.coursys }})
* Programming setup homework: HW0 due on {{ site.hwdates[0].deadline }} (1%)
* Four programming homeworks. (56% total)
    * HW1 on {{ site.hwdates[1].deadline }} [with grace days: {{ site.hwdates[1].gracedays }}] (10%), 
    * HW2 on {{ site.hwdates[2].deadline }} [with grace days: {{ site.hwdates[2].gracedays }}] (12%), 
    * HW3 on {{ site.hwdates[3].deadline }} [with grace days: {{ site.hwdates[3].gracedays }}] (14%), 
    * HW4 on {{ site.hwdates[4].deadline }} [with grace days: {{ site.hwdates[4].gracedays }}] (20%) 
* Participation: Helping other students **on the discussion board** in a positive way (5%)
* Online quiz performance. (18% total; Best 4 out of 5; Each quiz is worth 4.5%)
    * Quiz 0 on {{ site.quiz[0].date }} (practice quiz; no marks)
    * Quiz 1 on {{ site.quiz[1].date }}
    * Quiz 2 on {{ site.quiz[2].date }}
    * Quiz 3 on {{ site.quiz[3].date }}
    * Quiz 4 on {{ site.quiz[4].date }}
    * Quiz 5 on {{ site.quiz[5].date }}
* Final: [Compiler Contest](hwcontest.html) {{ site.hwdates[5].deadline }} (20%) **No grace days for final submission**

