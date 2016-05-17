---
layout: default
img: race
img_link: "http://www.flickr.com/photos/nationaalarchief/3198249977/"
caption: ""
title: Leaderboard
active_tab: leaderboard
jquery: true
---

Submit your assignments [here](http://sfu-yacc.appspot.com). Results will be updated in a few minutes.


<table class="table table-hover table-condensed">
  <thead>
    <tr>
      <th>
        Rank
      </th>
      <th>
        Handle
      </th>
      <th class="text-right">
        <a href="hw0.html">#0</a><br/><span class="small text-muted">Setup</span>
      </th>
<!--      
      <th class="text-right">
        <a href="hw1.html">#1</a><br/><span class="small text-muted">Segment</span>
      </th>
      <th class="text-right">
        <a href="hw2.html">#2</a><br/><span class="small text-muted">Chunk</span>
      </th>
      <th class="text-right">
        <a href="hw3.html">#3</a><br/><span class="small text-muted">Align</span>
      </th>
      <th class="text-right">
        <a href="hw4.html">#4</a><br/><span class="small text-muted">Decode</span>
      </th>
      <th class="text-right">
        <a href="hw5.html">#5</a><br/><span class="small text-muted">Rerank</span>
      </th>
-->
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>

<script type="text/javascript" src="leaderboard-code.js"></script>

<div id="loading">Loading...</div>

<div class="panel panel-default"> 
<div class="panel-heading">Legend</div> 

<div class="panel-body"> 

<p>A value of -1 indicates that the assignment file was found but
contained invalid content.</p>

<p>The highlighted lines are <span class="text-success">oracle (best possible)</span>,  
<span class="text-danger">default (performance of code provided to you if any; no marks)</span>
and <span class="text-success">baseline</span> which is the performance you should aim for.</p>

</div>

</div>

### Acknowledgements

The original leaderboard code for Google App Engine was developed by [Matt Post](https://github.com/mjpost) and [Adam Lopez](https://github.com/alopez).

