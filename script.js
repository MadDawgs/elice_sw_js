// ���û��׿� ���� �ڵ带 �ۼ��մϴ�.
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
let arr = [];
rl.on("line", function (line) {

  rl.close(); 
}).on("close", function () {
  
});(

    function getDigits(n){
        let ans = [];
        var str =""
        str = n.toString(10);
        for (var i = 0; i<str.length; i++){
            ans.push(parseInt(str.charAt(i)));
        }
        return(ans);
    }
    