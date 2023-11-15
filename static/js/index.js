// $("div").addClass("main-preview");
// $("div").addClass("first-preview");
// $("div").addClass("second-preview");
alert("hello");

function display_c(){

    var refresh=1000; // Refresh rate in milli seconds
    mytime=setTimeout('display_time()', refresh)
    }

function display_time() {

    var x = new Date()
    document.getElementById('time').innerHTML = x;
    display_c();
    }