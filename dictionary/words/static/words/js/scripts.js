// words/static/words/js/entries.js

document.addEventListener("DOMContentLoaded", function() {
    var translateButtons = document.querySelectorAll(".translate-button");
    translateButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            var translation = button.nextElementSibling; // Get the next sibling (translation element)
            translation.classList.toggle("show-translation");
            button.style.display = "none"; // Hide the "Translate" button
        });
    });
});
