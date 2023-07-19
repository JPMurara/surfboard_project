const allButtons = document.getElementsByClassName("btn-remove");

if (allButtons) {
  for (const btn of allButtons) {
    btn.addEventListener("click", removeEl);
  }
}

function removeEl(e) {
  const btnClicked = e.target;
  const surfboardContainer = btnClicked.parentElement;
  surfboardContainer.remove();
}

const loginBtn = document.getElementById("login-btn");
loginBtn.addEventListener("click", loginRoute);

function loginRoute() {
  window.location.href = "/login";
}

function addRoute() {
  window.location.href = "/add";
}
