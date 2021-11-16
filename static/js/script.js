window.onload =function setSlideImage(){
    document.getElementById("box1").style.left = 0 + "%";
    document.getElementById("box2").style.left = 100 + "%";
    document.getElementById("box3").style.left = 200 + "%";
    var imageScrollSpeed = 5000;
    setTimeout(function(){
      imageScroll();
    },5000);
}
/* Set positions of box divs before the scroll function is called */
