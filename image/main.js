function factorial(){
    num=parseInt(document.getElementById("num").value)
    res=1
    for(let i=2;i<=num;i++){
        res*=i
    }
    message="Factorial of "+num+"is"+res
    document.getElementById("res").innerHTML="<h2>"+message+"</h2>"
}
function digitsum()
{
    num=parseInt(document.getElementById("num").value)
    message="";
    s=0;
    num1=num
    if(num){
        while(num!=0){
            s+=parent(num%10)
            num=parsent(num/10)
        }
    }
}