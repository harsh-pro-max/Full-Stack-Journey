//1. Write a JavaScript function that returns array elements larger than a number.

let arr=[53,52,12,63,123,632,22,334];
function maxArray(arr){
    max=0;
    for(let i=0;i<arr.length;i++){
        if(arr[i]>max){
            max=arr[i];
        }
    }
    return max;
}
console.log(maxArray(arr));

// 2. Write a JavaScript function to extract unique characters from a string.
//str="abcdabcdefgggh" ans="abcdefgh"
function strUnique(str) {
    let ans = "";
    for (let i = 0; i < str.length; i++) {
        if (!ans.includes(str[i])) {
            ans += str[i];
        }
    }
    return ans;
}

console.log(strUnique("abcdabcdefgggh")); 

// 3. Write a JavaScript function that accepts a list of  country names as input and returns the longest country name as output.
let country=["Australia","Germany","United States of America"]
let len=country.length;
function longString(string,len){
    let lenStr=0;
    let res;
    for(let i=0;i<len;i++){
        
        if(string[i].length>lenStr){
            lenStr=string[i].length;
            res=i;
        }
    }
    return res;
}
console.log(country[longString(country,len)])

//4.Write a JavaScript function to count the number of vowels in a string arguement.
let string2="mynameisharshkushwaha";
function countVowel(str){
    let vol="aeiouAEIOU";
    let count=0;
    for(let i=0;i<str.length;i++){
        for(let j=0;j<vol.length;j++){
            if(str[i]==vol[j]){
                count++;
            }
        }
    }
    return count;
}
console.log(countVowel(string2));

//5. Write a JavaScript function to generate a random number within a range (start end).
function genRandom(start, end) {
    if (start > end) {
        console.error("Start should be less than or equal to end");
        return;
    }
    let rand = Math.floor(Math.random() * (end - start + 1)) + start;
    console.log(rand);
}
for (let i = 0; i < 100; i++) {
    console.log(genRandom(5, 10));
}
