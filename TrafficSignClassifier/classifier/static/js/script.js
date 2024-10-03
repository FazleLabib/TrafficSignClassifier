const uploadPanel = document.getElementById('upload-panel');
const fileInput = document.getElementById('file-input');
const clearButton = document.getElementById('clear-button');

document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById("theme-toggle");
    const darkModeIcon = document.getElementById("dark-mode-icon");
    const lightModeIcon = document.getElementById("light-mode-icon");
  
    if (localStorage.getItem('theme') === 'dark') {
      document.body.classList.add('dark-mode');
      toggle.checked = true;
      darkModeIcon.style.display = "block";
      lightModeIcon.style.display = "none";
    }
  
    toggle.addEventListener("change", function () {
      if (this.checked) {
        document.body.classList.add("dark-mode");
        darkModeIcon.style.display = "block";
        lightModeIcon.style.display = "none";
        localStorage.setItem('theme', 'dark');
      } else {
        document.body.classList.remove("dark-mode");
        darkModeIcon.style.display = "none";
        lightModeIcon.style.display = "block";
        localStorage.setItem('theme', 'light');
      }
    });
  });  

fileInput.addEventListener('change', handleFileSelect);
uploadPanel.addEventListener('dragover', (e) => {
    e.preventDefault();
});
uploadPanel.addEventListener('drop', (e) => {
    e.preventDefault();
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        fileInput.files = files;
        handleFileSelect();
    }
});


function handleFileSelect() {
    const file = fileInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {

            const previewImage = document.createElement('img');
            previewImage.src = e.target.result;
            previewImage.className = 'preview-image';

            const uploadContent = uploadPanel.querySelector('.upload-content');
            if (uploadContent) {
                uploadContent.remove();
            }

            uploadPanel.appendChild(previewImage);
        };
        reader.readAsDataURL(file);
    }
}

clearButton.addEventListener('click', (e) => {
    location.replace(location.href);
});
