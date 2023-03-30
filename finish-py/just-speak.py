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


for el in datAnt:


    desk = el["desk"]
    Est = el["Estimasi"]
    deskMod = desk.replace("\n", "")
    estMod = Est.replace("\n", "")
    skill=f"{el['Skill']}"
    link = el['linknya']


    repl2 = {"[": "", "]": "", "'": ""}

    for old, new in repl2.items():
        skill2 = skill.replace(old, new)




    title = ["*Judul* : ","*Proposal* : ","*Paymentnya* : ","*Spend* : ","*Post* : ","*Negara* : ","*Job-Type* : ","*Est* : ","*Deskripsi* : ",""]
    titleIsi = [el['judul'],el['propo'],el['paymentnya'],el['spendnya'],el['Post'],el['negara'],el['Type'],estMod,deskMod,""]


    tstn = f"Hello sir. there is a new post.  Job-Title:   {titleIsi[0]}. repeat once {titleIsi[0]}. Job-Skills:   {skill2}. repeat once {skill2}. Job-Type:   {titleIsi[6]}. repeat once {titleIsi[6]}. thank you sir."
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
    txtBatnow = f"your battery now is {batStat}, is {batStat}, is {batStat}, normal battery"
    if(batStat > 30):
        os.system(f"termux-tts-speak -r 0.7 {txtBatnow}")
    else:
        os.system(f"termux-tts-speak -r 0.7 {txtBatlow}")


    
    print("done")


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



