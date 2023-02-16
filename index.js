async function getData(params) {
    const url = 'http://127.0.0.1:8000/predict?news='
    const response = await fetch(url + params);
    const data = await response.json();
    document.getElementById("response").innerHTML = data;
}

document.getElementById("from").addEventListener("submit", function (event) {
    event.preventDefault();
    console.log();
    getData(document.getElementById("txtbox").value)
})
