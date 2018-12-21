var fibonacci = function(n) {
    if(n <2){
      return n;
    }
    else{
      return fibonacci(n-1) + fibonacci(n-2);
    }
};

var heading = document.getElementById("h");
var list = document.getElementById("thelist");

//mouse hovering over -> element becomes heading
list.addEventListener('mouseover', function(e){
  heading.innerHTML = e['target'].innerHTML;
});

//mouse off heading "Hello World!"
list.addEventListener('mouseout', function(){
  heading.innerHTML = "Hello World";
});

//click to remove
list.addEventListener('click', function(e){
  e['target'].remove();
});