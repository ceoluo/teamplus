       Vue.filter('date',function(input){
var oDate=new Date(input);
return oDate.getFullYear()+'/'+oDate.getMonth()+'/'+oDate.getDay();
})
Vue.filter('lev',function(input){
       if(input==1){
              return "校级"
       }else if(input==2){
              return "院级"
       }else if(input==3){
              return "自组"
       }
})

window.onload=function(){
	var vm=new Vue({
	el:'body',
	data:{
	      sign:"SIGN IN",
	      activity:[],
	      username:'',
	      userpass:'',
	      yanzhengma:'',
	      yanzhen:'http://192.168.1.111:5000/check_code',
	      username1:'',

             flag:2,
             current:1
		},
	methods:{
       content(i,type){
              if(type==1){
              localStorage.setItem('act_id',this.activity[i].a_id)
              window.open("../html/content3.html","_self")
              }else if(type==2){
              localStorage.setItem('team_id',this.activity[i].t_id)
              window.open("../html/content.html","_self")
              }

       },
       show(level,act,page){
              if(act==1){
              	this.flag=1;
       	      this.activity=[];
       	      this.$http.get('http://192.168.1.111:5000/show_activities',
       		     {a_level:level,
       		     current_page:page}
       		     ).then((res)=>{
       			    var st=res.data.data;
       			    for(var i=0;i<st.length;i++){
       				   this.activity.push({
       				   title:st[i].a_name,
					  startime:st[i].a_begin_time,
					  endtime:st[i].a_end_time,
					  name:'www',
					  imga:st[i].a_imgs,
					  a_id:st[i].a_id
       				   });
       					}
       				}).catch(function(res){
       					alert("请求数据失败！！！")
       				});
       			}else if(act=3){
                                   this.flag=2;
       				this.activity=[],
       				this.$http.get('http://192.168.1.111:5000/show_teams',
       					{t_level:level,current_page:page},{emulateJSON:true}

       			).then((res)=>{
       				var st=res.data.data;
       				for(var i=0;i<st.length;i++){
       					this.activity.push({
       					title:st[i].t_title,
       							/*startime:"
       							endtime:"",*/
                                                        level:st[i].t_level,
       							imga:"../images/05.jpg",
       							t_id:st[i].t_id,
       							name:st[i].t_name,
                                                        menbers:st[i].t_menbers

       					});
       				}
       					}).catch(function(res){
       					alert("请求数据失败！！")
       					});
       					
       			}
       		},
       		login(){
       	if(this.sign=="SIGN IN") {
       		$("#mark1").css('display', 'block');
       		$("#form1").css('display', 'block');
            this.$http.post('http://192.168.1.111:5000/login', {
                    u_xh_id: this.username,
                    u_password: this.userpass,
                    check_code: this.yanzhengma
                }, {emulateJSON: true}
            ).then((res) => {
                var json = res.data;
            this.username1 = 'json.u_xh_id'
            alert("登录成功");
            $("#mark1").css('display', 'none');
            $("#form1").css('display', 'none');

            if (this.username1 != "") {
                this.sign = "个人中心"
            }
        }).
            catch(function (res) {
                if (res.data.code == 400)
                    alert("密码错误")
            });
        }
       		},
       		usercenter(){
       			if(this.sign=="个人中心"){
       				window.open("../html/activity.html","_self")

       			}
       		},
                     check_login(){

                            this.$http.get('http://192.168.1.111:5000/check_login',{}).then((res)=>{
                                   var st=res.data;

                                   if(st.is_login==1){
                                          this.sign="个人中心";
                                   }else{
                                          this.sign="SIGN IN";
                                   }
                            }).catch(function(res){
                                   alert("连接失败")
                            });
                     },
                     change1(){
                           
                            if(this.current==1){
                                   alert("已经是首页了")
                            }
                            else{
                                  this.current=this.current-1; 
                            }

                     },
                     change2(){
                            this.current=this.current+1;

                     }

       },
       created(){
       	this.show(3,3,1);
              this.check_login();
       }
	});
	$('#yanzhen').attr("src",vm.yanzhen+"?t="+Math.random());
}