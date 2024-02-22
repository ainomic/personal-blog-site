function confirmDelete(itemId) {
    if (confirm("Are you sure you want to delete this item?")) {
        document.getElementById("deleteLink").setAttribute("href", "/blogs/delete/" + itemId);
    } else {
        // Do nothing
    }
}