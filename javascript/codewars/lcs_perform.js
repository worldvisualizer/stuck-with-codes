const Test = require('./test');

// don't forget about padding
function initializeMatrix(len1, len2) {
  return new Array(len1).fill(0).map(() => new Array(len2).fill(0));
}

function lcs(str1, str2) {
  const len1 = str1.length;
  const len2 = str2.length;
  const mat = initializeMatrix(len1 + 1, len2 + 1);
  // memoization roll
  for (let i = 1; i < len1 + 1; i++) {
    for (let j = 1; j < len2 + 1; j++) {
      if (str1[i] === str2[j]) {
        mat[i][j] = 1 + Math.max(mat[i-1][j], mat[i][j-1]);
      } else {
        mat[i][j] = Math.max(mat[i-1][j], mat[i][j-1]);
      }
    }
  }
  return backtrack(mat, str1, len1, len2);
}

// proof of concept simple max length sequence
function lcsLength(str1, str2) {
  const len1 = str1.length;
  const len2 = str2.length;
  const mat = initializeMatrix(len1 + 1, len2 + 1);
  // memoization roll
  for (let i = 1; i < len1 + 1; i++) {
    for (let j = 1; j < len2 + 1; j++) {
      if (str1[i] === str2[j]) {
        mat[i][j] = 1 + Math.max(mat[i-1][j], mat[i][j-1]);
      } else {
        mat[i][j] = Math.max(mat[i-1][j], mat[i][j-1]);
      }
    }
  }
  return mat[len1][len2];
}

function backtrack(mat, str1, str1Length, str2Length) {
  // testing equivalent of pass
  if (!mat[0].length) {
    return '';
  }
  let ret = '';
  let i = str1Length;
  let j = str2Length;
  while (i > 0 && j > 0) {
    if (mat[i][j] === mat[i-1][j] === mat[i][j-1]) {
      ret += str1[i];
    } else {
      if (i === 1) j--;
      else if (j === 1) i--;
      else if (mat[i-1][j] > mat[i][j-1]) i--;
      else j--;
    }
  }
  return ret.split('').reverse().join('');
}

Test.describe("Backtracking LCS", () => {
  Test.it("Simple Tests", () => {
    // 5x6 matrix for padding, "bdfe" and "abdfg"
    let mat = [
      [],
      [],
      [],
      [],
      [],
    ];
    const str = 'bdfe';
    Test.assertEquals(backtrack(mat, str, 4, 5), "bdf");
  });
})

Test.describe("LCS Length Test",() => {
  Test.it("Example tests",() => {
    Test.assertEquals(lcsLength("", ""), 0);
    Test.assertEquals(lcsLength("abc", ""), 0);
    Test.assertEquals(lcsLength("", "abc"), 0);
    Test.assertEquals(lcsLength("a", "b"), 0);
    Test.assertEquals(lcsLength("a", "a"), 1);
    Test.assertEquals(lcsLength("abc", "ac"), 2);
    Test.assertEquals(lcsLength("abcdef", "abc"), 3);
    Test.assertEquals(lcsLength("abcdef", "acf"), 3);
    Test.assertEquals(lcsLength("anothertest", "notatest"), 7);
    Test.assertEquals(lcsLength("132535365", "123456789"), 5);
    Test.assertEquals(lcsLength("nothardlythefinaltest", "zzzfinallyzzz"), 5);
    Test.assertEquals(lcsLength("abcdefghijklmnopq", "apcdefghijklmnobq"), 15);
  });
});

Test.describe("Longest Common Subsequence",() => {
  Test.it("Example tests",() => {
    Test.assertEquals(lcs("", ""), "");
    Test.assertEquals(lcs("abc", ""), "");
    Test.assertEquals(lcs("", "abc"), "");
    Test.assertEquals(lcs("a", "b"), "");
    Test.assertEquals(lcs("a", "a"), "a");
    Test.assertEquals(lcs("abc", "ac"), "ac");
    Test.assertEquals(lcs("abcdef", "abc"), "abc");
    Test.assertEquals(lcs("abcdef", "acf"), "acf");
    Test.assertEquals(lcs("anothertest", "notatest"), "nottest");
    Test.assertEquals(lcs("132535365", "123456789"), "12356");
    Test.assertEquals(lcs("nothardlythefinaltest", "zzzfinallyzzz"), "final");
    Test.assertEquals(lcs("abcdefghijklmnopq", "apcdefghijklmnobq"), "acdefghijklmnoq");
  });
});