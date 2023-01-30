let hidden = document.getElementById("hiddenmenu");

document.getElementById("clickvisible").addEventListener("click", () => {
  if (hidden.className === "hidden-menu") {
    hidden.classList.add("visible");
  } else {
    hidden.classList.remove("visible");
  }
});
