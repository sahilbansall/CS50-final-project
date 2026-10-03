document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("searchInput");

    if (!searchInput) {
        return;
    }

    searchInput.addEventListener("input", function () {
        const searchText = searchInput.value.toLowerCase().trim();
        const rows = document.querySelectorAll("#expenseTable tbody tr");

        rows.forEach(function (row) {
            const text = row.innerText.toLowerCase();

            if (text.includes(searchText)) {
                row.style.display = "";
            } else {
                row.style.display = "none";
            }
        });
    });
});