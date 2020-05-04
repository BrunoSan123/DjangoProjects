import matplotlib.pyplot as plt
import numpy as np
import datetime
import requests
import json

url ="https://api.covid19api.com/dayone/country/brazil"
payload={}
headers={}
resp=requests.request("GET",url,headers=headers,data=payload)
dt = json.loads(resp.text)


#requisiçõs da api 

data=[]
dt_confi=[]

for s in range(int(len(dt)/2),len(dt)):
    data.append(str(dt[s]["Date"])[5:10]+"|")
    dt_confi.append(dt[s]["Confirmed"])
x =np.arange(len(data))

#loop para listar e dividir dados

width =0.20
fig,ax =plt.subplots()
rects1 =ax.bar(x-width,dt_confi,width,label="COVID PELO BRASIL")
ax.set_title("Coronavirus Brasil")
ax.set_ylabel("Números de casos confirmados")
ax.set_xlabel("Mês e Dia")
ax.set_xticks(x)
ax.set_xticklabels(data)
ax.legend()
def autolabel(rects):
    for rect in rects:
        height =rect.get_height()
        ax.annotate('{}'.format(height),
        xy=(rect.get_x()+rect.get_width(),height),
        xytext=(0,3), # deslocamento vertical de 3 pontos
        textcoords="offset points",
        ha='center',va='bottom')
autolabel(rects1)
fig.tight_layout()
plt.show()
        
        
