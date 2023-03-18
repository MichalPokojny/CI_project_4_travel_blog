function sendMail(contactForm) {
    emailjs.send("gmail", "Michal", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "email_enquiry": contactForm.infoenquiry.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            alert(`Thank you ${contactForm.name.value}, your email has been sent!`);
            location.reload()
        },
        function(error) {
            console.log("FAILED", error);
            alert("Email hasn't been sent!");
        }
    );
    return false;  // To block from loading a new page
    
}