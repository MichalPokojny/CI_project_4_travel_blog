function sendMail(contactForm) {
    emailjs.send("gmail", "Michal", {

        "email_enquiry" : contactForm.floatingSelect.value,
        "from_name": contactForm.firstname.value,
        "last_name": contactForm.lastname.value,
        "from_email": contactForm.floatingInput.value,
        "comment": contactForm.floatingTextarea.value,
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            alert(`Thank you ${contactForm.firstname.value}, your email has been sent!`);
            location.reload();
        },
        function(error) {
            console.log("FAILED", error);
            alert("Email hasn't been sent!");
        }
    );
    return false;  // To block from loading a new page
    
}