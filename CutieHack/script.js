const yearSelect = document.getElementById("year");
const monthSelect = document.getElementById("month");
const daySelect = document.getElementById("day");
console.log('');
// const months
function horoscope() {
    let input1 = document.getElementById("user-input-1").value;
    let input2 = document.getElementById("user-input-2").value;
    console.log('fasdfasf');
    fetch("https://a08a-2600-8801-2819-1d00-899d-e84c-3cc3-c77e.ngrok.io/horoscope?m="+input1+"&d="+input2, {
  "method": "GET",
  "headers": {}
})
.then(response => {
  return response.text();
}) .then(response => {
// alert(response)
document.getElementById("display").innerHTML=`<b>${response}</b>`
})
.catch(err => {
  console.error(err);
});
fetch("https://a08a-2600-8801-2819-1d00-899d-e84c-3cc3-c77e.ngrok.io/playlist?m="+input1+"&d="+input2, {
    "method": "GET",
    "headers": {}
  })
  .then(response => {
    return response.text();
  }) .then(response => {
  // alert(response)
  document.getElementById("display2").innerHTML=`<b>${response}</b>`
  document.getElementById("myiframe").src=response;
  })
  .catch(err => {
    console.error(err);
  });
  // document.getElementById('myiframe').setAttribute("src",response);
}
