'use strict';

function cs142MakeMultiFilter(originalArray) {
  return function arrayFilterer(filterCriteria, callback) {
    let currentArray = originalArray;

    if (callback) {
      callback.bind(this);
      callback(currentArray);
    }
  }
}

module.exports = cs142MakeMultiFilter;