function add(str1, str2) {
  const maxlen = (str1.length > str2.length) ? str1.length : str2.length;
  let result = '';
  let carryover = 0;
  for (i = 0; i < maxlen; i++) {
    let char1 = '';
    let char2 = '';
    if (i === 0) {
      char1 = str1.slice(-1);
      char2 = str2.slice(-1);
    } else {
      char1 = str1.slice(-(i+1), -i);
      char2 = str2.slice(-(i+1), -i);
    }
    let added = Number(char1) + Number(char2) + carryover;
    carryover = Math.floor(added / 10);
    result += added % 10;
  }
  if (carryover) {
    result += carryover;
  }
  return result.split('').reverse().join('');
}

function addExample1(a, b) {
  var res = '', c = 0
  a = a.split('')
  b = b.split('')
  while (a.length || b.length || c) {
    c += ~~a.pop() + ~~b.pop()
    res = c % 10 + res
    c = c > 9
  }
  return res
}

function addExample2(a, b) {
  var carry = 0, result = [],
      len = Math.max(a.length, b.length), i = len;
  while (i--) {
    var sum = (+a[i - len + a.length]||0) + (+b[i - len + b.length]||0) + carry;
    carry = parseInt(sum / 10);
    result.unshift(sum % 10);
  }
  if (carry) result.unshift(carry);
  return result.join('');
}

function assertEquals(str1, str2) {
  console.log(typeof str1 === 'string' && str1 === str2);
  console.log(`Expected ${str2}, got ${str1}`);
}

assertEquals(add("1", "1"), "2");
assertEquals(add("123", "456"), "579");
assertEquals(add("888", "222"), "1110");
assertEquals(add("1372", "69"), "1441");
assertEquals(add("12", "456"), "468");
assertEquals(add("101", "100"), "201");
assertEquals(add(
  '63829983432984289347293874',
  '90938498237058927340892374089'),
  "91002328220491911630239667963");