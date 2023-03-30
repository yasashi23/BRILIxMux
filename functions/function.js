const fs = require('fs')
const {spawn} = require('child_process')



// hari jam
var date = new Date()
var hours = date.getHours()
var minutes = date.getMinutes()
var second = date.getSeconds()
var day = date.getDay()


async function program(dtk){

    const pythonExec = await spawn("python3",["/root/prog-kk/finish-py/wa-speak2.py"])


pythonExec.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});

 pythonExec.on('exit',(code,signal)=>{
	fs.writeFileSync('/root/nodenya/data-send.json', JSON.stringify(dtk))

const rdAntr2 = JSON.parse(fs.readFileSync('/root/nodenya/antrian/antrian2.json','utf-8'))
  fs.writeFileSync('/root/nodenya/antrian/antrian.json',JSON.stringify(rdAntr2))
  const newD = []
  fs.writeFileSync('/root/nodenya/antrian/antrian2.json',JSON.stringify(newD))

	 console.log("beres")
	
    })

}



module.exports = {program}
