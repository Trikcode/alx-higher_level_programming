#!/usr/bin/node
exports.converter = function (base) {
  return function (nbase) {
    return (nbase.toString(base));
  };
};
