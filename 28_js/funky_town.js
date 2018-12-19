/* 
 Team Awoooo - Jeffrey Wu and Britni Canale
 SoftDev1 pd6
 K28 - Sequential Progression
 2018-12-19   
*/

var fibonacci = function(n) {
    if(n <2){return n;}
    else{return fibonacci(n-1) + fibonacci(n-2);}
};

var gcd = function(a,b){
    if (a == b){
        return a;
    }
    else if (a > b){ return gcd(b,a-b);}
    else{return gcd(a,b-a);}
}

var students = ['Jeffrey','Britni','Thomas', 'Tim','Damian']
var randomStudent = function(){
    return students[Math.floor(Math.random()*students.length)]
}