
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
      doQR(text)
    })
    .catch(err => console.log(err));
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

function doQR(short_l){
    console.log("Start")
    var qrcodeElement = document.getElementById("qrcode");
    qrcodeElement.innerHTML = '';
    if (typeof QRCode !== 'undefined') {
      new QRCode(qrcodeElement, {
        text: short_l, width: 100, height: 100});
    }
}

// document.getElementById("short-link").value