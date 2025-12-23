document.addEventListener("DOMContentLoaded", function () {
    const statusSelect = document.getElementById("status-filter");
    if (statusSelect && statusSelect.form) {
        statusSelect.addEventListener("change", function () {
            statusSelect.form.submit();
        });
    }
});