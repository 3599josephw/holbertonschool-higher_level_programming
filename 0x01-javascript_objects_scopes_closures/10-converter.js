#!usr/bin/node
exports.converter = function (base) {
  function temp (number) {
    return number.toString(base);
  }
  return temp;
};
