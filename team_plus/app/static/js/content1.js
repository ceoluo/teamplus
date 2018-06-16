Vue.filter('date',function(input){
var oDate=new Date(input);
return oDate.getFullYear()+'/'+oDate.getMonth()+'/'+oDate.getDay();
})
window.onload=function(){
	var vm=new Vue({
		el:'body',
		data:{
			username:'请登录',
			begin_time:'2018/05/06',
			end_time:'2018/5/24',
			title:'网页设计大赛',
			introduction:'添“易”网页设计大赛，源于生活，易于生活。本次大赛的主题为网页版易班创造一个全新的模块（只要是之前易班上没有的或者大家觉得不够好的，都可以进行创新哦）。',
			imga:'',
			content:'添“易”网页设计大赛，源于生活，易于生活。本次大赛的主题为网页版易班创造一个全新的模块（只要是之前易班上没有的或者大家觉得不够好的，都可以进行创新哦）。添“易”网页设计大赛，源于生活，易于生活。添“易”网页设计大赛，源于生活，易于生活。本次大赛的主题为网页版易班创造一个全新的模块（只要是之前易班上没有的或者大家觉得不够好的，都可以进行创新哦）。添“易”网页设计大赛，源于生活，易于生活。本次大赛的主题为网页版易班创造一个全新的模块（只要是之前易班上没有的或者大家觉得不够好的，都可以进行创新哦）。添“易”网页设计大赛，源于生活，易于生活。本次大赛的主题为网页版易班创造一个全新的模块（只要是之前易班上没有的或者大家觉得不够好的，都可以进行创新哦）。添“易”网页设计大赛，源于生活，易于生活。本次大赛的主题为网页版易班创造一个全新的模块（只要是之前易班上没有的或者大家觉得不够好的，都可以进行创新哦）。添“易”网页设计大赛，源于生活，易于生活。本次大赛的主题为网页版易班创造一个全新的模块（只要是之前易班上没有的或者大家觉得不够好的，都可以进行创新哦）。',
			name:'科创部',
			isjoin:1,
			a_id:'',
			list:[]
		},
		methods:{
			getact(){
				var s=localStorage.act_id;
				this.a_id=s;

				this.$http.get('http://192.168.1.111:5000/get_activity_data',{
					a_id:this.a_id
				}
				).then((res)=>{
					var st=res.data.data;
					this.title=st.a_name;
					this.begin_time=st.a_begin_time;
					this.end_time=st.a_end_time;
					this.introduction=st.a_introduction;
					this.content=st.a_content;
					this.isjoin=st.is_joined;
					this.imga=st.a_imgs;
				}).catch(function(res){

				});
			},
			getperson(){
				var s=localStorage.act_id;
				this.a_id=s;
				this.$http.get('http://192.168.1.111:5000/show_user_list',{
					a_id:this.a_id
				}).then((res)=>{
					var st=res.data;
					for(var i=0;i<st.length;i++){
						this.list.push({
							u_neckname:st[i].u_nickname,
							imga:"../images/35.jpg"
							})
					}

				}).catch(function(res){

				});

			},
			join(){
				
				this.$http.get('http://192.168.1.111:5000/join_activity',
				{a_id:this.a_id}
					).then((res)=>{
						var st=res.data;
						if(st.success==1){
							alert("报名成功");

						}
					}).catch(function(res){

					});
				
			}
		},
		created(){
			this.getact();
			this.getperson();
		}	
	})



}