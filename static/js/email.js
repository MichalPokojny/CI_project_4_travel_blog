// function to send email using emailJS
function sendMail(contactForm) {
    // call the emailJS send function with the appropriate parameters
    emailjs.send("gmail", "Michal", {
        // Extract form data and pass it as emailJS template parameters
        "email_enquiry" : contactForm.floatingSelect.value,
        "from_name": contactForm.firstname.value,
        "last_name": contactForm.lastname.value,
        "from_email": contactForm.floatingInput.value,
        "comment": contactForm.floatingTextarea.value,
    })
    .then(
        function(response) {
            // If the email is sent successfully, log a success mesage
            console.log("SUCCESS", response);
            alert(`Thank you ${contactForm.firstname.value}, your email has been sent!`);
            location.reload();
        },
        function(error) {
            // if there's error sending the email, log the err mesage
            console.log("FAILED", error);
            alert("Email hasn't been sent!");
        }
    );
    return false;  // To block from loading a new page 
}