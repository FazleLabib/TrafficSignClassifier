const uploadPanel = document.getElementById('upload-panel');
const fileInput = document.getElementById('file-input');
const clearButton = document.getElementById('clear-button');

// Handle file selection and drag & drop
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

// Function to handle file selection
function handleFileSelect() {
    const file = fileInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            // Create an image element for the preview
            const previewImage = document.createElement('img');
            previewImage.src = e.target.result;
            previewImage.className = 'preview-image';

            // Clear existing preview and add new one
            const uploadContent = uploadPanel.querySelector('.upload-content');
            if (uploadContent) {
                uploadContent.remove();
            }

            uploadPanel.appendChild(previewImage);
            // Hide the existing text and icon in the upload panel
        };
        reader.readAsDataURL(file);
    }
}

// Clear button functionality
clearButton.addEventListener('click', (e) => {
    // Show the existing text and icon in the upload panel again
    location.replace(location.href);
});
