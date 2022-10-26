let numRows = 10;
let outerArr = [];
let innerArray = [];
for (let i = 1; i <= numRows; i++){
    if (i == 1){
        innerArray = [1]
    }else if (i == 2 ){
        innerArray = [1, 1]
    }else{
        let start = 0
        for(let w=1; w <=i; w++){
            if (w == 1){
                innerArray.push(w);
            }else if (w == i){
                innerArray.push(1) 
            }else{
                let arr = outerArr[i - 2];
                num = 0
                for(let s= start; s < w; s++){
                    start ++
                    num += arr[s]
                }
                start -= 1
                innerArray.push(num)

            }
        }
    }
    outerArr.push(innerArray)
    innerArray = []
} 
console.log(outerArr)