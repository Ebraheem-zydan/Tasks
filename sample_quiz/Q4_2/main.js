let Light = document.getElementById("Light")
let Dark = document.getElementById("Dark")
Light.addEventListener("click",function(){
    getComputedStyle(document.documentElement).getPropertyValue('--backgroundColor');
    document.documentElement.style.setProperty('--backgroundColor', '#fff')

    getComputedStyle(document.documentElement).getPropertyValue('--whiteColor');
    document.documentElement.style.setProperty('--whiteColor', '#000')

    getComputedStyle(document.documentElement).getPropertyValue('--greenColor');
    document.documentElement.style.setProperty('--greenColor', '#ca4456')


})
Dark.addEventListener("click",function(){
    getComputedStyle(document.documentElement).getPropertyValue('--backgroundColor');
    document.documentElement.style.setProperty('--backgroundColor', '#1D1D1D')

    getComputedStyle(document.documentElement).getPropertyValue('--whiteColor');
    document.documentElement.style.setProperty('--whiteColor', '#fff')

    getComputedStyle(document.documentElement).getPropertyValue('--greenColor');
    document.documentElement.style.setProperty('--greenColor', '#6FCA44')


})