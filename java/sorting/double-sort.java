function doubleSort(arr) 
{
    
    var numbers=[], strings=[];
    arr.forEach(function(x) {
      if (isNumber(x)) {
        numbers.push(Number(x));
      } else {
        strings.push(x);
      }
    });
    
    strings.sort();
    numbers.sort(function(a, b) { return a - b; });
    
    var sorted=[], nextNumber=0, nextString=0;
    arr.forEach(function(x) {
      if (isNumber(x)) {
        sorted.push(String(numbers[nextNumber++]));
      } else {
        sorted.push(strings[nextString++]);
      }
    });
    return sorted;
  }
  
  
  function isNumber(x) {
    return Number(x).toString() === x;