//https://developer.mozilla.org/en-US/docs/Web/API/Document

// var header = document.querySelector("h1");
// var p1 = document.getElementsByClassName("p1");
// var p2 = document.getElementById("p2");

// header.innerHTML = "Integer pharetra dui eu orci aliquam, cursus imperdiet justo eleifend.";
// p1[0].innerHTML = "Integer pharetra dui eu orci aliquam, cursus imperdiet justo eleifend.";
// p2.innerHTML = "Integer pharetra dui eu orci aliquam, cursus imperdiet justo eleifend.";

// var alink = document.querySelector("a");

// console.log(alink.getAttribute("href"));

// alink.setAttribute("href","https://www.techreport.us");

var headOne = document.querySelector('#h1')
var headTwo = document.querySelector('#h2')

// Hover (mouseover and mouseout)
headOne.addEventListener('mouseover',function(){
  headOne.textContent = "Mouse currently Over";
  headOne.style.color = 'red';
})

headOne.addEventListener('mouseout',function(){
  headOne.textContent = "Mouse Not On me."
  headOne.style.color = 'blue';
})

// On Click
headTwo.addEventListener("click",function(){
  headTwo.textContent = "Clicked On";
  headTwo.style.color = 'blue';
})
