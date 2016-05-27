var old_id = '';
var state = false

function showBig(id){
    var state_new = state;
    if (!state || old_id !=  id){
        var showBigItem = document.querySelector(id);
        showBigItem.classList.remove("col-xs-6");
        showBigItem.classList.remove("col-sm-4");
        showBigItem.classList.remove("col-md-4");
        showBigItem.classList.add("col-xs-12");
        showBigItem.classList.add("col-sm-12");
        showBigItem.classList.add("col-md-12");
        state_new = true;
    }
    if (((old_id==id && state) || old_id !=  id) && old_id != '') {
        var showNormalItem = document.querySelector(old_id);
        showNormalItem.classList.remove("col-xs-12");
        showNormalItem.classList.remove("col-sm-12");
        showNormalItem.classList.remove("col-md-12");
        showNormalItem.classList.add("col-xs-6");
        showNormalItem.classList.add("col-sm-4");
        showNormalItem.classList.add("col-md-4");
        state_new = (old_id !=  id);
    }
    state = state_new;
    old_id = id;
}

function myFunction() {
    document.getElementById("demo").innerHTML = "coucou";
}

function void(){

        showBigItem.classList.remove("col-xs-6");
        showBigItem.classList.remove("col-sm-4");
        showBigItem.classList.remove("col-md-4");
        showBigItem.classList.add("col-xs-12");
        showBigItem.classList.add("col-sm-12");
        showBigItem.classList.add("col-md-12");
}
