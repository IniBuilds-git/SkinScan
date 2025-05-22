
document.addEventListener('DOMContentLoaded', function() {
    initializeImageUpload();
    initializeAnimations();
    initializeProgressBars();
    initializeTooltips();
    initializeSmoothScrolling();
    initializeFormValidation();
});

/**
 * This enhanced image upload handling with visual feedback
 * Provides drag & drop, preview, and validation
 */
function initializeImageUpload() {
    const photoInput = document.getElementById('photo');
    const uploadArea = document.getElementById('upload-area');
    const imagePreviewContainer = document.getElementById('image-preview-container');
    const imagePreview = document.getElementById('image-preview');
    const selectedFile = document.getElementById('selected-file');
    
    if (!photoInput || !uploadArea) return;
    
    uploadArea.addEventListener('click', function(e) {
        if (!e.target.closest('.btn')) {
            photoInput.click();
        }
    });
    
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, preventDefaults, false);
    });
    
    ['dragenter', 'dragover'].forEach(eventName => {
        uploadArea.addEventListener(eventName, function() {
            uploadArea.classList.add('drag-active');
            uploadArea.classList.add('border-primary');
        }, false);
    });
    
    // Remove highlight when drag ends
    ['dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, function() {
            uploadArea.classList.remove('drag-active');
            uploadArea.classList.remove('border-primary');
        }, false);
    });
    
    // Handle dropped files
    uploadArea.addEventListener('drop', function(e) {
        const dt = e.dataTransfer;
        const files = dt.files;
        
        if (files.length) {
            handleFileSelection(files);
        }
    }, false);
    
    // Handle selected files from input
    photoInput.addEventListener('change', function() {
        if (this.files.length) {
            handleFileSelection(this.files);
        }
    });
    
    function handleFileSelection(files) {
        const file = files[0];
        
        // Check file type
        const validTypes = ['image/jpeg', 'image/jpg', 'image/png'];
        if (!validTypes.includes(file.type)) {
            showAlert('Please select a valid image file (JPG, JPEG, or PNG).', 'warning');
            return;
        }
        
        // Check file size (max 5MB)
        const maxSize = 5 * 1024 * 1024; // 5MB
        if (file.size > maxSize) {
            showAlert('Image file is too large. Please select an image under 5MB.', 'warning');
            return;
        }
        
        // Update file name display
        if (selectedFile) {
            selectedFile.textContent = file.name;
            selectedFile.classList.add('fade-in');
        }
        
        // Create and display image preview
        const reader = new FileReader();
        reader.onload = function(e) {
            imagePreview.src = e.target.result;
            imagePreviewContainer.style.display = 'block';
            
            // Add animations
            imagePreviewContainer.classList.add('fade-in');
            
            // Add success indication
            uploadArea.classList.add('upload-success');
            setTimeout(() => {
                uploadArea.classList.remove('upload-success');
            }, 1500);
        };
        reader.readAsDataURL(file);
        
        // Show submit button animation
        const submitBtn = document.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.classList.add('pulse-animation');
        }
    }
    
    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }
}

/**
 * This initialize staggered animations for page elements
 * Creates a more engaging user experience
 */
function initializeAnimations() {
    // Animate cards with staggered delay
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 100 + (index * 100));
    });
    
    // Animate diagnosis results if on diagnosis page
    const diagnosisResults = document.querySelector('.diagnosis-result');
    if (diagnosisResults) {
        animateDiagnosisResults();
    }
}

/**
 * Special animations for the diagnosis results page
 * Creates a more professional presentation of results
 */
function animateDiagnosisResults() {
    // Animate diagnosis badge
    const diagnosisBadge = document.querySelector('.diagnosis-badge');
    if (diagnosisBadge) {
        diagnosisBadge.classList.add('slide-in');
    }
    
    // Animate recommendation items with delay
    const recommendations = document.querySelectorAll('.recommendations li');
    recommendations.forEach((item, index) => {
        item.style.opacity = '0';
        item.style.transform = 'translateX(-10px)';
        
        setTimeout(() => {
            item.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
            item.style.opacity = '1';
            item.style.transform = 'translateX(0)';
        }, 300 + (index * 150));
    });
}

/**
 * Animate progress bars on page load
 * Creates a more dynamic visualization of confidence levels
 */
function initializeProgressBars() {
    const progressBars = document.querySelectorAll('.progress-bar');
    
    if (progressBars.length > 0) {
        // First set width to 0
        progressBars.forEach(bar => {
            const targetWidth = bar.style.width;
            bar.style.width = '0%';
            
            // Then animate to actual width
            setTimeout(() => {
                bar.style.width = targetWidth;
            }, 300);
        });
    }
}

/**
 * Initialize Bootstrap tooltips with enhanced styling
 */
function initializeTooltips() {
    // Check if Bootstrap tooltip is available
    if (typeof bootstrap !== 'undefined' && typeof bootstrap.Tooltip !== 'undefined') {
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function(tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl, {
                boundary: document.body,
                animation: true
            });
        });
    }
}

/**
 * Initialize smooth scrolling for internal links
 */
function initializeSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                
                window.scrollTo({
                    top: targetElement.offsetTop - 70, 
                    behavior: 'smooth'
                });
                
                history.pushState(null, null, targetId);
            }
        });
    });
}

/**
 * Enhanced form validation with visual feedback
 */
function initializeFormValidation() {
    const forms = document.querySelectorAll('.needs-validation');
    
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
                showAlert('Please check the form and try again.', 'warning');
            }
            
            form.classList.add('was-validated');
            
        
            const fileInput = form.querySelector('input[type="file"]');
            if (fileInput && fileInput.files.length === 0) {
                event.preventDefault();
                showAlert('Please select an image to upload.', 'warning');
            }
        }, false);
    });
}

/**
 * Display an alert message with animation and auto-dismiss
 * @param {string} message - The message to display
 * @param {string} type - Alert type (success, danger, warning, info)
 */
function showAlert(message, type = 'info') {
    const alertsContainer = document.querySelector('.container');
    if (!alertsContainer) return;
    
    // Create alert element
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed top-0 start-50 translate-middle-x mt-4`;
    alertDiv.style.zIndex = '1050';
    alertDiv.style.maxWidth = '90%';
    alertDiv.style.width = '500px';
    alertDiv.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.15)';
    
    // Add icon based on type
    let icon = 'info-circle';
    if (type === 'success') icon = 'check-circle';
    if (type === 'warning') icon = 'exclamation-triangle';
    if (type === 'danger') icon = 'exclamation-circle';
    
    alertDiv.innerHTML = `
        <div class="d-flex align-items-center">
            <i class="fas fa-${icon} me-3"></i>
            <div>${message}</div>
        </div>
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
   
    alertDiv.style.opacity = '0';
    alertDiv.style.transform = 'translateY(-20px)';
    document.body.appendChild(alertDiv);
    
   
    setTimeout(() => {
        alertDiv.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
        alertDiv.style.opacity = '1';
        alertDiv.style.transform = 'translateY(0)';
    }, 10);
    
    
    setTimeout(() => {
        alertDiv.style.opacity = '0';
        alertDiv.style.transform = 'translateY(-20px)';
        
        setTimeout(() => {
            if (alertDiv.parentNode) {
                alertDiv.parentNode.removeChild(alertDiv);
            }
        }, 300);
    }, 5000);
    
    
    const closeButton = alertDiv.querySelector('.btn-close');
    if (closeButton) {
        closeButton.addEventListener('click', () => {
            alertDiv.style.opacity = '0';
            alertDiv.style.transform = 'translateY(-20px)';
            
            setTimeout(() => {
                if (alertDiv.parentNode) {
                    alertDiv.parentNode.removeChild(alertDiv);
                }
            }, 300);
        });
    }
}