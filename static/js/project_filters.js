// Live search for projects table (filters rows by title or client name)
document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.querySelector("#project-search");
    const table = document.querySelector("table");
    if (!searchInput || !table) return;

    const rows = Array.from(table.querySelectorAll("tbody tr, tr")).filter(
        (row) => row.querySelectorAll("td").length > 0
    );

    searchInput.addEventListener("input", function () {
        const query = searchInput.value.trim().toLowerCase();

        rows.forEach((row) => {
            const titleCell = row.querySelector("td:nth-child(1)");
            const clientCell = row.querySelector("td:nth-child(2)");

            if (!titleCell || !clientCell) {
                return;
            }

            const text =
                (titleCell.textContent || "").toLowerCase() +
                " " +
                (clientCell.textContent || "").toLowerCase();

            if (!query) {
                row.style.display = "";
            } else if (text.includes(query)) {
                row.style.display = "";
            } else {
                row.style.display = "none";
            }
        });
    });
});
