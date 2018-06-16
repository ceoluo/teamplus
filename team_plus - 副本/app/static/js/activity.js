Vue.filter('date',function(input){
    var d=new Date(input);
    var year = d.getFullYear(); 
    var month = d.getMonth() + 1;
    var day = d.getDate() <10 ? '0' + d.getDate() : '' + d.getDate();
	return year+"/"+month+"/"+day;
})
Vue.filter('age',function(input){
	var birth=new Date(input);
	return 2018-birth.getFullYear();
})
window.onload=function(){
	var vm=new Vue({
		el:'body',
	data:{
		username:'万事通',
		flag:1,
		a_title:'',
		a_name:'个人',
		a_startday:'',	
		a_endday:'',
		a_content:'',
		level:'校级',
		a_intrduction:'',
		a_level:0,
		adm_time:'',
		username:'万事通',
		u_id:'3120160905106',
		u_neckname:'waston',
		u_sex:'男',
		u_age:18,
		u_add:'四川成都', 
		u_mingzu:'汉族',
		u_school:'计算机与软件工程学院',
		u_introduction:'',
		u_major:'软件工程',
		t_name:'team+',
		t_level:'校级',
		t_level1:'',			
		t_introduction:'123',
		t_file:'',
		t_members:12,
		t_title:'',
		u_team_id:'',
		t_limt_members:122,
		a_img:'',
		a_img_base64: '',
		arr:[{
			name:'个人',
			id:1
		}],
		myact:[],
		myteam:[],
		head:"",
		headimga:'../images/31.png'
	},	
	methods:{
		/*loadImg(e) {
            var file = this.a_img = e.target.files[0];
            var reader = new FileReader();
            var _this = this;
            reader.readAsDataURL(file);
            reader.onload = function () {
               console.log(this.result);
               _this.a_img_base64 = this.result

            }
        },*/
		headimg(i){
			if(i==1) {
                $("#head").css('display', 'block');
            }else {
				$("#head").css('display', 'none');
			}
		},
			save(){
			this.$http.post('http://192.168.1.105/alter_my_data',{
				u_nickname:this.u_nickname,
				u_add:this.u_add1,
				u_title:"wrq",
				u_introduction:this.u_introduction1,
			},{emulateJSON: true}).then((res)=>{
				this.getinformation()
			}).catch(function(){
				alert("修改失败")
			});

		},



	
	submit(){



	},
	getinformation(){
		this.$http.get('http://192.168.1.105/my_data',).then((res)=>{
		var json=res.data.data;
		this.username=json.u_name;
		this.u_neckname=json.u_nickname;
		this.u_id=json.u_xh_id;
		this.u_sex=json.u_sex;
		this.u_age=json.u_birth;
		this.u_mingzu=json.u_race;
		this.u_school=json.u_faculty;
		this.u_major=json.u_discipline;
		this.adm_time=json.u_adm_time;
		this.u_introduction=json.u_introduction;
		this.headimga=json.head_img;
		}).catch(function(res){
			/*alert("请求失败：错误代码"+res.data.code)*/
		});
	},
	creactivity(){

		if(this.level=="校级"){
			this.a_level=1;
		}else if(this.level=="团队"){
			this.a_level=2;
		}else if(this.level=="个人"){
			this.a_level=3;
		}
		//alert(this.a_level+"    "+this.a_title+"   "+this.a_startday+"        "+this.a_endday+"   "+this.a_content+"    "+this.a_intrduction)
		if(this.a_name=="个人"){
			this.u_team_id=1;
		}else{
			for(var j=0;j<this.arr.length;j++){
				if(this.a_name==this.arr[j].name){
					this.u_team_id=this.arr[j].id;
				}
			}
		}
	/*	var formData = new FormData()

		formData.append("file",this.a_img)
		alert(this.a_img)*/
		/*this.$http.post('http://192.168.1.111:5000/upload_activity_file',{
			file: this.a_img_base64
		}).then((res)=>{
			alert("提交图片成功！！！")

		}).catch (function(res){
			alert("提交图片失败")
		});*/
		//jQuery上传图片
		// console.log($("#imgfile"))


		this.$http.post('http://192.168.1.105/create_activity',{
			a_name:this.a_title,
			a_introduction:this.a_introduction,
			a_begin_time:this.a_startday,
			a_end_time:this.a_endday,
			a_level:this.a_level,
			a_content:this.a_content,
			a_imgs:"12312312",
			a_creator:this.u_team_id,
			},{emulateJSON:true}
			).then((res)=>{

		}).catch(function(res){

		});
		
	},
	seemyact(i){
		if(i==2){
			this.flag=3;
			this.myact=[];
			this.$http.get('http://192.168.1.105/show_joined_activities',).then((res)=>{
				var st=res.data.data;
				for(var i=0;i<st.length;i++){
					
					this.myact.push({
						title:st[i].a_name,
						content:st[i].a_introduction,
						begintime:st[i].a_begin_time,
						endtime:st[i].a_end_time,
						imga:st[i].a_imgs
					});
				}
			}).catch(function(res){
					})

				}else if(i==1){
					this.flag=2;
					this.myact=[];
					this.$http.get('http://192.168.1.105/my_activity',).then((res)=>{
						var st=res.data;
						for(var i=0;i<st.length;i++){
							this.myact.push({
							title:st[i].a_name,
							content:st[i].a_introduction,
							begintime:st[i].a_begin_time,
							endtime:st[i].a_end_time,
							imga:st[i].a_imgs

							})}
						}).catch(function(res){
							});
						
					
				}
	
		},
		seemyteam(i){
			
			if(i==1){
				this.flag=6;
				this.myteam=[];
				this.$http.get('http://192.168.1.105/my_teams',).then((res)=>{
					var st=res.data;
					for(var i=0;i<st.length;i++){
						this.myteam.push({
							content:st[i].t_introduction,
							title:st[i].t_name,
							imga:'../images/33.jpg'
						});
					}
				}).catch(function(res){
				});
			}else if(i==2){
				this.flag=7;
				this.myteam=[];
				this.$http.get('http://192.168.1.105/show_joined_teams',).then((res)=>{
					var st=res.data.data;
					for(var i=0;i<st.length;i++){
						this.myteam.push({
							content:st[i].t_introduction,
							title:st[i].t_name,
							imga:'../images/33.jpg'
						});
					}
				}).catch(function(res){
					alert("失败！！！")
				});

			}

		},
		getteam(){
			this.$http.get('http://192.168.1.105/my_teams',{}).then((res)=>{
				var st=res.data;
				for(var i=0;i<st.length;i++){
					this.arr.push({
						name:st[i].t_name,
						id:st[i].t_id
					});
					
				}
			}).catch(function(res){
				alert("失败！！！")
			})
		},
		createam(){
			if(this.t_level=="校级"){
				this.t_level1=1;
			}else if(this.t_level=="院级"){
				this.t_level1=2;
			}else if(this.t_level=="自组团队"){
				this.t_level1=3;
			}

			this.$http.post('http://192.168.1.105/create_team',{
				t_name:this.t_title,
				t_introduction:this.t_introduction,
				t_members:this.t_limt_members,
				t_level:this.t_level1,
			},{emulateJSON:true}
			).then((res)=>{
				alert("创建活动成功！！")
			this.seemyteam(2)
			}).catch(function(res){

			});

		},
		test(){
			alert(this.u_team_id)
		}

	},
	

created(){
	this.getinformation();
	this.getteam();
}
})
}