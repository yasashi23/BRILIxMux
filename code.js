const express = require('express')
const app = express()
const cors = require('cors')
const bodyParser = require('body-parser')
const fs = require('fs')
const {spawn} = require('child_process')
const {program} =require('/root/nodenya/functions/function')

app.use(cors())
app.use(bodyParser.json());

app.get('/',(req,res)=>{
    res.send('aman')
})




app.post('/data-ku',(req,res)=>{
    const datanya = JSON.stringify(req.body)
	const dataP = JSON.parse(datanya)
    res.send({success: 'kamu berhasil hore'})
})

var date = new Date()
var hours = date.getHours()
var minutes = date.getMinutes()
var second = date.getSeconds()
var day = date.getDay()
var hari = ["Minggu","Senin","Selasa","Rabu","Kamis","Jum'at","Sabtu"]


app.post('/data-ku2',(req,res)=>{
const datanya = JSON.stringify(req.body)
    res.send({success: 'kamu berhasil hore'})
    const aftDat = JSON.parse(datanya)
const skl = aftDat.Skill
    const iWant = ["HTML5","HTML","CSS","CSS 3","JavaScript","jQuery","Bootstrap","React"]
    const mySkl = skl.some(el=>iWant.includes(el))
    const nonSkl = ["WordPress","Divi","Elementor","WooCommerce","WordPress Development", "WordPress Plugin","Hugo","Bubble.io","Webflow"]

const type = aftDat.Type
const typeFix = type.includes("Fixed")
const estI = aftDat.Estimasi
const estIw = estI.replace("$","")
const estP = parseInt(estIw)


const resultSkill = skl.some(el => nonSkl.includes(el))   
const antr = JSON.parse(fs.readFileSync('/root/nodenya/antrian/antrian.json','utf-8'))
const antr2 = JSON.parse(fs.readFileSync('/root/nodenya/antrian/antrian2.json','utf-8'))
    if(aftDat.paymentnya === 'Payment verified'){
        if(aftDat.negara !== 'Israel'){
            if(aftDat.spendnya !== "$0"){
                if(!resultSkill && mySkl){
		   if(typeFix && estP > 35 || !typeFix ){
                    fs.writeFileSync('/root/nodenya/data.json', JSON.stringify(req.body))


              }}}}}else{console.log('tidak verified')}


//fs.writeFileSync('data.json', JSON.stringify(req.body))
const dataku = JSON.parse(fs.readFileSync('/root/nodenya/data.json', 'utf-8'))
const dataKirim = JSON.parse(fs.readFileSync('/root/nodenya/data-send.json', 'utf-8'))
const cek = antr.some(el => el.judul.includes(dataku.judul))
const cek2 = antr2.some(el => el.judul.includes(dataku.judul))


console.log(`${hours} : ${minutes} : ${second}`)
const stat = JSON.parse(fs.readFileSync('/root/nodenya/antrian/status.json','utf-8'))
if(dataku.judul === dataKirim.judul || antr.length !== 0){
    console.log('sama')
	if(stat.statusProg === "kosong" && antr.length !== 0) {
        program(dataku,antr2)
	
	}    
	

}else{
    console.log('beda')

if(stat.statusProg === "kosong"){
    if(!cek || antr.length === 0 ){
        antr.push(dataku)
        fs.writeFileSync('/root/nodenya/antrian/antrian.json',JSON.stringify(antr))
        program(dataku,antr2)
    }else{
        console.log("datanya udah ada diantrian")
    }
}else{
console.log("berjalan")
    if(!cek && antr2.length === 0 || antr2.length !== 0 && !cek && !cek2){
        antr2.push(dataku)
        fs.writeFileSync('/root/nodenya/antrian/antrian2.json',JSON.stringify(antr2))

    }
}




console.log(antr.length)	

}

})

app.listen(3001, ()=>{
	console.log("berjalan")
    })

