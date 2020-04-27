var select=document.getElementById("submit");
var cal=2000;
var tot_fat=50;
var pro=56;
var cho=300;//mg
var carb=250;
var fib=38;

function filter(){
    var x=document.getElementById("correction");
    x.style.display="none";
    var text=document.getElementById("search_text");
    var url='/request?search_text='+text.value;
    var xhttp=new XMLHttpRequest();
    xhttp.open('GET',url,true);
    xhttp.send();
    xhttp.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            var obj=JSON.parse(this.responseText);
            display(obj);
        }
    };
    //for post:xhttp.setRequestHeader('Content-type','application/x-www-form-urlencoded');
}
select.addEventListener('click',function(event){
    event.preventDefault();
    var text=document.getElementById("search_text").value;
    if(text==""){
        var x=document.getElementById("correction");
        x.style.display="block";
    }
    else{
        filter();
    }
},false);
function display(obj){
    console.log(obj);
    document.getElementById("image").src=obj.image;
    document.getElementById("detail").innerText=obj.detail;
    var chart_css=document.getElementById("chart_css");
    chart_css.style.display="block";
    var serving_size=document.getElementById("serving_size");
    serving_size.innerText="Serving Size:"+obj.serving_size+"g.";
    var calorie=document.getElementById("cal");
    calorie.style.width=(obj.calories*100/cal).toString()+"%";
    calorie.innerText=(obj.calories).toString();
    var total_fat=document.getElementById("tot_fat");
    total_fat.style.width=(obj.total_fat*100/tot_fat).toString()+"%";
    total_fat.innerText=(obj.total_fat).toString()+"g";
    var protein=document.getElementById("pro");
    protein.style.width=(obj.protein*100/pro).toString()+"%";
    protein.innerText=(obj.protein).toString()+"g";
    var cholestrol=document.getElementById("cho");
    cholestrol.style.width=(obj.cholestrol*100/cho).toString()+"%";
    cholestrol.innerText=(obj.cholestrol).toString()+"mg";
    var carbs=document.getElementById("carb");
    carbs.style.width=(obj.carbohydrates*100/carb).toString()+"%";
    carbs.innerText=(obj.carbohydrates).toString()+"g";
    var fibres=document.getElementById("fib");
    fibres.style.width=(obj.fiber*100/fib).toString()+"%";
    fibres.innerText=(obj.fiber).toString()+"g";
}
