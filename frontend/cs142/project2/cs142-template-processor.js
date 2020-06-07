'use strict';

const regex = /{{\w*}}/g;

class Cs142TemplateProcessor {

  // template processor
  constructor(template) {
    this.template = template;
  }

  regexMatches() {
    return this.template.match(regex);
  }

  fillIn(dictionary) {
    for (let match of this.regexMatches()) {
      let replaced = false;
      for (let item of Object.entries(dictionary)) {
        let [key, value] = item;
        if (key === replaceable.substring(2, replaceable.length-2)) {
          this.template.replace(replaceable, value);
          replaced = true;
        }
      }

      if (!replaced) {
        this.template.replace(replaceable, '');
      }
    }
  }
}

module.exports = Cs142TemplateProcessor;