#Python program to scrape website 
#and save quotes from website
import json
import requests 
from bs4 import BeautifulSoup 
import csv 

URL = "https://indiarailinfo.com/station/map/katni-junction-kte/"
URL1="https://www.w3schools.com/jsref/jsref_length_array.asp"
team={}
f= open("mydata.json")
team = json.load(f)
print(len(team))
for i in range(1,12860):
    r = requests.get(URL+str(i))
    soup = BeautifulSoup(r.content, 'html5lib')
    if(soup.find('div', class_= 'topcapsule')):
        containers =soup.find('div', class_= 'topcapsule')
        s=containers.h1.text
        ini = s.find("/")
        s1=s[0:ini]
        team[s1]=[]
    #movie_containers=movie_containers.div.find("div", {"class": "row","id": "all_quotes"})
    #movie_containers = movie_containers.find_all('div', class_ = 'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top')
    #Nearby_stations=containers.find('div',{"style": "line-height:2;border-radius:5px;padding:3px;margin:3px;color:#800066;background-color:#EED7F4;text-align:center;"})
    
        if(containers.find('div',{"style": "line-height:2;border-radius:5px;padding:3px;margin:3px;color:#800066;background-color:#EED7F4;text-align:center;"})):
            Nearby_stations=containers.find('div',{"style": "line-height:2;border-radius:5px;padding:3px;margin:3px;color:#800066;background-color:#EED7F4;text-align:center;"})
            Nearby_stations=Nearby_stations.find_all('a')
            print('hjax',i)
            for j in Nearby_stations:
                ss=j.text
                inii=ss.find("/")
                team[s1].append(ss[0:inii])
                print("stations "+ss[0:inii])
            print(len(Nearby_stations))
print(len(team))
with open('mydata_new.json', 'w') as f:
    json.dump(team, f)


'''import json
import requests 
from bs4 import BeautifulSoup 
import csv
if(i==1):
    URL1=URL+str(i)
    r = requests.get(URL1)
    soup = BeautifulSoup(r.content, 'html5lib')
    containers =soup.div.find('div',class_='topcapsule')
    #containers=containers
    print(soup)
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html5lib')
print(soup.div)
team = {}
team['cars']=[]
team['cars'].append("uop")
#team=json.dumps(team)
with open('mydata.json', 'w') as f:
    json.dump(team, f)'''
