function countingValleys(n, s) {
    s=s.split("");
    let count=0;
    let valley=0;
s.forEach(i=>{
    if(i==="U"){
        count=count+1;
        if(count===0){
            valley++;
        }
    }
    else if(i==="D"){
        count=count-1;
    }
})
return valley;
}