
  var fibonacci = function(n) {
    var sum = [0,1]
    for (var i = 2; i <= n; i++) 
      sum.push(sum[i-2] + sum[i-1]);
    sum[n]
  };
  
  var gcd = function(a,b) {
    while(a!=b)
    {
        if(a>b)
            a=a-b;
        else
            b=b-a;
    }
    return a
  };
  var students = ['joe','bob','mary','addison','dennis','andrew','tyler','jessica','karen','vincent','allen']
  var randomStudent = function(){
    students[parseInt(Math.random() * students.length)];
  };

  f = document.getElementById('fibb')
  g = document.getElementById('gcd')
  r = document.getElementById('randomS')

  f.addEventListener('click',function(){
      console.log(fibonacci(13));
      document.getElementById("message").innerHTML = 'Fibonnacci of 13 is ' + fibonacci(13);
    });
  r.addEventListener('click',function(){
      console.log(randomStudent());
      document.getElementById("message").innerHTML = 'Random student is ' + randomStudent();
    });
  g.addEventListener('click',function(){
      console.log(gcd(2019,3365));
      document.getElementById("message").innerHTML = 'The GCD of 2019 and 3365 is ' + gcd(2019,3365);
    });