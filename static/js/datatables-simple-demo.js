
const dataTable = new simpleDatatables.DataTable("#nextCart")
// const convertedData = simpleDatatables.convertJSON(   )


window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        // const dataTableTest = new DataTable("#datatableSimple");
        new simpleDatatables.DataTable(datatablesSimple);
    }
});

