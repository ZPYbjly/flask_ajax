window.onload = init;
function init(){
   
    $('#notify').on('click',
        function() {
        //取变量
            var b= $("#options").val(); //单选框取值
            var date = $("#firedate").val();
            var data = {
            data: JSON.stringify({
            'date':date,
            'type': b
            }),
         }
 
        //小于11位提示
        
        
 
         //ajax 提交数据
 
        $.ajax({
            type: "POST",
            dataType: "json",
            url: "/aaa",//后端请求
            data: data,
            success: function(result) {
                console.log(result)
             },
            error: function (result) {
                console.log(result)
            }
        })
    
    })
 

}