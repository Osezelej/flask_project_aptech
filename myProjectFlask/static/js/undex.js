// '()[]{}'
// let brackets = '{';
// let start = 0;
// let answer = true
// if (brackets){
//     for(let i = 0; i < brackets.length; i+= 2){
//         console.log(brackets[i])
//         if (brackets[i] == '('){
//             if(brackets[i + 1] == ')'){
//                 continue;
//             }else{
//                 answer = false
//                 break;}
//         }else if (brackets[i] == '['){
//             if(brackets[i + 1] == ']'){
//                 continue;
//             }else{
//                 answer = false
//                 break;
//             }
//         }else if (brackets[i] == '{'){
//             if(brackets[i + 1] == '}'){
//                 continue;
//             }else{
//                 answer = false;
//                 break;
//             }
//         }else{
//             answer = false
//             break;
//         }
//     }
// }else{
//     answer = false;
// }
// console.log(answer)

// functional programming 

function callName(name){
    let n = name.toUpperCase()
   return n
}

var message = callName('vincent')
console.log(message)


// add, sub, mul, div
function add(n1, n2){
    let answer = n1 + n2;
    return answer
}

function sub(n1, n2){
    let answer = n1 - n2;
    return answer
}


console.log(message)