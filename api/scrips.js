const signInBtn = document.getElementById("signIn");
const signUpBtn = document.getElementById("signUp");
const signInForm = document.getElementById("form1");
const sendSignUp = document.getElementById("sendSignUp");
const signUpForm = document.getElementById("form2");
const Password = document.getElementById("password");
const CPassword = document.getElementById("C-password");
const container = document.querySelector(".container");
const hostname = window.location.origin
signInBtn.addEventListener("click", () => {
	container.classList.remove("right-panel-active");
});

signUpBtn.addEventListener("click", () => {
	container.classList.add("right-panel-active");
});

signInForm.addEventListener("submit", (e) => e.preventDefault());
sendSignUp.addEventListener('click', (e) => {
	e.preventDefault()
    if((Password.value === CPassword.value) && (Password.value !== '' && CPassword.value !== '')){
        signupData()
        return true;
    }
    else{
        alert("Please check if :\n\n1. You fill out all the fields\n2. Password isn't empty!\n3. Password are the Same!");
        return false;
        }
    })


function signupData(){
    const data = {
        name: document.getElementById("Username").value,
        email: document.getElementById("Email").value,
        password: document.getElementById("C-password").value,
    }
     fetch(`${hostname}/signUp`, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    }).then(res =>{
        console.log(res)
    })
}