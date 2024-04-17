function get_initial() {
  const message = document.getElementById("initial-link").value;
  return message;
}

function put_short(message) {
  var sh = document.getElementById('short-link');
   sh.value = message;
}

//--------------------FetchPost------------------
function send_initial(){
  initial_url = get_initial();
  fetch('http://localhost:5000/get_short_url',
    {
      mode: 'cors',
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({'initial_url': initial_url} )
    }
  )
    .then((response) => response.text())
    .then((text) => { 
      put_short(text)
    })
    .catch(err => console.log(err));
}

  //-------------------GET_Clear-----------------
function clear_fu(){
  console.log('clear')
    fetch('http://localhost:5000/clear', {mode: 'cors'})
    .then((response) => response.text())
    .then((text)=> {
    })
}
  