function balancedParensRecursive(remaining, counter, string, array) {
  if (remaining === 0 && counter === 0) {
    array.push(string);
  } else if (counter > 0 && remaining === 0) {
    balancedParensRecursive(remaining, counter - 1, string + ')', array);
  } else if (counter === 0 && remaining > 0) {
    balancedParensRecursive(remaining - 1, counter + 1, string + '(', array);
  } else {
    balancedParensRecursive(remaining, counter - 1, string + ')', array);
    balancedParensRecursive(remaining - 1, counter + 1, string + '(', array);
  }
}

function balancedParens(n) {
  let array = [];
  let counter = 0;
  balancedParensRecursive(n, counter, '', array);
  return array;
}

function balancedParensExample1(n) {
  let all = [];
  let parens = function(left, right, str) {
    // if no more brackets can be added then add the final balanced string
    if (left === 0 && right === 0) {
      all.push(str);
    }
    // if we have a left bracket left we add it
    if (left > 0) {
      parens(left - 1, right + 1, str + "(");
    }
    // if we have a right bracket left we add it
    if (right > 0) {
      parens(left, right - 1, str + ")");
    }
  };
  parens(n, 0, "");
  return all;
}

function balancedParensExample2(n) {
  function solve(n,start,end,s){
    if (!end) li.push(s)
    if (end>start) solve(n,start,end-1,s+')')
    if (start) solve(n,start-1,end,s+'(')
  }
  var li = []
  solve(n,n,n,'')
  return li
}

function assertDeepEquals(arr1, arr2) {
  const jarr1 = JSON.stringify(arr1);
  const jarr2 = JSON.stringify(arr2);
  console.log(`Expected ${jarr2}, got ${jarr1}`);
}

assertDeepEquals( balancedParens(0).sort(), [""] );
assertDeepEquals( balancedParens(1).sort(), ["()"] );
assertDeepEquals( balancedParens(2).sort(), ["(())","()()"] );
assertDeepEquals( balancedParens(3).sort(), ["((()))","(()())","(())()","()(())","()()()"] );
assertDeepEquals( balancedParens(4).sort(), ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"] );

