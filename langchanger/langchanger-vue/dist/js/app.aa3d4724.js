(function(n){function e(e){for(var a,r,u=e[0],i=e[1],s=e[2],l=0,d=[];l<u.length;l++)r=u[l],Object.prototype.hasOwnProperty.call(o,r)&&o[r]&&d.push(o[r][0]),o[r]=0;for(a in i)Object.prototype.hasOwnProperty.call(i,a)&&(n[a]=i[a]);f&&f(e);while(d.length)d.shift()();return c.push.apply(c,s||[]),t()}function t(){for(var n,e=0;e<c.length;e++){for(var t=c[e],a=!0,r=1;r<t.length;r++){var u=t[r];0!==o[u]&&(a=!1)}a&&(c.splice(e--,1),n=i(i.s=t[0]))}return n}var a={},r={app:0},o={app:0},c=[];function u(n){return i.p+"js/"+({}[n]||n)+"."+{"chunk-02c844c8":"a5abaf35","chunk-13e6c81e":"473cd755","chunk-2d215fa4":"4ea4d4cd","chunk-2d22d746":"9bb7dfd4","chunk-565adc48":"6f6498a3","chunk-58a5cd18":"b12029a8","chunk-5f75d802":"3bf7013b","chunk-662bc62a":"1704077c","chunk-748d435b":"2651d00f","chunk-75f186c3":"210dd5f9","chunk-7841f5b7":"e8796f93","chunk-789b8aa0":"08c84c27","chunk-7e3fde65":"efca451e","chunk-9734388a":"783e0284","chunk-b0dbdeaa":"ffe3ac2d","chunk-da3e29d0":"332bc344","chunk-e74b1dd8":"eb41bc07"}[n]+".js"}function i(e){if(a[e])return a[e].exports;var t=a[e]={i:e,l:!1,exports:{}};return n[e].call(t.exports,t,t.exports,i),t.l=!0,t.exports}i.e=function(n){var e=[],t={"chunk-02c844c8":1,"chunk-13e6c81e":1,"chunk-565adc48":1,"chunk-58a5cd18":1,"chunk-5f75d802":1,"chunk-662bc62a":1,"chunk-748d435b":1,"chunk-75f186c3":1,"chunk-7841f5b7":1,"chunk-789b8aa0":1,"chunk-7e3fde65":1,"chunk-9734388a":1,"chunk-b0dbdeaa":1,"chunk-da3e29d0":1,"chunk-e74b1dd8":1};r[n]?e.push(r[n]):0!==r[n]&&t[n]&&e.push(r[n]=new Promise((function(e,t){for(var a="css/"+({}[n]||n)+"."+{"chunk-02c844c8":"02a744db","chunk-13e6c81e":"a37f5137","chunk-2d215fa4":"31d6cfe0","chunk-2d22d746":"31d6cfe0","chunk-565adc48":"e3299b2b","chunk-58a5cd18":"4d087b3f","chunk-5f75d802":"72c2013f","chunk-662bc62a":"1bb01b95","chunk-748d435b":"2d827b10","chunk-75f186c3":"0653a2ae","chunk-7841f5b7":"007bdb4f","chunk-789b8aa0":"7f5e17f6","chunk-7e3fde65":"d6ce0098","chunk-9734388a":"6cfb7a7f","chunk-b0dbdeaa":"5211288f","chunk-da3e29d0":"6e54f08b","chunk-e74b1dd8":"4bf9c39f"}[n]+".css",o=i.p+a,c=document.getElementsByTagName("link"),u=0;u<c.length;u++){var s=c[u],l=s.getAttribute("data-href")||s.getAttribute("href");if("stylesheet"===s.rel&&(l===a||l===o))return e()}var d=document.getElementsByTagName("style");for(u=0;u<d.length;u++){s=d[u],l=s.getAttribute("data-href");if(l===a||l===o)return e()}var f=document.createElement("link");f.rel="stylesheet",f.type="text/css",f.onload=e,f.onerror=function(e){var a=e&&e.target&&e.target.src||o,c=new Error("Loading CSS chunk "+n+" failed.\n("+a+")");c.code="CSS_CHUNK_LOAD_FAILED",c.request=a,delete r[n],f.parentNode.removeChild(f),t(c)},f.href=o;var h=document.getElementsByTagName("head")[0];h.appendChild(f)})).then((function(){r[n]=0})));var a=o[n];if(0!==a)if(a)e.push(a[2]);else{var c=new Promise((function(e,t){a=o[n]=[e,t]}));e.push(a[2]=c);var s,l=document.createElement("script");l.charset="utf-8",l.timeout=120,i.nc&&l.setAttribute("nonce",i.nc),l.src=u(n);var d=new Error;s=function(e){l.onerror=l.onload=null,clearTimeout(f);var t=o[n];if(0!==t){if(t){var a=e&&("load"===e.type?"missing":e.type),r=e&&e.target&&e.target.src;d.message="Loading chunk "+n+" failed.\n("+a+": "+r+")",d.name="ChunkLoadError",d.type=a,d.request=r,t[1](d)}o[n]=void 0}};var f=setTimeout((function(){s({type:"timeout",target:l})}),12e4);l.onerror=l.onload=s,document.head.appendChild(l)}return Promise.all(e)},i.m=n,i.c=a,i.d=function(n,e,t){i.o(n,e)||Object.defineProperty(n,e,{enumerable:!0,get:t})},i.r=function(n){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(n,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(n,"__esModule",{value:!0})},i.t=function(n,e){if(1&e&&(n=i(n)),8&e)return n;if(4&e&&"object"===typeof n&&n&&n.__esModule)return n;var t=Object.create(null);if(i.r(t),Object.defineProperty(t,"default",{enumerable:!0,value:n}),2&e&&"string"!=typeof n)for(var a in n)i.d(t,a,function(e){return n[e]}.bind(null,a));return t},i.n=function(n){var e=n&&n.__esModule?function(){return n["default"]}:function(){return n};return i.d(e,"a",e),e},i.o=function(n,e){return Object.prototype.hasOwnProperty.call(n,e)},i.p="/",i.oe=function(n){throw console.error(n),n};var s=window["webpackJsonp"]=window["webpackJsonp"]||[],l=s.push.bind(s);s.push=e,s=s.slice();for(var d=0;d<s.length;d++)e(s[d]);var f=l;c.push([0,"chunk-vendors"]),t()})({0:function(n,e,t){n.exports=t("56d7")},"034f":function(n,e,t){"use strict";var a=t("85ec"),r=t.n(a);r.a},2491:function(n,e,t){},"56d7":function(n,e,t){"use strict";t.r(e);t("e260"),t("e6cf"),t("cca6"),t("a79d");var a=t("2b0e"),r=function(){var n=this,e=n.$createElement,t=n._self._c||e;return t("div",{attrs:{id:"app"}},[t("Header"),t("section",{attrs:{id:"content"}},[t("div",{attrs:{id:"wrapper"}},[t("section",{attrs:{id:"main"}},[t("router-view")],1),t("Footer")],1)])],1)},o=[],c=function(){var n=this,e=n.$createElement,a=n._self._c||e;return a("header",[a("div",{staticClass:"username-div"},[n.loggedIn?a("p",{attrs:{id:"username-p"}},[n._v("Вы вошли как: "),a("a",{attrs:{href:/user/+n.USERID}},[n._v(n._s(n.CLIENT_USERNAME))])]):n._e()]),a("nav",[a("Finder"),n._m(0),a("MainMenu")],1),a("div",[n.loggedIn?n._e():a("router-link",{attrs:{to:"/login"}},[a("ButtonWhite",{staticClass:"sign-in",attrs:{value:"Войти"}})],1),n.loggedIn?a("router-link",{attrs:{to:"/logout"}},[a("ButtonWhite",{staticClass:"sign-in",attrs:{value:"Выйти"}})],1):n._e(),a("img",{attrs:{src:t("c626")}})],1)])},u=[function(){var n=this,e=n.$createElement,a=n._self._c||e;return a("a",{attrs:{href:"/"}},[a("img",{attrs:{src:t("a5f7")}})])}],i=t("5530"),s=function(){var n=this,e=n.$createElement;n._self._c;return n._m(0)},l=[function(){var n=this,e=n.$createElement,a=n._self._c||e;return a("div",[a("input",{attrs:{type:"text",placeholder:"Поиск..."}}),a("button",[a("img",{attrs:{src:t("98fb")}})])])}],d={name:"Finder"},f=d,h=(t("aa47"),t("2877")),p=Object(h["a"])(f,s,l,!1,null,"13b5dabe",null),m=p.exports,b=function(){var n=this,e=n.$createElement;n._self._c;return n._m(0)},g=[function(){var n=this,e=n.$createElement,t=n._self._c||e;return t("ul",[t("li",[t("a",{attrs:{href:"/library"}},[n._v("Библиотека")])]),t("li",[t("a",{attrs:{href:"/users"}},[n._v("Пользователи")])]),t("li",[t("a",{attrs:{href:"/about"}},[n._v("О сайте")])])])}],k={name:"MainMenu"},_=k,E=(t("d6e1"),Object(h["a"])(_,b,g,!1,null,"f51d71da",null)),v=E.exports,S=function(){var n=this,e=n.$createElement,t=n._self._c||e;return t("button",[n._v(" "+n._s(n.value)+" ")])},T=[],I={name:"ButtonWhite",props:{value:String}},O=I,N=(t("9cd4"),Object(h["a"])(O,S,T,!1,null,"4812cf26",null)),y=N.exports,R=t("bc3a"),j=t.n(R),w=t("2f62"),A={name:"Header",created:function(){this.loggedIn&&this.GET_USER_SETTINGS()},methods:Object(i["a"])({},Object(w["b"])(["GET_USER_SETTINGS"])),computed:Object(i["a"])({},Object(w["c"])(["CLIENT_USERNAME","USERID","loggedIn"])),components:{Finder:m,MainMenu:v,ButtonWhite:y}},D=A,M=(t("775b"),Object(h["a"])(D,c,u,!1,null,"64c037d4",null)),G=M.exports,x=function(){var n=this,e=n.$createElement;n._self._c;return n._m(0)},U=[function(){var n=this,e=n.$createElement,t=n._self._c||e;return t("footer",[t("span",[n._v("© Copyright 2020")])])}],C={name:"Footer"},P=C,L=(t("8d83"),Object(h["a"])(P,x,U,!1,null,"93fce448",null)),F=L.exports,$={components:{Header:G,Footer:F}},z=$,K=(t("034f"),Object(h["a"])(z,r,o,!1,null,null,null)),B=K.exports,H=(t("d3b7"),t("8c4f"));a["a"].use(H["a"]);var V=new H["a"]({mode:"history",routes:[{path:"/",component:function(){return t.e("chunk-b0dbdeaa").then(t.bind(null,"bb51"))}},{path:"/library",component:function(){return t.e("chunk-7e3fde65").then(t.bind(null,"55a5"))}},{path:"/users",component:function(){return t.e("chunk-75f186c3").then(t.bind(null,"ed81"))}},{path:"/about",component:function(){return t.e("chunk-2d22d746").then(t.bind(null,"f820"))}},{path:"/login",component:function(){return t.e("chunk-58a5cd18").then(t.bind(null,"a55b"))}},{path:"/logout",component:function(){return t.e("chunk-2d215fa4").then(t.bind(null,"c100"))}},{path:"/register",component:function(){return t.e("chunk-789b8aa0").then(t.bind(null,"73cf"))}},{path:"/book/:id",component:function(){return t.e("chunk-662bc62a").then(t.bind(null,"5e61"))}},{path:"/reading/:id",component:function(){return t.e("chunk-02c844c8").then(t.bind(null,"6367"))}},{path:"/translation/:id",component:function(){return t.e("chunk-7841f5b7").then(t.bind(null,"ffa5"))}},{path:"/editing/:id",component:function(){return t.e("chunk-da3e29d0").then(t.bind(null,"2f9a"))}},{path:"/translating/:id",component:function(){return t.e("chunk-748d435b").then(t.bind(null,"8469"))}},{path:"/user/:id",component:function(){return t.e("chunk-5f75d802").then(t.bind(null,"1511"))}},{path:"/user-settings",component:function(){return t.e("chunk-e74b1dd8").then(t.bind(null,"3a73"))}},{path:"/user-onhold",component:function(){return t.e("chunk-565adc48").then(t.bind(null,"2655"))}},{path:"/changes/:id",component:function(){return t.e("chunk-13e6c81e").then(t.bind(null,"a592"))}},{path:"/version/:id",component:function(){return t.e("chunk-9734388a").then(t.bind(null,"4026"))}}]}),W=t("53ca");a["a"].use(w["a"]);var Y=new w["a"].Store({state:{main_origins:[],origins:[],users:[],client_username:"",userID:"",token:localStorage.getItem("access_token")||null},actions:{GET_MAIN_ORIGINS:function(n){var e=n.commit;return j()("http://127.0.0.1:8000/project-api/library/main/",{method:"GET"}).then((function(n){e("SET_MAIN_ORIGINS",n.data.data)}))},GET_ORIGINS:function(n){var e=n.commit;return j()("http://127.0.0.1:8000/project-api/library/origin/all/?page_size=30",{method:"GET"}).then((function(n){e("SET_ORIGINS",n.data.data)}))},GET_USERS:function(n){var e=n.commit;return j()("http://127.0.0.1:8000/project-api/user/all/?page_size=30",{method:"GET"}).then((function(n){e("SET_USERS",n.data.data)}))},DESTROY_TOKEN:function(n){if(j.a.defaults.headers.common["Authorization"]="Token "+n.state.token,n.getters.loggedIn)return new Promise((function(e,t){j.a.post("http://127.0.0.1:8000/auth/token/logout/").then((function(t){localStorage.removeItem("access_token"),n.commit("DESTROY_TOKEN"),e(t)})).catch((function(e){localStorage.removeItem("access_token"),n.commit("DESTROY_TOKEN"),t(e)}))}))},RETRIEVE_TOKEN:function(n,e){return new Promise((function(t,a){var r=new FormData;r.append("email",e.email),r.append("password",e.password),j.a.post("http://127.0.0.1:8000/auth/token/login/",r).then((function(e){var a=e.data.data.attributes.auth_token;localStorage.setItem("access_token",a),n.commit("RETRIEVE_TOKEN",a),t(e)})).catch((function(n){a(n)}))}))},GET_USER_SETTINGS:function(n){return j.a.defaults.headers.common["Authorization"]="Token "+n.state.token,new Promise((function(e,t){j()("http://127.0.0.1:8000/project-api/user/main-info/").then((function(t){n.commit("SET_CLIENT_USERNAME",t.data.username),n.commit("SET_USERID",t.data.id),e(t)})).catch((function(n){t(n)}))}))},TRANSLATION_ADD:function(n,e){j.a.defaults.headers.common["Authorization"]="Token "+n.state.token;var t=new FormData;t.append("origin",e.origin),t.append("language",e.language),t.append("file",e.file,"file.txt"),j.a.post("http://127.0.0.1:8000/project-api/library/translation/add/",t).then((function(n){console.log(n)}))},ADD_VERSION:function(n,e){j.a.defaults.headers.common["Authorization"]="Token "+n.state.token;var t=new FormData;t.append("translation",e.translation),t.append("file",e.file,"file.txt"),j.a.put("http://127.0.0.1:8000/project-api/library/translation/add-version/",t).then((function(n){console.log(n)}))},DELETE_TRANSLATION:function(n,e){console.log(e.translation),console.log(Object(W["a"])(e.translation));var t=new FormData;t.append("translation",e.translation),j.a.delete("http://127.0.0.1:8000/project-api/library/translation/delete/",{headers:{Authorization:"Token "+n.state.token},data:t}).then((function(n){console.log(n)}))},COMMENT_POST:function(n,e){var t=new FormData;t.append("post",e.post),t.append("author",n.state.userID),t.append("origin",e.origin),j.a.post("http://127.0.0.1:8000/project-api/library/comment-origin/add/",t,{headers:{Authorization:"Token "+n.state.token}}).then((function(n){console.log(n)}))}},mutations:{SET_MAIN_ORIGINS:function(n,e){n.main_origins=e},SET_ORIGINS:function(n,e){n.origins=e},SET_USERS:function(n,e){n.users=e},SET_CLIENT_USERNAME:function(n,e){n.client_username=e},SET_USERID:function(n,e){n.userID=e},RETRIEVE_TOKEN:function(n,e){n.token=e},DESTROY_TOKEN:function(n){n.token=null}},getters:{MAIN_ORIGINS:function(n){return n.main_origins},ORIGINS:function(n){return n.origins},USERS:function(n){return n.users},CLIENT_USERNAME:function(n){return n.client_username},USERID:function(n){return n.userID},loggedIn:function(n){return null!==n.token}}}),q=Y,J=t("1dce"),Q=t.n(J);a["a"].use(Q.a),a["a"].config.productionTip=!1,new a["a"]({router:V,render:function(n){return n(B)},store:q}).$mount("#app")},"775b":function(n,e,t){"use strict";var a=t("feee"),r=t.n(a);r.a},"85ec":function(n,e,t){},"8d83":function(n,e,t){"use strict";var a=t("9d29"),r=t.n(a);r.a},"98fb":function(n,e,t){n.exports=t.p+"img/finder.d1fb2b62.svg"},"9cd4":function(n,e,t){"use strict";var a=t("ef2b"),r=t.n(a);r.a},"9d29":function(n,e,t){},a5f7:function(n,e,t){n.exports=t.p+"img/logo.5872e56a.svg"},aa47:function(n,e,t){"use strict";var a=t("2491"),r=t.n(a);r.a},c626:function(n,e,t){n.exports=t.p+"img/sign-in.a4a08999.svg"},cf20:function(n,e,t){},d6e1:function(n,e,t){"use strict";var a=t("cf20"),r=t.n(a);r.a},ef2b:function(n,e,t){},feee:function(n,e,t){}});
//# sourceMappingURL=app.aa3d4724.js.map