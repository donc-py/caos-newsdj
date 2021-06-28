function loadDestination() {
  fetch("../destinations/getall", {
    method: "POST",
  })
    .then(function (response) {
      return response.text();
    })
    .then(function (data) {
      console.log(data);
      sessionStorage.setItem("destinations", data);
    })
    .catch(function (err) {
      console.error(err);
    });
}

function find() {

const trip = document.querySelector('#ida_vuelta')
const departureDate = document.querySelector('#fecha_ida')
const returnDate = document.querySelector('#fecha_vuelta')
const from = document.querySelector('#inputFromV')
const to = document.querySelector('#inputToV')
const adult = document.querySelector('#inputAdult')
const child = document.querySelector('#inputChild')

let __passengers = adult.value + child.value

let __trip = trip.checked?1:0

const findAll = __trip+'/'+from.value+'/'+to.value+'/'+__passengers+'/'+child.value+'/'+adult.value+'/'+departureDate.value+'/'+returnDate.value

location.href='destinations/search/'+findAll


}
