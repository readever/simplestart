// ----------------------------------------------------
// Just copy/paste these functions as-is:
// 获取 URL 参数
const urlParams = new URLSearchParams(window.location.search);

// 获取指定参数的值
const componentId = urlParams.get('componentId');

function init() {
    sendMessageToStreamlitClient("componentReady", {msg: "ready"});
}

function sendMessageToStreamlitClient(type, data) {
    var outData = Object.assign({
        componentId:componentId,
        isSSMessage: true,
        _type: type,
    }, data);
    window.parent.postMessage(outData, "*");
}

// The `data` argument can be any JSON-serializable value.
function sendDataToPython(data) {
    sendMessageToStreamlitClient("setComponentValue", data);
}

// Hook things up!
//window.addEventListener("message", onDataFromPython);
init();

function setFrameHeight(height) {
    sendMessageToStreamlitClient("setFrameHeight", {height: height});
}

// Hack to autoset the iframe height.
window.addEventListener("load", function() {
    window.setTimeout(function() {
        setFrameHeight(document.documentElement.clientHeight)
    }, 0);
});