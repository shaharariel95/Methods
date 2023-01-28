/*!
    * Start Bootstrap - SB Admin v7.0.5 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2022 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
    // 
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});



const addList = async () => {

    const button = document.getElementById('addButton');
    const success = document.getElementById('success')
    const response = await fetch(`/newCart`, {
        method: 'PUT',

    });
    console.log("38")
    // const body = await response.json()
    console.log(response)
    if (response.status === 200){
        console.log("hello world")
        button.style.visibility = 'hidden';
        success.style.visibility = 'visible';
    }



    // return body;
}


// $(document).ready(function (){
//     $("nextCart").DataTable({
//         ajax: '/predict',
//         columns : [
//             {data: 'product name'},
//             {data: 'amount'}
//         ]
//     })
// })