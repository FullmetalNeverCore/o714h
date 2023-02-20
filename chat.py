import requests 
from colorama import Fore, Back, Style



class Chat714h:
    def __init__(self,char,rnd,lenn,fpen,ppen,ip):
        self.char = char 
        self.rnd = rnd 
        self.lenn = lenn 
        self.fpen = fpen 
        self.ppen = ppen 
        self.ip = ip 

    def get_stats(self):
        for x in [self.char,self.rnd,self.lenn,self.fpen,self.ppen,self.ip]:print(x) 
    

    def upload_nn_vals(self):
        headers = {'Content-type': 'application/json'}
        for x,y in zip(['rnd','lenn','fpen','ppen'],[self.rnd,self.lenn,self.fpen,self.ppen]):
            r = requests.post(f'http://{self.ip}:5000/nn_vals',json={
                'type' : x, 
                'val': y
            },headers=headers)
            assert r.status_code == 200,print(f'Err in post {x,y}')

    def changeChar(self):
        headers = {'Content-type': 'application/json'}
        requests.post(f'http://{self.ip}:5000/verify_credentials',json={
            'username':'',
            'password':'',
            'char':str(self.char)
            },
            headers=headers).content

    def chat(self,data,type='gpt3'):
        if requests.post(f'http://{self.ip}:5000/chat_exchange',json={'chat':data,'type':type}).status_code == 200:
            rq = requests.get(f"http://{self.ip}:5000/msg_buffer").json()["text"]
            msg_bfr = ''
            for x in range(2,len(rq)):
                msg_bfr += rq[x]
            print(f'{Fore.MAGENTA + msg_bfr}')
    
    def translate_msg(self):
        rq = requests.get(f"http://{self.ip}:5000/msg_buffer").json()["text"]
        msg_bfr = ''
        for x in range(2,len(rq)):
            msg_bfr += rq[x]
        print(msg_bfr)

        



if "__main__" == __name__:
    chat = Chat714h(input('Choose char: '),float(input('Choose rnd: ')),int(input('Choose lenn: ')),float(input('Choose fpen: ')),float(input('Choose ppen: ')),"192.168.8.147")
    chat.upload_nn_vals()
    print(Fore.RED +'714h. ')
    chat.changeChar()
    #chat.get_stats()
    while True:
        chat.chat(input(Fore.CYAN +'N: '))  
    