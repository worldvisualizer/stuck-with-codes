const assert = require('assert');

/* How mocha tests are organized

run 'mocha spec.js'
|
spawn child process
|
|--------------> inside child process
  process and apply options
  |
  run spec file/s
  |
  |--------------> per spec file
    suite callbacks (e.g., 'describe')
    |
    'before' root-level pre-hook
    |
    'before' pre-hook
    |
    |--------------> per test
      'beforeEach' root-level pre-hook
      |
      'beforeEach' pre-hook
      |
      test callbacks (e.g., 'it')
      |
      'afterEach' post-hook
      |
      'afterEach' root-level post-hook
    |<-------------- per test end
    |
    'after' post-hook
    |
    'after' root-level post-hooks
  |<-------------- per spec file end
|<-------------- inside child process end

*/

class Test {
  static describe(description, callback) {
    console.log(description);
    callback();
  }

  static it(description, callback) {
    console.log(description);
    callback();
  }

  static assertEquals(obj1, obj2) {
    try {
      assert.equal(obj1, obj2);
    } catch (err) {
      console.log(err.code, err.message);
    } finally {
      const jobj1 = JSON.stringify(obj1);
      const jobj2 = JSON.stringify(obj2);
      console.log(`Expected ${jobj2}, Got ${jobj1}`);
    }
  }
}

module.exports = Test;