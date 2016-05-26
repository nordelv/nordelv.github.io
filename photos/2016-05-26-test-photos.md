---
layout: default
title: Photos d'Utö
tags: photo
---
<script>
var old_id = '';
var state = false

function showBig(id){
    var state_new = state;
    if (!state || old_id !=  id){
        var showBigItem = document.querySelector(id);
        showBigItem.classList.add("col-xs-12 col-sm-12 col-md-12");
        state_new = true;
    }
    if (((old_id==id && state) || old_id !=  id) && old_id != '') {
        var showNormalItem = document.querySelector(old_id);
        showNormalItem.classList.remove("col-xs-12 col-sm-12 col-md-12");
        state_new = (old_id !=  id);
    }
    state = state_new;
    old_id = id;
}

</script>

<section class="row">
<div class="thumbnails col-xs-6 col-sm-4 col-md-4" id="5F0A7051-1.jpg" onclick="showBig('#'+id)>
  <img src="/photos/2016-05-26-test/5F0A7051-1.jpg" class="img-rounded">
</div>
<div class="thumbnails col-xs-6 col-sm-4 col-md-4" id="5F0A7053-1.jpg" onclick="showBig('#'+id)>
  <img src="/photos/2016-05-26-test/5F0A7053-1.jpg" class="img-rounded">
</div>
<div class="thumbnails col-xs-6 col-sm-4 col-md-4" id="5F0A7061-1.jpg" onclick="showBig('#'+id)>
  <img src="/photos/2016-05-26-test/5F0A7061-1.jpg" class="img-rounded">
</div>
<div class="thumbnails col-xs-6 col-sm-4 col-md-4" id="5F0A7068-1.jpg" onclick="showBig('#'+id)>
  <img src="/photos/2016-05-26-test/5F0A7068-1.jpg" class="img-rounded">
</div>
<div class="thumbnails col-xs-6 col-sm-4 col-md-4" id="5F0A7072-1.jpg" onclick="showBig('#'+id)>
  <img src="/photos/2016-05-26-test/5F0A7072-1.jpg" class="img-rounded">
</div>
<div class="thumbnails col-xs-6 col-sm-4 col-md-4" id="5F0A7075-1.jpg" onclick="showBig('#'+id)>
  <img src="/photos/2016-05-26-test/5F0A7075-1.jpg" class="img-rounded">
</div>
</section>