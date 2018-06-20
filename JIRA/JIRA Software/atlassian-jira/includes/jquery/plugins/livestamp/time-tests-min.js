AJS.test.require(["jira.webresources:jira-global","jira.webresources:jquery-livestamp"],function(){"use strict";var e=require("jira/jquery/plugins/livestamp/time"),t=require("jira/moment"),a=require("jira/util/formatter");module("time.js Test Suite",{setup:function(){sinon.spy(a,"format")},teardown:function(){a.format.restore(),e.restoreDefaultRelativeTranslations()},assertRelativeDate:function(t,s,o,i,r){a.format.reset();var n=e.formatDateWithRelativeAge(o.clone(),e.FormatType.types.shortAge,s.clone());equal(n,i,t),void 0!==r&&sinon.assert.alwaysCalledWith(a.format,i,r)},assertRelativeDateFromNow:function(e,a,s){var o=t("2012-02-16T04:00:00.000");this.assertRelativeDate("Now "+e,o.clone(),o.clone().add(t.duration(e)),a,s)},assertRelativeDateFromMidnight:function(e,a,s){var o=t("2012-02-16T00:00:00.000");this.assertRelativeDate("Midnight "+e,o.clone(),o.clone().add(t.duration(e)),a,s)},assertAMomentAgo:function(e){this.assertRelativeDateFromNow("",e),this.assertRelativeDateFromNow("-00:00:59",e),this.assertRelativeDateFromNow("-00:00:59.999",e)},assertOneMinuteAgo:function(e){this.assertRelativeDateFromNow("-00:01:00",e),this.assertRelativeDateFromNow("-00:01:00.001",e),this.assertRelativeDateFromNow("-00:01:29",e),this.assertRelativeDateFromNow("-00:01:30",e),this.assertRelativeDateFromNow("-00:01:31",e),this.assertRelativeDateFromNow("-00:01:59.999",e)},assertXMinutesAgo:function(e){this.assertRelativeDateFromNow("-00:02:00",e,2),this.assertRelativeDateFromNow("-00:02:01",e,2),this.assertRelativeDateFromNow("-00:02:29",e,2),this.assertRelativeDateFromNow("-00:02:30",e,2),this.assertRelativeDateFromNow("-00:02:31",e,2),this.assertRelativeDateFromNow("-00:29:00",e,29),this.assertRelativeDateFromNow("-00:30:00",e,30),this.assertRelativeDateFromNow("-00:31:00",e,31),this.assertRelativeDateFromNow("-00:49:59.999",e,49)},assertOneHourAgo:function(e){this.assertRelativeDateFromNow("-00:50:00",e),this.assertRelativeDateFromNow("-00:50:00.001",e),this.assertRelativeDateFromNow("-01:29:00",e),this.assertRelativeDateFromNow("-01:29:59.999",e)},assertXHoursAgo:function(e){this.assertRelativeDateFromNow("-01:30:00",e,2),this.assertRelativeDateFromNow("-01:31:00",e,2),this.assertRelativeDateFromNow("-03:59:59",e,4),this.assertRelativeDateFromNow("-04:00:00",e,4),this.assertRelativeDateFromNow("-04:00:01",e,4),this.assertRelativeDateFromNow("-04:59:59",e,5),this.assertRelativeDateFromNow("-05:00:00",e,5),this.assertRelativeDateFromMidnight("-01:30:00",e,2),this.assertRelativeDateFromMidnight("-05:00:00",e,5)},assertOneDayAgo:function(e){this.assertRelativeDateFromNow("-05:00:00.001",e),this.assertRelativeDateFromNow("-1.00:00:00",e),this.assertRelativeDateFromNow("-1.04:00:00",e),this.assertRelativeDateFromMidnight("-05:00:00.001",e),this.assertRelativeDateFromMidnight("-23:59:59",e),this.assertRelativeDateFromMidnight("-1.00:00:00",e)},assertXDaysAgo:function(e){this.assertRelativeDateFromNow("-1.04:00:00.001",e),this.assertRelativeDateFromNow("-2.00:00:00",e,2),this.assertRelativeDateFromNow("-6.00:00:00",e,6),this.assertRelativeDateFromNow("-6.23:59:59.999",e,6),this.assertRelativeDateFromMidnight("-1.00:00:00.001",e,2),this.assertRelativeDateFromMidnight("-2.00:00:00",e,2),this.assertRelativeDateFromMidnight("-2.23:59:59.999",e,2),this.assertRelativeDateFromMidnight("-3.00:00:00",e,3),this.assertRelativeDateFromMidnight("-3.00:00:00.001",e,3),this.assertRelativeDateFromMidnight("-6.23:59:59.999",e,6)},assertOneWeekAgo:function(e){this.assertRelativeDateFromNow("-7.00:00:00",e),this.assertRelativeDateFromNow("-7.23:59:59.999",e)},assertInAMoment:function(e){this.assertRelativeDateFromNow("+00:00:00.001",e),this.assertRelativeDateFromNow("+00:00:59",e)},assertInOneMinute:function(e){this.assertRelativeDateFromNow("+00:01:00",e),this.assertRelativeDateFromNow("+00:01:00.001",e),this.assertRelativeDateFromNow("+00:01:29",e),this.assertRelativeDateFromNow("+00:01:30",e),this.assertRelativeDateFromNow("+00:01:31",e),this.assertRelativeDateFromNow("+00:01:59.999",e)},assertInXMinutes:function(e){this.assertRelativeDateFromNow("+00:02:00",e,2),this.assertRelativeDateFromNow("+00:02:01",e,2),this.assertRelativeDateFromNow("+00:02:29",e,2),this.assertRelativeDateFromNow("+00:02:30",e,2),this.assertRelativeDateFromNow("+00:02:31",e,2),this.assertRelativeDateFromNow("+00:29:00",e,29),this.assertRelativeDateFromNow("+00:30:00",e,30),this.assertRelativeDateFromNow("+00:31:00",e,31),this.assertRelativeDateFromNow("+00:49:59.999",e,49)},assertInOneHour:function(e){this.assertRelativeDateFromNow("+00:50:00",e),this.assertRelativeDateFromNow("+00:50:00.001",e),this.assertRelativeDateFromNow("+01:29:00",e),this.assertRelativeDateFromNow("+01:29:59.999",e)},assertInXHours:function(e){this.assertRelativeDateFromNow("+01:30:00",e,2),this.assertRelativeDateFromNow("+01:31:00",e,2),this.assertRelativeDateFromNow("+19:59:59.999",e,20),this.assertRelativeDateFromMidnight("+01:30:00",e,2),this.assertRelativeDateFromMidnight("+05:00:00",e,5),this.assertRelativeDateFromMidnight("+23:59:59",e,24)},assertInOneDay:function(e){this.assertRelativeDateFromNow("+20:00:00",e),this.assertRelativeDateFromNow("+1.00:00:00",e),this.assertRelativeDateFromNow("+1.19:59:59.999",e),this.assertRelativeDateFromMidnight("+1.00:00:00",e),this.assertRelativeDateFromMidnight("+1.23:59:59.999",e)},assertInXDays:function(e){this.assertRelativeDateFromNow("+1.20:00:00",e,2),this.assertRelativeDateFromNow("+2.00:00:00",e,2),this.assertRelativeDateFromNow("+6.00:00:00",e,6),this.assertRelativeDateFromNow("+6.23:59:59.999",e,6),this.assertRelativeDateFromMidnight("+2.00:00:00",e,2),this.assertRelativeDateFromMidnight("+2.23:59:59.999",e,2),this.assertRelativeDateFromMidnight("+3.00:00:00",e,3),this.assertRelativeDateFromMidnight("+3.00:00:00.001",e,3),this.assertRelativeDateFromMidnight("+6.23:59:59.999",e,6)},assertInOneWeek:function(e){this.assertRelativeDateFromNow("+7.00:00:00",e),this.assertRelativeDateFromNow("+7.23:59:59",e)}}),test("format relative dates",function(){this.assertAMomentAgo("common.date.relative.a.moment.ago"),this.assertOneMinuteAgo("common.date.relative.one.minute.ago"),this.assertXMinutesAgo("common.date.relative.x.minutes.ago"),this.assertOneHourAgo("common.date.relative.one.hour.ago"),this.assertXHoursAgo("common.date.relative.x.hours.ago"),this.assertOneDayAgo("common.date.relative.one.day.ago"),this.assertXDaysAgo("common.date.relative.x.days.ago"),this.assertOneWeekAgo("common.date.relative.one.week.ago"),this.assertInAMoment("common.date.relative.in.a.moment"),this.assertInOneMinute("common.date.relative.in.one.minute"),this.assertInXMinutes("common.date.relative.in.x.minutes"),this.assertInOneHour("common.date.relative.in.one.hour"),this.assertInXHours("common.date.relative.in.x.hours"),this.assertInOneDay("common.date.relative.in.one.day"),this.assertInXDays("common.date.relative.in.x.days"),this.assertInOneWeek("common.date.relative.in.one.week")}),test("format relative dates with a custom text",function(){e.setRelativeTranslations({aMomentAgo:"custom-common.date.relative.a.moment.ago",oneMinuteAgo:"custom-common.date.relative.one.minute.ago",xMinutesAgo:"custom-common.date.relative.x.minutes.ago",oneHourAgo:"custom-common.date.relative.one.hour.ago",xHoursAgo:"custom-common.date.relative.x.hours.ago",oneDayAgo:"custom-common.date.relative.one.day.ago",xDaysAgo:"custom-common.date.relative.x.days.ago",oneWeekAgo:"custom-common.date.relative.one.week.ago",inAMoment:"custom-common.date.relative.in.a.moment",inOneMinute:"custom-common.date.relative.in.one.minute",inXMinutes:"custom-common.date.relative.in.x.minutes",inOneHour:"custom-common.date.relative.in.one.hour",inXHours:"custom-common.date.relative.in.x.hours",inOneDay:"custom-common.date.relative.in.one.day",inXDays:"custom-common.date.relative.in.x.days",inOneWeek:"custom-common.date.relative.in.one.week"}),this.assertAMomentAgo("custom-common.date.relative.a.moment.ago"),this.assertOneMinuteAgo("custom-common.date.relative.one.minute.ago"),this.assertXMinutesAgo("custom-common.date.relative.x.minutes.ago"),this.assertOneHourAgo("custom-common.date.relative.one.hour.ago"),this.assertXHoursAgo("custom-common.date.relative.x.hours.ago"),this.assertOneDayAgo("custom-common.date.relative.one.day.ago"),this.assertXDaysAgo("custom-common.date.relative.x.days.ago"),this.assertOneWeekAgo("custom-common.date.relative.one.week.ago"),this.assertInAMoment("custom-common.date.relative.in.a.moment"),this.assertInOneMinute("custom-common.date.relative.in.one.minute"),this.assertInXMinutes("custom-common.date.relative.in.x.minutes"),this.assertInOneHour("custom-common.date.relative.in.one.hour"),this.assertInXHours("custom-common.date.relative.in.x.hours"),this.assertInOneDay("custom-common.date.relative.in.one.day"),this.assertInXDays("custom-common.date.relative.in.x.days"),this.assertInOneWeek("custom-common.date.relative.in.one.week")}),test("format date with format string - format is correct (short, long, full, timestamp)",function(){function e(e,t,a){a=a||"timestamp";try{equal(s.formatDateWithFormatString(e.clone(),s.FormatType.types[a]),t,"formatted date is correct for "+e.toDate().toUTCString())}catch(t){ok(!1,"formatDateWithFormatString failed with args "+e.toDate().toUTCString()+" and "+a+".\nCause: "+t.toString())}}var t=AJS.test.mockableModuleContext();t.mock("jira/moment/moment.jira.datetime-formats",{dateFormats:{},lookAndFeelFormats:{}});var a=t.require("jira/moment"),s=t.require("jira/jquery/plugins/livestamp/time"),o=a(new Date("2012-02-16T00:00:00.000+03:00")),i=o.clone().add("d",1).subtract("ms",1);e(i,"LLL","timestamp"),e(i,"LLL","full"),e(i,"LL","long"),e(i,"ll","short")})});