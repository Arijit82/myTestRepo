define("jira/page/atl/prefetch",["jira/util/data/meta","jira/data/local-storage","jira/ajs/dark-features","jquery","wrm/context-path"],function(e,t,r,n,i){"use strict";function a(e){n("<link />",{rel:"prefetch",href:e}).appendTo("head")}function s(e){var t=e.sections;if(t){var r=t.filter(function(e){return"issues_history_main"===e.id});if(r.length&&0!==r[0].items.length){return r[0].items[0].url}}}function u(e,t){for(var r;r=t.exec(e);){a(r[1].replace(/&amp;/g,"&"))}}function c(){t.setItem(h,d)}function f(e){u(e,/<script.+?src="(.+?)".+?<\/script>/g),u(e,/<link.+?rel="stylesheet".+?href="(.+?)".+?>/g),c()}function o(){return!!r.isEnabled("jira.issue.prefetch")&&(1===n("#isNavigator").length?(c(),!1):e.get("issue-key")?(c(),!1):d!==t.getItem(h))}function l(e){var t=s(e);t&&p(t)}function p(e){n.get(e,f)}function g(){o()&&n.ajax({url:i()+"/rest/api/1.0/menus/find_link?inAdminMode=false",dataType:"json"}).done(l)}var h="jira.issue.prefetch.last.superbatch",d=function(){var e=new Date,t=e.getFullYear().toString()+e.getMonth().toString()+e.getDate().toString(),r=n("head > script").filter(function(e,t){return t.src.indexOf("/_super")>0});return(r.length>0?r[0].src:"empty")+t}();return{prefetchResourcesForUrl:p,prefetchViewIssueResources:g}});