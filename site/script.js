function SignIn(e) {
    e.preventDefault();
    const role = document.getElementById('role').value;
    const tables = document.getElementById('data-tables');

    if (role === 'moderator') {
        tables.classList.remove('hidden');
    } else {
        tables.classList.add('hidden');
    }
}