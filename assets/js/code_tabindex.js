// adds tabindex = 0 to code elements inside pre elements to make them keyboard accessible
document.addEventListener('DOMContentLoaded', (event) => {
    // Select all code elements inside pre tags
    const codeBlock = document.querySelectorAll('pre code');

    // Add tabindex="0" to each selected element
    codeBlock.forEach(element => {
        element.setAttribute('tabindex', '0');
    });
});
