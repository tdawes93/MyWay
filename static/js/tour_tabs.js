document.getElementById("defaultOpen").click();

function openTab(evt, tabName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}

function openYear(evt, yearName) {
  var i, yearcontent, yearlinks;
  yearcontent = document.getElementsByClassName("yearcontent");
  for (i = 0; i < yearcontent.length; i++) {
    yearcontent[i].style.display = "none";
  }
  yearlinks = document.getElementsByClassName("yearlinks");
  for (i = 0; i < yearlinks.length; i++) {
    yearlinks[i].className = yearlinks[i].className.replace(" active", "");
  }
  document.getElementById(yearName).style.display = "block";
  evt.currentTarget.className += " active";
}

function openMonth(evt, monthName) {
  var i, monthcontent, monthlinks;
  monthcontent = document.getElementsByClassName("monthcontent");
  for (i = 0; i < monthcontent.length; i++) {
    monthcontent[i].style.display = "none";
  }
  monthlinks = document.getElementsByClassName("monthlinks");
  for (i = 0; i < monthlinks.length; i++) {
    monthlinks[i].className = monthlinks[i].className.replace(" active", "");
  }
  document.getElementById(monthName).style.display = "block";
  evt.currentTarget.className += " active";
}