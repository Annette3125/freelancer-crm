document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("client-search");
    const rows = document.querySelectorAll("table tr"); // first header

    if (!searchInput || rows.length === 0) return;

    searchInput.addEventListener("input", function () {
        const query = searchInput.value.toLowerCase().trim();

        rows.forEach((row, index) => {
            if (index === 0) return; // let go trough header

            const text = row.textContent.toLowerCase();

            if (!query || text.includes(query)) {
                row.style.display = "";
            } else {
                row.style.display = "none";
            }
        });
    });
});