// theme/static/js/app.js

document.addEventListener('DOMContentLoaded', () => {
    const themeToggleButton = document.getElementById('theme-toggle-btn');
    const html = document.documentElement;
    const storageKey = 'theme-preference';

    // Function to apply theme
    const applyTheme = (theme) => {
        html.className = 'theme-' + theme;
        updateThemeIcon(theme);
    };

    // Update theme icon
    const updateThemeIcon = (theme) => {
        const icon = themeToggleButton.querySelector('.material-symbols-outlined');
        icon.textContent = theme === 'dark' ? 'dark_mode' : 'light_mode';
    };

    // Get current theme
    const getCurrentTheme = () => {
        return html.classList.contains('theme-dark') ? 'dark' : 'light';
    };

    // Set initial icon
    updateThemeIcon(getCurrentTheme());

    // Toggle theme on button click
    themeToggleButton.addEventListener('click', () => {
        const currentTheme = getCurrentTheme();
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        applyTheme(newTheme);
        localStorage.setItem(storageKey, newTheme);
    });

    // Listen for system theme changes (only if user hasn't set a preference)
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        const savedTheme = localStorage.getItem(storageKey);
        if (!savedTheme) {
            // Only update if user hasn't manually set a preference
            const newTheme = e.matches ? 'dark' : 'light';
            applyTheme(newTheme);
        }
    });
});
