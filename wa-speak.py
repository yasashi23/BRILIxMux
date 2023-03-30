from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import json
import time
import os
import subprocess

#statusnya
def status():
    with open('/root/nodenya/antrian/status.json', 'r') as file:
        cont = file.read()
        dat = json.loads(cont)
        return dat

rSt = status()
rSt["statusProg"] = "berjalan"


with open('/root/nodenya/antrian/status.json', 'w') as wfile:
    json.dump(rSt,wfile)

rst = status()
print(rst["statusProg"])    

#datanya
def readA():
    with open('/root/nodenya/antrian/antrian.json', 'r') as file:
        cont = file.read()
        dat = json.loads(cont)
        return dat

datAnt = readA()

dr_ser = Service(executable_path='/usr/local/bin/geckodriver',port=5001,service_args=['--marionette-port','2828','--connect-existing'])
driver = webdriver.Firefox(service=dr_ser)
for el in datAnt:
#    print(f"JUDUL : {el['judul']}   ESTIMASI : {el['Estimasi']}")

    desk = el["desk"]
    Est = el["Estimasi"]
    deskMod = desk.replace("\n", "")
    estMod = Est.replace("\n", "")
    skill=f"{el['Skill']}"
    link = el['linknya']

    repl = {"[": "", "]": "", "'": "*",",":" ```-``` "}

    for old, new in repl.items():
        skill1 = skill.replace(old, new)

    repl2 = {"[": "", "]": "", "'": ""}

    for old, new in repl2.items():
        skill2 = skill.replace(old, new)




    title = ["*Judul* : ","*Proposal* : ","*Paymentnya* : ","*Spend* : ","*Post* : ","*Negara* : ","*Job-Type* : ","*Est* : ","*Deskripsi* : ",""]
    titleIsi = [el['judul'],el['propo'],el['paymentnya'],el['spendnya'],el['Post'],el['negara'],el['Type'],estMod,deskMod,""]


    tstn = f"Hello sir. there is a new post.  Job-Title:   {titleIsi[0]}. Job-Skills:   {skill2}. Job-Type:   {titleIsi[6]}. thank you sir."
    os.system(f"termux-tts-speak -r 0.7 {tstn}")

    def battery():
	    output = subprocess.check_output("termux-battery-status", shell=True)
    	percentage = output.decode("utf-8").split('"')[6]
	    newPer = {":":"",",":""," ":""}
    	for old,new in newPer.items():
    		percentage = percentage.replace(old,new)
	    bat = int(percentage)
    	return bat

    batStat = battery()
    txtBatlow = f"your battery now is {batStat}, is {batStat}, is {batStat}, please charge sir!!"
    txtBatnow = f"your battery now is {batStat}, is {batStat}, is {batStat}, noraml battery"
    if(batStat > 30) {
    os.system(f"termux-tts-speak -r 0.7 {txtBatnow}")
            }
    else{
    os.system(f"termux-tts-speak -r 0.7 {txtBatLow}")

            }




    #driver.get('https://web.whatsapp.com')
    #driver.refresh()
    cont = driver.find_element(By.CSS_SELECTOR,'span[title="+62 852-1245-4896"]')
    cont.click()

    chat = driver.find_element(By.CSS_SELECTOR,'._3Uu1_')

    ActionChains(driver).move_to_element(chat).click()\
        .send_keys("========= PEMBUKA ========")\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .send_keys(f"{title[0]} {titleIsi[0]}")\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .send_keys(f"{title[1]} {titleIsi[1]}")\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .send_keys(f"{title[2]} {titleIsi[2]}")\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .send_keys(f"*Skills* :")\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .send_keys(f"{skill1}")\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .send_keys(f"{title[3]} {titleIsi[3]}")\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .send_keys(f"{title[4]} {titleIsi[4]}")\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .send_keys(f"{title[5]} {titleIsi[5]}")\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .send_keys(f"{title[6]} {titleIsi[6]}")\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .send_keys(f"{title[7]} {titleIsi[7]}")\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .send_keys(f"{title[8]} {titleIsi[8]}")\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .send_keys(f"*Link* : {link}")\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)\
        .send_keys("======== PENUTUP ========")\
        .send_keys(Keys.ENTER).perform()
    print("done")

driver.quit()

datN = readA()
newDat = datN[0:0]

with open('/root/nodenya/antrian/antrian.json', 'w') as wfile:
    json.dump(newDat,wfile)

time.sleep(5)

print(len(readA()))
rStN = status()
rStN["statusProg"] = "kosong"


with open('/root/nodenya/antrian/status.json', 'w') as wfile:
    json.dump(rStN,wfile)
rstN = status()
print(rstN["statusProg"])    



