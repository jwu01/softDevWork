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
var button = document.getElementById('b');
var fibButt = document.getElementById('fb');
var fibList = document.getElementById("fiblist")

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

button.addEventListener('click',function(){
  console.log('word')
  var li = document.createElement('li');
  li.innerHTML = "WORD";
  list.appendChild(li);
});

var count = 0; 
fibButt.addEventListener('click',function() {
 var li = document.createElement('li');
 li.innerHTML = fibonacci(count);
 fibList.appendChild(li);
 count++;
});

var power2 = document.createElement('ol');
var body =  document.getElementsByTagName('body')[0];
body.appendChild(power2);
var twoBut = document.createElement('button');
twoBut.innerHTML = "powers of 2";
body.appendChild(twoBut);

var twoCount = 0;
twoBut.addEventListener('click', function(){
  var li = document.createElement('li');
  li.innerHTML = 2 ** twoCount;
  li.setAttribute('style', "color: #" + twoCount % 10 + 'AAA' + (10 -twoCount) % 10 + 'A');
  power2.appendChild(li);
  twoCount++;
})
