define("jira/util/logger",["exports"],function(n){"use strict";function o(){}function e(n){return"undefined"!=typeof console&&"function"==typeof console[n]?console[n].bind(console):function(){if("undefined"!=typeof console&&console[n])return Function.prototype.apply.call(console[n],console,arguments)}}function r(n){return e(n)||o}n.log=r("log"),n.info=r("info"),n.warn=r("warn"),n.error=r("error"),n.debug=r("debug"),n.trace=function n(){var e=window.__tracer||o;if(e!==n)return e.apply(e,arguments)}});