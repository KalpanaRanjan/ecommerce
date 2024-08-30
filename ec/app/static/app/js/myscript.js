$('.plus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var a=this.parentNode.children[2];
    console.log("pid =" ,id);
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log("data = ",data );
            a.innerText=data.quantity
            document.getElementById("totalamount").innerText=data.totalamount
            document.getElementById("amount").innerText=data.amount
        }
    })
})

$('.minus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var a=this.parentNode.children[2];
    console.log("pid =" ,id);
    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log("data = ",data );
            a.innerText=data.quantity
            document.getElementById("totalamount").innerText=data.totalamount
            document.getElementById("amount").innerText=data.amount
        }
    })
})

$('.remove-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var a=this
    console.log("pid =" ,id);
    $.ajax({
        type:"GET",
        url:"/removecart",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log("data = ",data );
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
            a.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})