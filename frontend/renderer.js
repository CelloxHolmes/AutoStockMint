function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const openBtn = document.getElementById('openSidebarBtn');
    sidebar.classList.toggle('hidden');
    openBtn.classList.toggle('hidden');
}

function toggleDropdown() {
    const dropdown = document.getElementById('dropdown');
    dropdown.classList.toggle('hidden');
}

function goToPage(page) {
    document.getElementById('mainPage').classList.add('hidden');
    document.getElementById('midjourneyPage').classList.add('hidden');

    if (page === 'main') {
        document.getElementById('mainPage').classList.remove('hidden');
    } else if (page === 'midjourney') {
        document.getElementById('midjourneyPage').classList.remove('hidden');
    }

    document.getElementById('dropdown').classList.add('hidden');
}

async function callAPI(path) {
    const res = await fetch("http://localhost:5000" + path, { method: "POST" });
    const json = await res.json();
    document.getElementById("result").innerText = json.message;
}
