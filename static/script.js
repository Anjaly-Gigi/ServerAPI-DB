document.getElementById("loginForm").addEventListener("submit", async function(e) {
  e.preventDefault();

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const res = await fetch("/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });

  const data = await res.json();

  if (data.status === "success") {
    localStorage.setItem("username", data.user.username);
    window.location.href = "/home";
  } else {
    document.getElementById("message").textContent = data.message;
  }
});
