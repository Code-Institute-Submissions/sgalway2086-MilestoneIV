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
function imageScroll(imageScrollSpeed){
    var scrollTimer = 0;
    var pause = 0;
    pause = pause + 1000;
    for (let i = 0; i < 100; i++){
      var scrollTimer = scrollTimer + 10;
      setTimeout(function(){
          for(let j = 0; j < 3; j++){
            let intergerCreater = document.getElementsByClassName("scrollBox")[j].style.left;
            intergerCreater = intergerCreater.replace("%", "");
            intergerCreater = intergerCreater - 1;
            document.getElementsByClassName("scrollBox")[j].style.left = intergerCreater + "%";
        }
      },scrollTimer);
    }
    setTimeout(function(){
      for(let i = 0; i < 3; i++){
        let leftStyleChecker = document.getElementsByClassName("scrollBox")[i].style.left;
        leftStyleChecker = leftStyleChecker.replace("%", "");
        if(leftStyleChecker <= -100){
          document.getElementsByClassName("scrollBox")[i].style.left = 200 + "%";
        }
      }
    },pause);
    setTimeout(function(){
      imageScroll();
    },5000);
  }
  
  /* times and creates the scrolling effect of the 3 divs on the main page */