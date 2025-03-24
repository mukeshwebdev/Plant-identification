<?php
if(isset($_POST['submit'])) {
    // Get form data
    $name = $_POST['name'];
    $email = $_POST['email'];
    $message = $_POST['message'];
    
    // Email configuration
    $to = 'your-email@example.com'; // Change this to your email address
    $subject = 'New Contact Form Submission';
    $body = "Name: $name\nEmail: $email\nMessage:\n$message";
    $headers = "From: $email";
    
    // Send email
    if(mail($to, $subject, $body, $headers)) {
        // If mail sent successfully
        echo '<script>alert("Thank you for your message. We will contact you soon.");</script>';
    } else {
        // If an error occurred
        echo '<script>alert("Sorry, there was an error sending your message. Please try again later.");</script>';
    }
}
?>
