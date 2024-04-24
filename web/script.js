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
  console.log(QRCode);
  if (typeof !QRCode) {
      console.log('not done');
      new QRCode(document.getElementById("qrcode"), "https://www.artofliving.ru");
  } else {
      // Скрипт еще не загружен, ждем его загрузки
      document.getElementById("qrcode-script").onload = function() {
          console.log('done');
          new QRCode(document.getElementById("qrcode"), "https://www.artofliving.ru");
      };
    
  }
}