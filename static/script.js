const btnsRemove = document.getElementsByClassName("btn-remove");
const loginBtn = document.getElementById("login-btn");
const registerBtn = document.getElementById("register-btn");
const detailsBtn = document.getElementsByClassName("details-btn");

loginBtn.addEventListener("click", loginRoute);
// registerBtn.addEventListener("click", registerRoute);

for (btn of detailsBtn) {
  btn.addEventListener("click", surfboardDetails);
}

for (btn of btnsRemove) {
  btn.addEventListener("click", removeEl);
}

function removeEl(e) {
  console.log("test");
  const btnClicked = e.target;
  const surfboardContainer = btnClicked.parentElement;
  surfboardContainer.remove();
}

function loginRoute() {
  window.location.href = "/login";
}

function addRoute() {
  window.location.href = "/add";
}

function registerRoute() {
  window.location.href = "/register";
}

function surfboardDetails(e) {
  const url = e.target.getAttribute("data-url");
  window.open(url, "_blank");
}
