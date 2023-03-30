const fetch = require('node-fetch')

const title = "bikinin web dong"
const link = "httpan lah pokona"
const href = "httpan lah pkona"
const deskripsi ="jangann lah kau tinggal kan diirii iku , takkan mammpu hadaapii se eemuu ua a , hanya bersammamuu kuua akan bisaa a , kau adaa laah jannn tung kuu uuu, kau adaa lah HIDUPKU, lengkaapi jiwa ku, oh SAyangku kau begituuu u, sempu uurnaa, (sekali lagi), sempuuurrrnaaa "
const proposal ="1" 
const payment ="$200"
const spend = "$900000"
const country ="indonesia" 
const jobType ="hourly" 
//const skills = document.querySelectorAll('.up-skill-wrapper')
//const skillSpread = skills[0].querySelectorAll("a")

const posted ="1 menit lalu" 
//const ket = document.querySelectorAll('small.text-muted.display-inline-block')
//const KetMendalam = ket[0].querySelectorAll('small > span')

//const est = KetMendalam[1].querySelector('span:last-child')






//const arrSkill = ["HTML","CSS"]
//for(let i = 0; i < skillSpread.length;i++){              arrSkill.push(skillSpread[i].textContent)
//}
//const upEst = est.textContent
const newEst = "20 hari"

fetch('http://localhost:3001/data-ku2', {
    method:'POST',                                       headers:{
        'Content-Type': 'application/json'               },
    body: JSON.stringify({
        judul: title,
        propo: proposal,
        paymentnya: payment,
        negara: country,
        spendnya: spend,
        linknya: href,
        desk: deskripsi,
        Type: jobType,
        Skill: arrSkill,
        Post: posted,
        Estimasi: newEst

    })
})
.then(res => res.json())
.then(response => console.log(response.success))
.catch(err => console.log(err))
