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
