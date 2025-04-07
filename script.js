function validateForm() {
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();
    const error = document.getElementById('error');

    if (!name || !email || !message) {
        error.textContent = "Please fill out all fields.";
        return false;
    }

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        error.textContent = "Please enter a valid email address.";
        return false;
    }

    error.textContent = ""; // Clear any previous errors
    return true;
}
