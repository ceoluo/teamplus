Vue.filter('date',function(input){
var oDate=new Date(input);
return oDate.getFullYear()+'/'+oDate.getMonth()+'/'+oDate.getDay();
})
Vue.filter('lev',function(input){
	if(input==1){return "校级团队"}
		else if(input==2){return "院级团队"}
			else if(input==3){return "个人团队"}
})
window.onload=function(){
	var vm=new Vue({
		el:'body',
		data:{
			username:'请登录',
			joined_members:15,
			title:'鼎',
			introduction:'添“易”网页设计大赛，源于生活，易于生活。本次大赛的主题为网页版易班创造一个全新的模块（只要是之前易班上没有的或者大家觉得不够好的，都可以进行创新哦）。',
			imga:'../image/07.jpg',
			members:11,
			t_level:3,
			content:'添“易”网页设计大赛，源于生活，易于生活。本次大赛的主题为网页版易班创造一个全新的模块（只要是之前易班上没有的或者大家觉得不够好的，都可以进行创新哦）。添“易”网页设计大赛，源于生活，易于生活。添“易”网页设计大赛，源于生活，易于生活。本次大赛的主题为网页版易班创造一个全新的模块（只要是之前易班上没有的或者大家觉得不够好的，都可以进行创新哦）。添“易”网页设计大赛，源于生活，易于生活。本次大赛的主题为网页版易班创造一个全新的模块（只要是之前易班上没有的或者大家觉得不够好的，都可以进行创新哦）。添“易”网页设计大赛，源于生活，易于生活。本次大赛的主题为网页版易班创造一个全新的模块（只要是之前易班上没有的或者大家觉得不够好的，都可以进行创新哦）。添“易”网页设计大赛，源于生活，易于生活。本次大赛的主题为网页版易班创造一个全新的模块（只要是之前易班上没有的或者大家觉得不够好的，都可以进行创新哦）。添“易”网页设计大赛，源于生活，易于生活。本次大赛的主题为网页版易班创造一个全新的模块（只要是之前易班上没有的或者大家觉得不够好的，都可以进行创新哦）。',
			name:'科创部',
			isjoin:1,
			t_id:'',
			list:[]
		},
		methods:{
			getteam(){
				var s=localStorage.team_id;
				this.t_id=s;

				this.$http.get('http://192.168.1.111:5000/show_team_data?t_id='+s,
				{t_id:this.t_id}).then((res)=>{
					var st=res.data.data;
					this.title=st.t_name;
					this.joined_members=st.count_joined_members;
					this.members=st.t_members;
					this.introduction=st.t_introduction;
					this.content=st.t_content;
					this.isjoin=st.is_joined;

				}).catch(function(res){
					alert("请求失败！！！");
				});
			},
			getperson(){
				var s=localStorage.team_id;
				this.t_id=s;
				this.$http.get('http://192.168.1.111:5000/show_members?t_id='+s,{
					t_id:this.t_id}).then((res)=>{
					var st=res.data;
					for(var i=0;i<st.length;i++){
						this.list.push({
							u_neckname:st[i].u_id,
							imga:"../images/31.png"
							})
					}
				}).catch(function(res){
					alert("请求查看参加人员名单失败")
				})

			},
			join(){
				this.$http.get('http://192.168.1.111:5000/join_team',
				{t_id:this.t_id}).then((res)=>{
						var st=res.data;
						
							alert("报名成功");

							
					}).catch(function(res){
						alert("报名失败！！");
					});
				
			}
		},
		created(){
			this.getteam();
			this.getperson();
		}	
	})



}