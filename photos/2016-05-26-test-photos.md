---
layout: photos
title: Photos test
tags: photo
---
<ul>
    <li onclick="disp('#q1')" id="q1">One</li>
    <li onclick="disp('#w')" id="w">Two</li>
    <li onclick="disp('#e')" id="e">Three</li>
    <li onclick="disp('#r')" id="r">Four</li>
    <li onclick="disp('#t')" id="t">Five</li>
    <li id="y" onclick="disp('#'+id)">Six</li>
</ul>

<img src="http://img0.mxstatic.com/wallpapers/8daae8e966248ff339b3310f6fcde6fe_large.jpeg" alt="Mountain View" id="dfdfd" onclick="disp('#'+id)">

<p>Click the button to trigger a function that will output "Hello World" in a p element with id="demo".</p>

<button onclick="myFunction()">Click me</button>

<p id="demo"></p>

<script>
var old_id = '';
var state = false

function myFunction() {
    document.getElementById("demo").innerHTML = state;
}

function printId(id){
alert(id);
}

function disp(id){
    var state_new = state;
    if (!state || old_id !=  id){
        var rmItem = document.querySelector(id);
        rmItem.classList.add("col-md-1");
        state_new = true;
    }
    if (((old_id==id && state) || old_id !=  id) && old_id != '') {
        var addItem = document.querySelector(old_id);
        addItem.classList.remove("disableMenu");
        state_new = (old_id !=  id);
    }
    state = state_new;
    old_id = id;
}

</script>


<section class="row">
<div class="thumbnails" id="a5F0A7051-1.jpg" onclick="disp('#'+id)">
  <img src="/photos/2016-05-26-test/5F0A7051-1.jpg" class="img-rounded">
</div>
<div class="thumbnails col-xs-6 col-sm-4 col-md-4" id="a5F0A7053-1.jpg" onclick="showBig('#'+id)">
  <img src="/photos/2016-05-26-test/5F0A7053-1.jpg" class="img-rounded">
</div>
<div class="thumbnails col-xs-6 col-sm-4 col-md-4" id="a5F0A7061-1.jpg" onclick="showBig('#'+id)">
  <img src="/photos/2016-05-26-test/5F0A7061-1.jpg" class="img-rounded">
</div>
<div class="thumbnails col-xs-6 col-sm-4 col-md-4" id="a5F0A7068-1.jpg" onclick="showBig('#'+id)">
  <img src="/photos/2016-05-26-test/5F0A7068-1.jpg" class="img-rounded">
</div>
<div class="thumbnails col-xs-6 col-sm-4 col-md-4" id="a5F0A7072-1.jpg" onclick="showBig('#'+id)">
  <img src="/photos/2016-05-26-test/5F0A7072-1.jpg" class="img-rounded">
</div>
<div class="thumbnails col-xs-6 col-sm-4 col-md-4" id="a5F0A7075-1.jpg" onclick="showBig('#'+id)">
  <img src="/photos/2016-05-26-test/5F0A7075-1.jpg" class="img-rounded">
</div>
</section>
