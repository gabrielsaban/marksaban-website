document.addEventListener('DOMContentLoaded', function() {
    const headers = document.querySelectorAll('.article-header');
    
    headers.forEach(header => {
        header.addEventListener('click', function() {
            // Toggle active class on the header
            const wasActive = this.classList.contains('active');
            
            // First close all sections
            headers.forEach(h => {
                h.classList.remove('active');
                h.nextElementSibling.style.display = 'none';
            });
            
            // If this wasn't the active one before, open it
            if (!wasActive) {
                this.classList.add('active');
                this.nextElementSibling.style.display = 'block';
            }
        });
    });
}); 