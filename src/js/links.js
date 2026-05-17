document.addEventListener('DOMContentLoaded', function() {
    const headers = document.querySelectorAll('.article-header');

    function setSectionState(header, isOpen) {
        const content = header.nextElementSibling;

        header.classList.toggle('active', isOpen);
        header.setAttribute('aria-expanded', String(isOpen));
        content.hidden = !isOpen;
        content.classList.toggle('is-open', isOpen);
    }

    function closeAll() {
        headers.forEach(header => setSectionState(header, false));
    }

    function openSection(header) {
        closeAll();
        setSectionState(header, true);
    }

    function openHashSection() {
        if (!window.location.hash) {
            return;
        }

        const target = document.querySelector(window.location.hash);
        if (!target || !target.classList.contains('article-header')) {
            return;
        }

        openSection(target);
        target.scrollIntoView({ block: 'start' });
    }

    headers.forEach((header, index) => {
        const content = header.nextElementSibling;
        const contentId = content.id || `article-content-${index + 1}`;

        content.id = contentId;
        header.setAttribute('aria-controls', contentId);
        setSectionState(header, false);

        header.addEventListener('click', function() {
            if (this.classList.contains('active')) {
                setSectionState(this, false);
            } else {
                openSection(this);
            }
        });
    });

    openHashSection();
    window.addEventListener('hashchange', openHashSection);
});
