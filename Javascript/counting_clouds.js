function jumpingOnClouds(c) {
    let i = 0;
    let count = 0;
    while (i < c.length) {
        if (c[i] === 0) {
            if(c[i+2]===0){
                i=i+2;
                count++;
            }else{
                i=i+1;
                count++;
            }
        }
    }
return count-1;
}
