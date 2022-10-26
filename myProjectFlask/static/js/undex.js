let word1 = ['ab', 'c', 'egg'];
let word2 = ['a', 'bc'];

// have a problem to solve
// define your problem
// breakdown your problem into goals
// solve your goal one after the other

// make a string from the arrays 
// check if the word1str is equals to word2str

let wordsArr = [word1, word2]
let str1 = '';
let str2 = '';
let strArr = [str1, str2]
console.log(wordsArr)
for(let index in wordsArr){
    let word = wordsArr[index]
    console.log('item in wordArr:  ',word)
    for(let item of word){
        console.log('item in wordArr items: ', item);
        strArr[index] += item
    }
    console.log('strArr: ', strArr)
}

let answer = true;
let check = strArr[0];
for(let i of strArr){
    if (i != check){
        answer = false;
        break;
    }
}
console.log(answer)
console.log(strArr.every((value)=>(value == strArr[0])));

'(())[]{}'
'('

'(][)'