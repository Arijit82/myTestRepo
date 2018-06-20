define("jira/ajs/select/dropdown-select",["jira/ajs/layer/layer-constants","jira/ajs/control","jira/ajs/select/select-model","jira/ajs/layer/inline-layer-factory","jira/ajs/list/list","jquery"],function(e,t,n,i,r,s){"use strict";return t.extend({init:function(t){var o=this;this.model=new n(t),this.model.$element.hide(),this._createFurniture(),this.dropdownController=i.createInlineLayers({alignment:e.LEFT,width:200,hideOnScroll:".issue-container",content:s(".aui-list",this.$container)}),this.dropdownController.layer().addClass("select-menu"),this.listController=new r({containerSelector:s(".aui-list",this.$container),groupSelector:"ul.opt-group",itemSelector:"li:not(.no-suggestions)",selectionHandler:function(e){o._selectionHandler(this.getFocused(),e),e.preventDefault()}}),this._assignEventsToFurniture()},show:function(){this.listController.generateListFromJSON(this.model.getAllDescriptors()),this.dropdownController.show(),this.listController.index=0,this.listController.focus(),this.listController.enable()},_assignEventsToFurniture:function(){this._assignEvents("trigger",this.$trigger)},_createFurniture:function(){var e=this.model.$element.attr("id");this.$container=this._render("container",e),this.$trigger=this.model.$element.prev("a").appendTo(this.$container),this.$container.append(this._render("suggestionsContainer",e)),this.$container.insertBefore(this.model.$element)},_renders:{container:function(e){return s('<div class="select-menu" />').attr("id",e+"-multi-select")},suggestionsContainer:function(e){return s('<div class="aui-list aui-list-checked" tabindex="-1" />').attr("id",e+"-suggestions")}},_selectionHandler:function(e){var t=this,n=0;this.model.setSelected(e.data("descriptor")),this.dropdownController.content().find(".aui-checked").removeClass(".aui-checked"),e.addClass(".aui-checked");var i=window.setInterval(function(){n++,e.toggleClass(".aui-checking"),n>2&&(clearInterval(i),t.dropdownController.hide())},80)},_events:{trigger:{click:function(e){this.show(),e.preventDefault(),e.stopPropagation()}}}})}),AJS.namespace("AJS.SelectMenu",null,require("jira/ajs/select/dropdown-select")),AJS.namespace("AJS.DropdownSelect",null,require("jira/ajs/select/dropdown-select"));