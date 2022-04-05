#!/usr/bin/node
exports.esrever = function (list) {
  const rlist = [];
  for (let i = list.length - 1; i >= 0; i--) {
    rlist.push(list[i]);
  }
  return rlist;
};
