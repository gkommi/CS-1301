document.addEventListener('DOMContentLoaded', postData);

const data = document.location.search;
const params = new URLSearchParams(data);

const name = params.get('fname');
const chips = params.get('chips');
const players = params.getAll('players');
const mvp = params.get('mvp');
const rookies = params.get('rookies');
const allstars = params.get('allstars');


let score;
let image;
if (rookies == "KAT") {
    score = "Elite";
    image = 'images/star.jpg';
    para = "The FitnessGram PACER Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The test is used to measure a student's aerobic capacity as part of the FitnessGram assessment. Students run back and forth as many times as they can, each lap signaled by a beep sound. The test get progressively faster as it continues until the student reaches their max lap score."
} else if (rookies == "KAT" && mvp == "Lebron") {
    score = "Superb";
    image = 'images/surprised.jpg';
    para = "The FitnessGram PACER Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The test is used to measure a student's aerobic capacity as part of the FitnessGram assessment. Students run back and forth as many times as they can, each lap signaled by a beep sound. The test get progressively faster as it continues until the student reaches their max lap score."
} else if (rookies == "Brogdon" && mvp == "Curry") {
    score = "Okay";
    image = 'images/smile.jpg';
    para = "The FitnessGram PACER Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The test is used to measure a student's aerobic capacity as part of the FitnessGram assessment. Students run back and forth as many times as they can, each lap signaled by a beep sound. The test get progressively faster as it continues until the student reaches their max lap score."
} else {
    score = "Meh";
    image = 'images/meh.jpg';
    para = "The FitnessGram PACER Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The test is used to measure a student's aerobic capacity as part of the FitnessGram assessment. Students run back and forth as many times as they can, each lap signaled by a beep sound. The test get progressively faster as it continues until the student reaches their max lap score."
}
console.log(mvp)
//writing html code
function postData() {
    const container = document.getElementById("results");
    container.innerHTML = `<h1>${score}!</h1>
                            <img src="${image}"></img>
                            <p>${para}</p>`
}
