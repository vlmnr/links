//var clipboard = new ClipboardJS('#copyButton');

function getInitial() {
  const initialUrl = document.getElementById("initial-link").value;
  return initialUrl;
}

function putShort(shortUrl) {
  var shortUrlField = document.getElementById('short-link');
   shortUrlField.value = shortUrl;
}

//--------------------FetchPost------------------
function sendInitial(){
  initialUrl = getInitial();
  fetch('http://localhost:5000/get_short_url',
    {
      mode: 'cors',
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({'initial_url': initialUrl} )
    }
  )
    .then((response) => response.text())
    .then((text) => { 
      putShort(text)
    })
    .catch(err => console.log(err));
}

  //-------------------GET_Clear-----------------
function clearFu(){
  console.log('clear')
    fetch('http://localhost:5000/clear', {mode: 'cors'})
    .then((response) => response.text())
    .then((text)=> {
    })
}
  
function СopyShortUrl(){
  var outputElement  = document.getElementById('short-link');
  var range = document.createRange();

  range.selectNode(outputElement);
  window.getSelection().removeAllRanges();
  window.getSelection().addRange(range);

  document.execCommand('copy');

  window.getSelection().removeAllRanges();
}

function doQR(){
  //document.getElementById("qrcode-script").onload = function(){
    var qrcodeElement = document.getElementById("qrcode");
    qrcodeElement.innerHTML = '';
    if (typeof QRCode !== 'undefined') {
      console.log('Yes');
      new QRCode(qrcodeElement, {
        text: document.getElementById("short-link").value, width: 100, height: 100});
    }
}