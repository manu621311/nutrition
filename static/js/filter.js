/*$(document).ready(function(){
    $(document).on('submit','#submitForm',function(e){
        e.preventDefault();
        var search_text=$('input[name="search_text"]').val();
        var url='/request?item='+search_text;
    })
})*/
var select=document.getElementById("submit");
function filter(){
    var text=document.getElementById("search_text");
    var url='/request?search_text='+text.value;
    var xhttp=new XMLHttpRequest();
    xhttp.open('GET',url,true);
    xhttp.send();
    xhttp.onreadystatechange=function(){
        if(this.readyState==4 && this.status==200){
            alert(this.responseText);
        }
    };
    //xhttp.setRequestHeader('Content-type','application/x-www-form-urlencoded');
}
select.addEventListener('click',function(event){
    event.preventDefault();
    filter();
},false);