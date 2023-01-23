$(function() {
    $(".btn").click(function() {
        $(".form-signin").toggleClass("form-signin-left");
        $(".form-signup").toggleClass("form-signup-left");
        $(".frame").toggleClass("frame-long");
        $(".signup-inactive").toggleClass("signup-active");
        $(".signin-active").toggleClass("signin-inactive");
        $(".forgot").toggleClass("forgot-left");
        $(this).removeClass("idle").addClass("active");
    });
});


$(document).ready(function() {
    $("#log").submit(function(event) {
        event.preventDefault();
    });
});

const Login = async () => {
    const form = document.getElementById('log')


    const data = {
        email: form.elements['email'].value,
        password: form.elements['password'].value
    }
   const response = await fetch(`/login`, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data)

    });
     if(response.redirected === true){
    window.location.href = response.url
    }
    const body = await response.json()

    console.log(body.reason)
    if (document.getElementById("log").contains(document.getElementById("res"))=== false) {
        const label = document.createElement("label");
        label.style.color = "black";
        label.setAttribute("id", "res") ;
        label.style.padding = "3px";
        label.innerText = "Invalid User/Password";
        form.appendChild(label)
    }

}
