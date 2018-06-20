!function(){"use strict";function e(){k("label.overlabel").overlabel()}function t(){var e=k("div.results"),t=e.width();e.bind("resultsWidthChanged",function(){k(this).css("width",100/t*(t-(parseInt(k(document.documentElement).prop("scrollWidth"),10)-k(window).width()))+"%")}),k(window).resize(function(){e.trigger("resultsWidthChanged")}),e.trigger("resultsWidthChanged"),k("#issuenav").bind("contractBlock expandBlock",function(){k(".results").trigger("resultsWidthChanged")})}function i(){k(".fieldTabs li").click(function(e){e.preventDefault(),e.stopPropagation();var t=k(this);t.hasClass("active")||(k(".fieldTabs li.active").removeClass("active"),t.addClass("active"),k(".fieldTabArea.active").removeClass("active"),k("#"+t.attr("rel")).addClass("active"))})}function a(){k("form").handleAccessKeys(),Q.bind("dialogContentReady",function(){k("form",this.$content).handleAccessKeys({selective:!1})})}function n(){Q.keydown(function(e){S.current&&27===e.which&&!k(e.target).is(":input")&&S.current.hide()})}function r(){new x({blockSelector:".twixi-block",storageCollectionName:"twixi"}).addCallback("toggle",function(){A.getStalker().trigger("stalkerHeightUpdated")}).addTrigger(".action-head .action-details","click"),new x({blockSelector:"#issue-filter .toggle-wrap:not(#navigator-filter-subheading-textsearch-group)",triggerSelector:".toggle-trigger",collapsedClass:"expanded",expandedClass:"collapsed",storageCollectionName:"navSimpleSearch"}),new x({blockSelector:".twixi-block",triggerSelector:".twixi-trigger",storageCollectionName:"twixi"}),new x({blockSelector:"#issuenav",triggerSelector:"a.toggle-lhc",collapsedClass:"lhc-collapsed",storageCollectionName:"lhc-state",autoFocusTrigger:!1}),k(".error","#issue-filter").parents(".toggle-wrap").removeClass("collapsed").addClass("expanded"),k("fieldset.content-toggle input[type='radio']").live("change",function(){var e=k(this);e.closest(".content-toggle").find("input[type='radio']").each(function(){var e=k(this);k("#"+e.attr("name")+"-"+e.val()+"-content").addClass("hidden")}),k("#"+e.attr("name")+"-"+e.val()+"-content").removeClass("hidden")})}function s(){k("#log-work-adjust-estimate-new-value,#log-work-adjust-estimate-manual-value").attr("disabled","disabled"),k("#log-work-adjust-estimate-"+k("input[name=worklog_adjustEstimate]:checked,input[name=adjustEstimate]:checked").val()+"-value").removeAttr("disabled"),k("input[name=worklog_adjustEstimate],input[name=adjustEstimate]").change(function(){k("#log-work-adjust-estimate-new-value,#log-work-adjust-estimate-manual-value").attr("disabled","disabled"),k("#log-work-adjust-estimate-"+k(this).val()+"-value").removeAttr("disabled")})}function o(){var e=k("input:checked");0!==e.length&&("forgot-login-rb-forgot-password"===e.attr("id")?(k("#username,#password").addClass("hidden"),k("#password").removeClass("hidden")):"forgot-login-rb-forgot-username"===e.attr("id")&&(k("#username,#password").addClass("hidden"),k("#username").removeClass("hidden"))),k("#forgot-login-rb-forgot-password").change(function(){k("#username,#password").addClass("hidden"),k("#password").removeClass("hidden")}),k("#forgot-login-rb-forgot-username").change(function(){k("#username,#password").addClass("hidden"),k("#username").removeClass("hidden")})}function l(){k("input.upfile").each(function(){var e=k(this),t=e.closest(".field-group");e.change(function(){e.val().length>0&&t.next(".field-group").removeClass("hidden")})})}function c(){Q.on("keypress","textarea",I.submitOnCtrlEnter),k("#jqltext").keypress(I.submitOnEnter)}function d(){var e=k("#browser-warning");k(".icon-close",e).click(function(){e.slideUp("fast"),N.save("UNSUPPORTED_BROWSER_WARNING","handled")})}function u(){k("form").submit(function(e){var t=new k.Event("before-submit");k(this).trigger(t),t.isDefaultPrevented()&&e.preventDefault()})}function f(){var e="#comment, #environment, #description";Q.bind("tabSelect",function(t,i){i.pane.find(e).expandOnInput()}),k(e).expandOnInput(200),Q.bind("dialogContentReady",function(t,i){i.get$popupContent().bind("tabSelect",function(t,i){i.pane.find(e).expandOnInput(200)}).find(e).expandOnInput(200)}),Q.bind("showWikiInput",function(t,i){i.find(e).expandOnInput()})}function g(){var e=k("form.aui"),t=k("a.cancel",e);L.isIE()&&L.majorVersion()<12&&t.attr("accessKey")&&t.focus(function(e){e.altKey&&(k(this).mousedown(),window.location.href=t.attr("href"))})}function h(){var e=function(e){k(e).closest(".availableActionRow").find("td:first :checkbox").attr("checked",!0)};k("#availableActionsTable tr.availableActionRow").children("td:last-child").find(":input").change(function(){e(this)})}function m(){var e=function(e){k(e).closest("tr").prev().find("td:first :checkbox").attr("checked",!0)};k("#availableActionsTable .availableActionRowMultiSelect").children("td:last-child").find(":input").change(function(){e(this)})}function p(){k("#availableActionsTable .availableActionMultiSelect select").change(function(){var e=k(this);e.closest("tr").next().toggleClass("hidden","removeall"===e.val())})}function v(){if(j.showmonitor){var e=k("<div class='perf-monitor'/>"),t=j["jira.request.server.time"]>2e3,i=j.jiraSQLstatements>50;t&&e.addClass("tooslow"),i&&e.addClass("toomanysql"),k("#header-top").append(e),new S(e,"perf-monitor-dialog",function(e,t,i){var a="<div>Page render time <strong>"+j["jira.request.server.time"]+" ms</strong>";j.jiraSQLstatements?(a+=" / SQL <strong>"+j.jiraSQLstatements+"@"+j.jiraSQLtime+" ms</strong></br>",a+='<a target="_blank" href='+D+"/sqldata.jsp?requestId="+j["jira.request.id"]+">More...</a>"):a+=" / No SQL statments",a+="</div>",e.empty().append(a),i()})}}function b(){k(".clickable").click(function(){window.location.href=k(this).find("a").attr("href")})}function w(e){k(".projects-list-trigger",e).each(function(){var e=k(this);e.click(!1);var t=e.attr("href");new S(this,t.substring(1),function(e,i,a){e.html(k(t).html()),a()},{onHover:!0,hideDelay:500,width:240})})}function C(){Q.on("click","[data-helplink=local]",function(e){var t=this.getAttribute("href");return window.open(t,"jiraLocalHelp","resizable, scrollbars=yes").focus(),e.preventDefault(),!1})}var k=require("jquery"),j=require("aui/params"),S=require("aui/inline-dialog"),y=require("aui/tabs"),x=require("jira/toggleblock/toggle-block"),q=require("jira/ajs/browser/describe-browser"),A=require("jira/issue"),E=require("jira/message"),N=require("jira/data/cookie"),I=require("jira/util/forms"),R=require("jira/util/formatter"),O=require("jira/util/data/meta"),T=require("jira/util/events"),L=require("jira/util/navigator"),M=require("jira/skate"),W=require("jira/util/strings"),P=require("wrm/context-path"),D=P(),Q=k(document);M("shared-item-trigger",{type:M.type.CLASSNAME,attached:function(e){var t=e.getAttribute("href");new S(e,t.substring(1),function(e,i,a){e.html(k(t).html()),a()},{width:240})}}),k(function(){r(),e(),t(),i(),a(),s(),o(),l(),c(),d(),u(),f(),g(),h(),m(),p(),n(),v(),b(),C(),w()}),q(),function(){T.bind("dialogContentReady",function(){y.setup()})}(),M("js-filter-form-edit",{type:M.type.CLASSNAME,extends:"form",events:{submit:function(e,t){if(!t.defaultPrevented){var i=W.escapeHtml(e.elements.filterName.value);E.showMsgOnReload(R.I18n.getText("editfilter.save.success",i),{type:"SUCCESS",closeable:!0,target:"body:not(:has(#filter-edit))"})}}}}),M("js-filter-form-subscription",{type:M.type.CLASSNAME,extends:"form",events:{submit:function(e,t){if(!t.defaultPrevented){var i=e.elements.groupName.value||O.get("remote-user-fullname");E.showMsgOnReload(R.I18n.getText("subscriptions.add.success",W.escapeHtml(i)),{type:"SUCCESS",closeable:!0,target:"body:not(:has(#filter-subscription))"})}}}})}();