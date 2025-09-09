
/*
Copyright by
| Alvin Sengkey
| 001202000115
| President University
| Faculty of Computing
| Major of Informatics
| MAY 2023
*/


// Initialize SpeechSynthesisUtterance object
let speech = new SpeechSynthesisUtterance();


// Set Speech Language
speech.lang = "id";



// List of Available Voices
// | The available voices may vary on different devices and browsers 
// | ^^ EXPLAIN ON THE REPORT ^^

let voices = [];
voices = window.speechSynthesis.getVoices();

speech.voice = voices[3];

// | vv EXPLAIN ON THE REPORT vv
// | voices[3] is "Microsoft Andika - Indonesian" on my device.
// speech.voice = voices[20]; // voices[20] is "Google Bahasa Indonesia" in Chrome Browser.



function start() {
  speech.rate = 1;
  speech.volume = 1;
  speech.pitch = 1;
  speech.text = document.getElementById("complete-trans").innerHTML;

  // Start Speaking
  window.speechSynthesis.speak(speech);
};

function isLetter(char) {
  return (/[a-zA-Z ]/).test(char);
};

function displayImage(src) {
  var img = document.createElement("img");
  img.src = src;
  img.width = 100;
  img.height = 100;
  document.getElementById("img-place").appendChild(img);
};

function toImages() {
  const imgList = document.getElementById("img-place");
  while (imgList.hasChildNodes()) {
    imgList.removeChild(imgList.firstChild);
  }
  let rawText = document.getElementById("input").innerText;
  let text = rawText.toLowerCase();
  let root = "static/img/";
  for (let char in text) {
    if (isLetter(text[char])) {
      if (text[char] === " " || text[char] == "\n") {
        path = root + "space" + ".jpg";
      } else {
        path = root + text[char] + ".jpg";
      }
      displayImage(path);
    }
  }
};

function resetImg() {
  const imgList = document.getElementById("img-place");
  while (imgList.hasChildNodes()) {
    imgList.removeChild(imgList.firstChild);
  }
}