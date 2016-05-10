---
layout: default
img: green_dragon_book
img_link: "https://en.wikipedia.org/wiki/Principles_of_Compiler_Design"
caption: "Principles of Compiler Design, by Alfred Aho and Jeffrey Ullman, published in 1977, is the classic textbook on compilers."
title: Syllabus
active_tab: syllabus
---

## Syllabus

<style type="text/css">
    .bs-example{
        margin: 20px;
    }
</style>

<div class="bs-example">
    <div class="panel-group" id="accordion">
        {% for week in site.data.syllabus %}
            <div class="panel panel-default">
                <div class="panel-heading">
                    <h4 class="panel-title">
                        <a data-toggle="collapse" data-parent="#accordion" href="#{{ week.tag }}">{{ week.title }}</a>
                    </h4>
                </div>
                {% if week.current %}
                <div id="{{ week.tag }}" class="panel-collapse collapse in">
                {% else %}
                <div id="{{ week.tag }}" class="panel-collapse collapse">
                {% endif %}
                    <div class="well">
                        <div class="panel panel-default">
                          <div class="panel-heading">
                            <h3 class="panel-title">Lecture notes</h3>
                          </div>
                          <ul class="list-group">
                          {% for notes in week.notes %}
                            <li class="list-group-item"> <a href="{{ notes.url }}">{{ notes.title }}</a>
                                {%if notes.video %}
                                    <a href="{{ notes.video }}"><span class="glyphicon glyphicon-film"></span></a>
                                {% endif %}
                            </li>
                          {% endfor %}
                          </ul>
                          <div class="panel-heading">
                            <h3 class="panel-title">Links</h3>
                          </div>
                          <ul class="list-group">
                          {% for link in week.links %}
                            <li class="list-group-item"> <a href="{{ link.url }}">{{ link.title }}</a>.
                                {%if link.author %}
                                    {{ link.author }}.
                                {% endif %}
                                {%if link.citation %}
                                    {{ link.citation }}.
                                {% endif %}
                                {%if link.video %}
                                    <a href="{{ link.video }}"><span class="glyphicon glyphicon-film"></span></a>
                                {% endif %}
                            </li>
                          {% endfor %}
                          </ul>
                        </div>
                    </div>
                </div>
            </div>
        {% endfor %}
    </div>
</div>

