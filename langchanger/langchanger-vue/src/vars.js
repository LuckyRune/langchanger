export const cors = 'https://langchangerproxy.herokuapp.com/'
export var host = ''
if(document.location.hostname == '127.0.0.1') host = 'http://127.0.0.1:8000/'
else host = 'https://' + document.location.hostname
// https://cors-anywhere.herokuapp.com/
// https://cors-proxy.htmldriven.com/?url=
// https://thingproxy.freeboard.io/fetch/
// http://www.whateverorigin.org/get?url=
// http://alloworigin.com/get?url=
// https://yacdn.org/serve/
// https://galvanize-cors-proxy.herokuapp.com/