document.addEventListener('DOMContentLoaded', function () {
    const languageSelect = document.getElementById('language-select');
    const searchInput = document.getElementById('search-input');
    const searchButton = document.getElementById('search-button');
  
    function animatePlaceholderChange(newPlaceholder) {
      let i = searchInput.placeholder.length;
  
      function frame() {
        if (i >= 0) {
          searchInput.placeholder = searchInput.placeholder.substring(0, i);
          i--;
        } else if (-i <= newPlaceholder.length) {
          searchInput.placeholder = newPlaceholder.substring(0, -i);
          i--;
        } else {
          searchInput.placeholder = newPlaceholder;
          clearInterval(interval);
        }
      }
  
      let interval = setInterval(frame, 50);
    }
  
    searchButton.addEventListener('click', function () {
      const selectedLanguage = languageSelect.value;
      const placeholderText = languageSelect.querySelector(`option[value=${selectedLanguage}]`).getAttribute(`data-placeholder-${selectedLanguage}`);
      const buttonText = languageSelect.querySelector(`option[value=${selectedLanguage}]`).getAttribute(`data-button-text-${selectedLanguage}`);
  
      if (placeholderText) {
        animatePlaceholderChange(placeholderText);
      }
  
      if (buttonText) {
        searchButton.innerText = buttonText;
      }
    });
  });
  