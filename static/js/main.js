	function subtract(){
			time--;
			$(".time").html(time);
			if(time==0){
				location.href="../login";
			}
			setTimeout(subtract, 1000);
		}
	function splitMessage(){
	$.ajax({
				url: '../json',
				type: 'GET',
				dataType: 'json',
				success:function(data){
					var content=data.message[0].content;//这是一字符串
					var strs= new Array(); //定义一数组
					var strs2= new Array();
					var strs3= new Array();
					strs=content.split("!"); //字符分割
					for (i=0;i<strs.length ;i++ )
					{
						strs2=strs[i].split(";"); //字符分割
						for(j=0;j<strs2.length;j++){
							 strs3=strs2[j].split(","); //字符分割
								for(k=0;k<strs3.length;k++){
									$("#main .publish:eq(3)").append("<div>"+strs3[k]+"</div>")
								}
						}
					}
				}
			});
	}
	function Leftscroll(){
		$("#personal").animate({left:"-60%"},500);
		$("#header").animate({left:0},500);
		$("#footer").animate({left:0},500);
		$("#all").animate({left:0},500);
	}
	function Rightscroll(){
		$("#personal").animate({left:0},500);
		$("#all").animate({left:"60%"},500);
		$("#footer").animate({left:"60%"},500);
		$("#header").animate({left:"60%"},500);
	}
	function timedCount(){
		var c=0;
		var t;
		function time(){
			 var temptextmin=document.getElementById('order_time');
			hour = parseInt(c / 3600);// 小时数
			min = parseInt(c / 60);// 分钟数
			if(min>=60){
				minmin=min%60
			}
			lastsecs = c % 60;
			c=c+1;
			temptextmin.innerHTML = hour + ":" + min + ":" + c;
			t=setTimeout(time,1000)
		}
       time();
	}

	//日历插件初始化
function datePickerscroll(){
	var date = new Date();
   	date.setMinutes(date.getMinutes()+30);
   	var inputDate=$('input:jqmData(role="datebox")');
 	inputDate.mobiscroll().datetime();
 	inputDate.mobiscroll("setDate",date,true);
}
function lock_make(){
	  var R = 26, CW = 400, CH = 320, OffsetX = 30, OffsetY = 30;
        function CaculateNinePointLotion(diffX, diffY) {
            var Re = [];
            for (var row = 0; row < 3; row++) {
                for (var col = 0; col < 3; col++) {
                    var Point = {
                        X: (OffsetX + col * diffX + ( col * 2 + 1) * R),
                        Y: (OffsetY + row * diffY + (row * 2 + 1) * R)
                    };
                    Re.push(Point);
                }
            }
            return Re;
        }
        var PointLocationArr = [];
        window.onload = function () {
            var c = document.getElementById("myCanvas");
            CW = document.body.offsetWidth;
            c.width = CW;
            c.height = CH;
            var cxt = c.getContext("2d");
            //两个圆之间的外距离 就是说两个圆心的距离去除两个半径
            var X = (CW - 2 * OffsetX - R * 2 * 3) / 2;
            var Y = (CH - 2 * OffsetY - R * 2 * 3) / 2;
            PointLocationArr = CaculateNinePointLotion(X, Y);
            InitEvent(c, cxt);
            //CW=2*offsetX+R*2*3+2*X
            Draw(cxt, PointLocationArr, [],null);
        }
        function Draw(cxt, _PointLocationArr, _LinePointArr,touchPoint) {
            if (_LinePointArr.length > 0) {
                cxt.beginPath();
                for (var i = 0; i < _LinePointArr.length; i++) {
                    var pointIndex = _LinePointArr[i];
                    cxt.lineTo(_PointLocationArr[pointIndex].X, _PointLocationArr[pointIndex].Y);
                }
                cxt.lineWidth = 10;
                cxt.strokeStyle = "#627eed";
                cxt.stroke();
                cxt.closePath();
                if(touchPoint!=null)
                {
                    var lastPointIndex=_LinePointArr[_LinePointArr.length-1];
                    var lastPoint=_PointLocationArr[lastPointIndex];
                    cxt.beginPath();
                    cxt.moveTo(lastPoint.X,lastPoint.Y);
                    cxt.lineTo(touchPoint.X,touchPoint.Y);
                    cxt.stroke();
                    cxt.closePath();
                }
            }
            for (var i = 0; i < _PointLocationArr.length; i++) {
                var Point = _PointLocationArr[i];
                cxt.fillStyle = "#627eed";
                cxt.beginPath();
                cxt.arc(Point.X, Point.Y, R, 0, Math.PI * 2, true);
                cxt.closePath();
                cxt.fill();
                cxt.fillStyle = "#ffffff";
                cxt.beginPath();
                cxt.arc(Point.X, Point.Y, R - 3, 0, Math.PI * 2, true);
                cxt.closePath();
                cxt.fill();
                if(_LinePointArr.indexOf(i)>=0)
                {
                    cxt.fillStyle = "#627eed";
                    cxt.beginPath();
                    cxt.arc(Point.X, Point.Y, R -16, 0, Math.PI * 2, true);
                    cxt.closePath();
                    cxt.fill();
                }

            }
        }
        function IsPointSelect(touches,LinePoint)
        {
            for (var i = 0; i < PointLocationArr.length; i++) {
                var currentPoint = PointLocationArr[i];
                var xdiff = Math.abs(currentPoint.X - touches.pageX);
                var ydiff = Math.abs(currentPoint.Y - touches.pageY);
                var dir = Math.pow((xdiff * xdiff + ydiff * ydiff), 0.5);
                if (dir < R ) {
                    if(LinePoint.indexOf(i) < 0){ LinePoint.push(i);}
                    break;
                }
            }
        }
        function InitEvent(canvasContainer, cxt) {
            var LinePoint = [];
            canvasContainer.addEventListener("touchstart", function (e) {
                IsPointSelect(e.touches[0],LinePoint);
            }, false);
            canvasContainer.addEventListener("touchmove", function (e) {
                e.preventDefault();
                var touches = e.touches[0];
                IsPointSelect(touches,LinePoint);
                cxt.clearRect(0,0,CW,CH);
                Draw(cxt,PointLocationArr,LinePoint,{X:touches.pageX,Y:touches.pageY});
            }, false);
            canvasContainer.addEventListener("touchend", function (e) {
                cxt.clearRect(0,0,CW,CH);
                Draw(cxt,PointLocationArr,LinePoint,null);
                alert("密码结果是："+LinePoint.join("->"));
                LinePoint=[];
            }, false);
        }
}
$(function(){
	//name�»�
	$(".order_list .name").click(function(){
		$(".order_list .hide").slideDown();
	});
	//closeup����
	$(".order_list .closeup").click(function(){
		$(".order_list .hide").slideUp();
	});

	//判断home表单内容类型
	//产品重量和运费
	var float=/^(-?\d+)(\.\d+)?$/;
	var telephone=/^1[0-9]{10}$/;
	$(".order_list td input").keyup(function(){
		if($(this).attr("id")=="product_weight"||$(this).attr("id")=="freight"){
			if(float.test($(this).val())==false){
				$(".error_prompt").insertBefore($(this).closest("tr"));
				$(".error_prompt").show();
				$(".error_prompt td").html("对不起，请输入浮点数类型！");
			}else{
				$(".error_prompt").hide();
			}
		}
		if($(this).attr("id")=="destination_phone"){
			if(telephone.test($(this).val())==false){
				$(".error_prompt").insertBefore($(this).closest("tr"));
				$(".error_prompt").show();
				$(".error_prompt td").html("对不起，您的手机号码格式不正确！");
			}else{
				$(".error_prompt").hide();
			}
		}

		if($(this).attr("id")=="loading_time"){
			if($(this).val()%0.5!=0){
				$(".error_prompt").insertBefore($(this).closest("tr"));
				$(".error_prompt").show();
				$(".error_prompt td").html("请输入0.5的倍数！");
			}else{
				$(".error_prompt").hide();
			}
		}
	})
	//验证登陆
	$(".login input").keyup(function(){
		var login_name=$("#login_name").val();
        var password=$("#login_password").val();
		var reg=/^[a-zA-Z0-9]{6,12}$/;
        if($(this).parent().parent().index()==1){
            if(reg.test(login_name)==false){
				$(this).parent().parent().find(".tips span").html("用户名长度在6-12之间!");
            }else{
                $(this).parent().parent().find(".tips span").html("");
            }
        }
        if($(this).parent().parent().index()==2){
            if(reg.test(password)==false){
                $(this).parent().parent().find(".tips span").html("密码长度在6-12之间！")
            }else{
                $(this).parent().parent().find(".tips span").html("");
            }
        }
	});

	//jQuery mobile滑动侧边栏
	var page=$('div:jqmData(role="page")');
	page.on("swipeleft",function(){
		Leftscroll();
	});
	page.on("swiperight",function(){
		Rightscroll();
	});
	//点击菜单icon，侧边栏主动滑出
	var flag=1;
	$(".personal_menu").on("tap",function(){
        if(flag==1){
			Rightscroll();
			flag=0;
		}else{
			Leftscroll();
			flag=1;
        }
	});

	//多个跳转
	$(".log_room a").click(function(){
		location.href="../log_list";
	})
	//footer跳轉
	$("#footer a").click(function(){
		if($(this).index()==0){
			location.href="../message";
		}if($(this).index()==1){
			location.href="../log_list";
		}if($(this).index()==2){
			location.href="../map";
		}if($(this).index()==3){
			location.href="../orderList";
		}
		})
	$(".orderList").click(function(){
		location.href="../orderList";
	});

	$(".login .title a").click(function(){
		location.href="../register";
	});

});