window.onload=function(){
	var url="http:/127.0.0.1:5000/login";
	var vm=new Vue({
		el:'body',
		data:{
			username:'',
			userpass:'',
			yanzhengma:'',
			flag:1,
			a:1,
			yanzhen:'http://127.0.0.1:5000/check_code',
			huodong:[		
			{
				title:'biaotiyi',
				neirong:'57rtgvtghghghsghardugjhaerjgbaejkrgbjaerkgbvjkasekgnaerklgnkaelwngvklaergeuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuieruioagvioahgvioiuerangvjiaerngvjaerngjkvnaerjkgvnaerjkgnvjkaerngioaerhgioerhnguieraghuaerngkjaengklaerngivaerhnbjhaengjivaerkgbajkbn',
				imga:'../images/01.jpg'

			},
			{
				title:'biaotier',
				neirong:'57rtgvtghghghsghardugjhaerjgbaejkrgbjaerkgbvjkasekgnaerklgnkaelwngvklaerg',
				imga:'../images/01.jpg'

			},
			{
				title:'biaot3',
				neirong:'57rtgvtghghghsghardugjhaerjgbaejkrgbjaerkgbvjkasekgnaerklgnkaelwngvklaerg',
				imga:'../images/01.jpg'

			}

			/*neirong:{['fcawerfvear','agevaergvae','eragvaer','ergvaerg']}
			time:['2018/01/02','2018/01/04','2018/01/03','2018/01/05']*/
			],
			jointable:[
			{
				title:'标题一',
				neirong:'rebjadfvbajkadbvjkaaaaaaaebjvjhbadjkvbjhadjkvbajkbadjbvaruioefgbejkasfguwehnfgjwebngagvjadvbhaerbvjke',
				time:'2017/04/06'
			},
			{
				title:'标题二',
				neirong:'rebjadfvbajkadbvjkaaaaaaaebjvjhbadjkvbjhadjkvbajkbadjbvaruioefgbejkasfguwehnfgjwebngagvjadvbhaerbvjke',
				time:'2017/04/07'
			},
			{
				title:'标题三',
				neirong:'rebjadfvbajkadbvjkaaaaaaaebjvjhbadjkvbjhadjkvbajkbadjbvaruioefgbejkasfguwehnfgjwebngagvjadvbhaerbvjke',
				time:'2017/04/08'
			}
						],
			stutable:[
			{
				neckname:'昵称一',
				stuid:'3120160905106',
			},
			{
				neckname:'昵称二',
				stuid:'3120160905106',
			},
			{
				neckname:'昵称三',
				stuid:'3120160905106',
			},
			{
				neckname:'昵称三',
				stuid:'3120160905106',
			},
			{
				neckname:'昵称三',
				stuid:'3120160905106',
			},
			{
				neckname:'昵称三',
				stuid:'3120160905106',
			}],

			liuyan:[
			{
				neirong:'sdgvgvgvgvgvgvgvhgasdgdsdsf',
				time:2018/04/25,
				person:'XXX'

			},
			{
				neirong:'sdgvgvgvgvgvgvgvhgasdgdsdsf',
				time:2018/04/25,
				person:'XXX'

			}
			],
			flag2:1,
			schoolactivity:[{
				imga:'../images/05.jpg',
				title:'title',
				content:'guidragvbaejbvjgjaerbgjaergbiaer'
			}],
			classactivity:[{
				imga:'../images/04.jpg',
				title:'title',
				content:'guidragvbaejbvjgjaerbgjaergbiaer'


			},
			{
				imga:'../images/04.jpg',
				title:'title',
				content:'guidragvbaejbvjgjaerbgjaergbiaer'


			}
			],
			conpetition:[{
				imga:'../images/02.jpg',
				title:'标题',
				content:'asdrfjawebfawebjfgbaebfi'

			}]
		,
		
			a1:'../images/01.jpg',
			a2:'../images/02.jpg',
			a4:'../images/03.jpg',
			a3:'../images/04.jpg'
		
		},
		methods:{
			userlogin(){

				this.$http.post('http://127.0.0.1:5000/login',{
						u_id:this.username,
						password:this.userpass,
						check_code:this.yanzhengma
					},{emulateJSON:true}
				).then(function(res){
					alert(res.body)

				},function(res){
					alert(res.body)
				});
			}
		}
	})
	$('#yanzhen').attr("src",vm.yanzhen+"?t="+Math.random());

}