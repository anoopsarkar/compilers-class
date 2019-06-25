---
layout: default
img: llvm
img_link: "http://llvm.org/"
caption: "The LLVM Project is a collection of modular and reusable compiler and toolchain technologies. "
title: Course Information
active_tab: main_page 
---

## Compilers <span class="text-muted">Summer 2019</span>

As [Steve Yegge said](http://steve-yegge.blogspot.ca/2007/06/rich-programmer-food.html), "If you don't know how compilers work, then you don't know how computers work."  This is a course for those who are interested in the design and implementation of programming languages. Compilers let us use a high-level programming language by translating programs into low-level machine code. Understanding how compilers work is essential if you want to be a good programmer. In this course, you will build a working compiler using lex, yacc and LLVM (it's ok if you don't know what those terms mean).

#### Instructor
* [Anoop Sarkar](http://www.cs.sfu.ca/~anoop/) 

#### Time and place
* Tuesdays 10:30-11:20 [BLU-9660](http://www.sfu.ca/campuses/maps-and-directions/burnaby-map.html)
* Thursdays 09:30-11:20. **Note**: From July 2nd onwards we will meet in [AQ 3153](http://www.sfu.ca/campuses/maps-and-directions/burnaby-map.html). Until then we continue to meet in [SCK-9500](http://www.sfu.ca/campuses/maps-and-directions/burnaby-map.html)
* Last day of classes: {{ site.lastday }}

#### Teaching Assistants
<ul>
<li> Do <b>not</b> email TAs directly. Use the <a href="{{ site.coursys }}discussion/">discussion board</a> only.</li>
{% for ta in site.tas %}
<li>{{ ta.name }}, <code>{{ ta.email }}</code>, Office hour: {{ ta.officehour }}</li>
{% endfor %}
</ul>

#### News
* [News feed on Coursys](https://coursys.sfu.ca/news/75221d0252e1cdacf94dac56b78600e9/anoop)

#### Calendar
* [View Calendar](https://coursys.sfu.ca/calendar/)
* [Subscribe](https://coursys.sfu.ca/calendar/0261d2fe6030dc6570c3073ca9dd1a93/anoop)
* Subscribe to the URL in your calendaring app rather than saving the file and adding it manually.

#### Asking for help
* Ask for help on [the discussion board]({{ site.coursys }}/discussion)
* Instructor office hours: Thursdays 11:30am-12:30pm TASC1 9427
* TA office hours listed above
* Do not email the TAs directly (without cc:ing the instructor) under any circumstance.
* Use only SFU email address and use `cmpt379:` as subject prefix

#### Textbook
* No required textbook. Online readings provided in Syllabus.
* [List of reference books](textbook.html)

#### Grading
* Submit homework source code and check your grades on [Coursys]({{ site.coursys }})
* Programming setup homework: HW0 due on {{ site.hwdates[0].deadline }} (1%)
* Four programming homeworks. Due dates: HW1 on {{ site.hwdates[1].deadline }}, HW2 on {{ site.hwdates[2].deadline }}, HW3 on {{ site.hwdates[3].deadline }}, HW4 on {{ site.hwdates[4].deadline }} (56% total)
* Participation: Helping other students on the discussion board in a positive way (5%)
* In class midterm: {{ site.midterm }} (18%)
* Final exam: {{ site.finalexam }} (20%)

