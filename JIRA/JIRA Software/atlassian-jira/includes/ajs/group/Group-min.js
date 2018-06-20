define("jira/ajs/group",["jira/ajs/control","jquery"],function(t,i){return t.extend({CLASS_SIGNATURE:"AJS_GROUP",init:function(){this.items=[],this.index=-1,this._assignEvents("instance",this)},addItem:function(t){this.items.push(t),this._assignEvents("item",t)},_removeItem:function(t){var e=i.inArray(t,this.items);if(e<0)throw new Error("Group: item ["+t+"] is not a member of this group");t.trigger("blur"),e<this.index&&this.index--,this.items.splice(e,1),this._unassignEvents("item",t)},removeItem:function(t){t.trigger("remove")},removeAllItems:function(){for(;this.items.length;)this.items[0].trigger("remove")},shiftFocus:function(t){if(-1===this.index&&1===t&&(t=0),this.items.length>0){var i=(Math.max(0,this.index)+this.items.length+t)%this.items.length;this.items[i].trigger("focus"),this.trigger("change:activeItem",this.items[i])}},prepareForInput:function(){this._assignEvents("keys",document)},_events:{instance:{focus:function(){0!==this.items.length&&(this.index<0?this.items[0].trigger("focus"):this._assignEvents("keys",document))},blur:function(){this.index>=0?this.items[this.index].trigger("blur"):this._unassignEvents("keys",document)}},keys:{"aui:keydown":function(t){this._handleKeyEvent(t)}},item:{focus:function(t){var e=this.index;this.index=i.inArray(t.target,this.items),e<0?this.trigger("focus"):e!==this.index&&this.items[e].trigger("blur")},blur:function(t){this.index===i.inArray(t.target,this.items)&&(this.index=-1,this.trigger("blur"))},remove:function(t){this._removeItem(t.target)}}},keys:{}})}),AJS.namespace("AJS.Group",null,require("jira/ajs/group"));