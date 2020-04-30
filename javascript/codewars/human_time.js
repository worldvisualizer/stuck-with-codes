const formats = [
  [60, 'second'],
  [60, 'minute'],
  [24, 'hour'],
  [365, 'day'],
  [1, 'year'],
];

function englishForm(seconds, level) {
  const english = formats[level][1];
  return (seconds !== 1) ? english + 's' : english;
}

function formatDuration(seconds) {
  if (seconds === 0) {
    return 'now';
  }
  let answer = [];
  for (let i = 0; i < formats.length; i++) {
    if (seconds === 0) {
      break;
    }
    let [ denom, word ] = formats[i];
    let num = seconds % denom;
    if (num !== 0) {
      answer.push(`${num} ${englishForm(num, i)}`);
    } else if (i === formats.length - 1) {
      answer.push(`${seconds} ${englishForm(seconds, i)}`)
    }
    seconds = Math.floor(seconds / denom);
  }
  answer.reverse();
  if (answer.length > 1) {
    return answer.slice(0,-1).join(', ') + ' and ' + answer[answer.length - 1];
  }
  return answer[0];
}

function formatDurationExample1(seconds) {
  var time = { year: 31536000, day: 86400, hour: 3600, minute: 60, second: 1 },
      res = [];

  if (seconds === 0) return 'now';
  
  for (var key in time) {
    if (seconds >= time[key]) {
      var val = Math.floor(seconds/time[key]);
      res.push(val += val > 1 ? ' ' + key + 's' : ' ' + key);
      seconds = seconds % time[key];
    }
  }
 
  return res.length > 1 ? res.join(', ').replace(/,([^,]*)$/,' and'+'$1') : res[0]
}

function formatDurationExample2(seconds) {
  if(!seconds)return "now";
  var strout = "";
  var s = seconds%60;
  seconds = (seconds-s)/60;
  var m = seconds%60;
  seconds = (seconds-m)/60;
  var h = seconds%24;
  seconds = (seconds-h)/24;
  var d = seconds%365;
  seconds = (seconds-d)/365;
  var y = seconds;
  
  var english=[];
  if(y)english.push(y+" year"+(y>1?'s':''));
  if(d)english.push(d+" day"+(d>1?'s':''));
  if(h)english.push(h+" hour"+(h>1?'s':''));
  if(m)english.push(m+" minute"+(m>1?'s':''));
  if(s)english.push(s+" second"+(s>1?'s':''));
  
  return english.join(", ").replace(/,([^,]*)$/," and$1");
  
}


function assertEquals(str1, str2) {
  console.log(typeof str1 === 'string' && str1 === str2);
  console.log(`Expected ${str2}, got ${str1}`);
}

assertEquals(formatDuration(1), "1 second");
assertEquals(formatDuration(62), "1 minute and 2 seconds");
assertEquals(formatDuration(120), "2 minutes");
assertEquals(formatDuration(3600), "1 hour");
assertEquals(formatDuration(3662), "1 hour, 1 minute and 2 seconds");

assertEquals(formatDuration(234234233443), '');