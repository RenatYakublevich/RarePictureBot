img_list = ['glitch_2020-5-13_13-3-27.gif','../img/glitch_2020-5-13_13-3-12.jpg','glitch_2020-5-13_13-3-52.gif','glitch_2020-5-13_13-4-3.jpg','glitch_2020-5-13_13-4-14.gif','glitch_2020-5-13_13-4-26.gif']
if (window.performance) {
console.log("Perfomance not supported");
}
if (performance.navigation.type == 1) {
  document.getElementById("head").src="glitch_2020-5-13_13-3-12.jpg";

}
