define("jira/project/browse/projectmodel",["backbone","underscore","jira/project/browse/projecttypesservice"],function(e,t,o){"use strict";return e.Model.extend({toJSON:function(){var e,c,r=t.clone(this.attributes);return this.collection&&this.collection.pageableCollection&&(e=this.collection.pageableCollection.categories),this.get("projectCategoryId")&&e&&(c=e.get(this.get("projectCategoryId")))&&(r.projectCategoryName=c.get("name")),r.projectTypeIcon=o.getProjectTypeIcon(r.projectTypeKey),r}})});