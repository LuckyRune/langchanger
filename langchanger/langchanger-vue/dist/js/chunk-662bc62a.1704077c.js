(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-662bc62a"],{"122b":function(t,e,a){},"183a":function(t,e,a){},"1cad":function(t,e,a){"use strict";var n=a("adda"),i=a.n(n);i.a},3830:function(t,e,a){"use strict";var n=a("122b"),i=a.n(n);i.a},"5e61":function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("h3",{staticClass:"mb20"},[t._v(t._s(t.origin.title))]),a("div",{staticClass:"book-info mb20"},[a("div",{staticClass:"svg-placeholder mr20"},[a("img",{attrs:{src:t.origin.poster.image}})]),a("div",[a("h5",[t._v("Информация")]),a("p",[a("span",{staticClass:"book-prop"},[t._v("Формат: ")]),a("a",{attrs:{href:"#"}},[t._v(t._s(t.origin.format_type.name))])]),a("p",[a("span",{staticClass:"book-prop"},[t._v("Жанры: ")]),a("a",{staticClass:"genre",attrs:{href:"#"}},[t._v(t._s(t.origin.genre[0].name))])]),a("p",[a("span",{staticClass:"book-prop"},[t._v("Возрастной рейтинг: ")]),a("a",{attrs:{href:"#"}},[t._v(t._s(t.origin.age_limit)+"+")])]),a("p",[a("span",{staticClass:"book-prop"},[t._v("Автор: ")]),t._v(t._s(t.origin.author))]),a("router-link",{attrs:{to:/reading/+t.origin.id}},[a("ButtonBlack",{staticClass:"mt20",attrs:{value:"Читать оригинал"}})],1)],1)]),a("div",{staticClass:"book-desc mb40"},[a("h5",[t._v("Описание")]),""!=t.origin.description?a("p",[t._v(t._s(t.origin.description))]):a("p",[t._v("Без описания.")])]),a("div",{staticClass:"mb40 read"},[a("h5",[t._v("Переводы")]),t.translation_languages.length>0?a("div",{staticClass:"read-selectors"},[a("div",[a("p",[t._v("Язык")]),a("select",{directives:[{name:"model",rawName:"v-model",value:t.selected_language,expression:"selected_language"}],attrs:{id:"select-language"},on:{change:[function(e){var a=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){var e="_value"in t?t._value:t.value;return e}));t.selected_language=e.target.multiple?a:a[0]},t.selectLang]}},t._l(t.translation_languages,(function(e){return a("option",{key:e.id,domProps:{value:e.id}},[t._v(t._s(e.name))])})),0)]),""!==t.selected_language?a("div",[a("p",[t._v("Автор")]),a("select",{directives:[{name:"model",rawName:"v-model",value:t.selected_translation,expression:"selected_translation"}],attrs:{id:"select-translation"},on:{change:function(e){var a=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){var e="_value"in t?t._value:t.value;return e}));t.selected_translation=e.target.multiple?a:a[0]}}},t._l(t.authors,(function(e){return a("option",{key:e.id,domProps:{value:e.id}},[t._v(t._s(e.author.username))])})),0)]):t._e(),""!==t.selected_translation?a("router-link",{attrs:{to:/translation/+t.selected_translation}},[a("button",{staticClass:"btnBlack",attrs:{id:"translation-read"}},[t._v("Читать перевод")])]):t._e()],1):a("div",[a("p",[t._v("Пока нет переводов. Создать версию перевода можно на странице чтения оригинала.")])])]),a("div",[a("h5",[t._v("Комментарии")]),a("div",{staticClass:"mb20"},[!t.comments.length>0?a("p",[t._v("Пока нет комментариев.")]):t._e(),t._l(t.comments,(function(e){return a("div",{key:e.id,staticClass:"comment"},[t._m(0,!0),a("div",{staticClass:"comment-data"},[a("div",{staticClass:"comment-info"},[a("div",{staticClass:"comment-author"},[t._v(t._s(e.author.username))]),a("div",{staticClass:"comment-date"},[t._v(t._s(e.post_date.substr(0,10)))])]),a("div",{staticClass:"comment-text"},[t._v(t._s(e.post))])])])}))],2),a("textarea",{staticClass:"mb20",attrs:{id:"comment-form"}}),t._v(" "),a("button",{staticClass:"btnBlack",on:{click:t.postComment}},[t._v("Написать")])])])},i=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"comment-usericon"},[a("img",{attrs:{src:"/usericon.svg",alt:"fsdf"}})])}],s=a("5530"),o=a("c71c"),r=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("select",{directives:[{name:"model",rawName:"v-model",value:t.select,expression:"select"}],attrs:{id:t.id},on:{change:function(e){var a=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){var e="_value"in t?t._value:t.value;return e}));t.select=e.target.multiple?a:a[0]}}},t._l(t.options,(function(e){return a("option",{key:e.id,domProps:{value:e.id}},[t._v(t._s(e.name))])})),0)},c=[],l={name:"SelectList",data:function(){return{select:""}},props:{id:String,options:Array}},u=l,d=(a("3830"),a("2877")),m=Object(d["a"])(u,r,c,!1,null,"111d8965",null),v=m.exports,g=a("8ab6"),p=a("bc3a"),_=a.n(p),h=a("2f62"),f={name:"OriginPage",data:function(){return{id:this.$route.params.id,origin:[],translation_languages:[],selected_language:"",selected_translation:"",authors:[],comments:[]}},methods:{selectLang:function(){var t=this,e=document.getElementById("select-language").selectedIndex,a=document.getElementById("select-language").options[e].value;_()("http://127.0.0.1:8000/project-api/library/origin/translation/?origin="+this.origin.id+"&language="+a).then((function(e){t.authors=e.data.data}))},getComments:function(){var t=this;_()("http://127.0.0.1:8000/project-api/library/comment-origin/?origin="+this.id).then((function(e){console.log(e.data.data),t.comments=e.data.data}))},postComment:function(){var t=document.getElementById("comment-form").value;""!==t?(this.$store.dispatch("COMMENT_POST",{post:t,origin:this.id}),document.getElementById("comment-form").value="",setTimeout(this.getComments,500)):alert("Напишите что-нибудь!")}},created:function(){var t=this;_()("http://127.0.0.1:8000/project-api/library/origin/?origin="+this.id,{method:"GET"}).then((function(e){t.origin=e.data.data.origin,t.translation_languages=e.data.data.languages,document.title=e.data.data.origin.title+" - Langchanger"})),_()("http://127.0.0.1:8000/project-api/library/comment-origin/?origin="+this.id).then((function(e){console.log(e.data.data),t.comments=e.data.data}))},computed:Object(s["a"])({},Object(h["c"])(["USERID"])),components:{Book:o["a"],SelectList:v,ButtonBlack:g["a"]}},b=f,C=(a("c480"),Object(d["a"])(b,n,i,!1,null,"77cbaa5e",null));e["default"]=C.exports},"8ab6":function(t,e,a){"use strict";var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("button",[t._v(" "+t._s(t.value)+" ")])},i=[],s={name:"ButtonBlack",props:{value:String}},o=s,r=(a("da07"),a("2877")),c=Object(r["a"])(o,n,i,!1,null,"feaeb9f6",null);e["a"]=c.exports},adda:function(t,e,a){},c480:function(t,e,a){"use strict";var n=a("ff54"),i=a.n(n);i.a},c71c:function(t,e,a){"use strict";var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"svg-placeholder",style:{width:t.width+"px",height:t.height+"px"}},[a("img",{style:{width:t.width+"px",height:t.height+"px"},attrs:{src:t.poster}})])},i=[],s={name:"Book",props:{width:String,height:String,poster:String}},o=s,r=(a("1cad"),a("2877")),c=Object(r["a"])(o,n,i,!1,null,"6ae7992e",null);e["a"]=c.exports},da07:function(t,e,a){"use strict";var n=a("183a"),i=a.n(n);i.a},ff54:function(t,e,a){}}]);
//# sourceMappingURL=chunk-662bc62a.1704077c.js.map