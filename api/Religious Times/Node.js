const API = "https://abolfazlzarei.sbs/ReligiousTimes.php/oghat?q=Mashhad";

fetch(API)
  .then(res => res.json())
  .then(data => {
    console.log(data.data.prayer_times.out.Fajr);
  })
  .catch(err => console.error(err));
