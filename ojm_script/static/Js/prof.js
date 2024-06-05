// document.addEventListener('DOMContentLoaded', function() {

var fileInput = document.getElementById('id_profile_picture');
    if (fileInput) {
        fileInput.addEventListener('change', function() {
            var input = this;
            var label = document.querySelector('.custom-file-input-label');
            var fileName = input.files[0].name;
            label.textContent = fileName;
        });
    }


// var fileInput = document.getElementById('fileInput');
//     if (fileInput) {
//       fileInput.addEventListener('change', function() {
//         var input = this;
//         var label = input.nextElementSibling.querySelector('.custom-file-input-label');
//         var fileName = input.files[0].name;
//         label.textContent = fileName;
//       });
//     }




    // Get the modals
    var uploadModal = document.getElementById("uploadModal");
    var businessInfoModal = document.getElementById("businessInfoModal");
    var serviceModal = document.getElementById("serviceModal");
    var locationModal = document.getElementById("locationModal");
    var priceModal = document.getElementById("priceModal");
    var qualificationModal = document.getElementById("qualificationModal");
    var detailsModal = document.getElementById("detailsModal");
    var bankModal = document.getElementById("bankModal");
    var verificationModal = document.getElementById("verificationModal");
    var notificationModal = document.getElementById("notificationModal");
    var passwordModal = document.getElementById("passwordModal");
    var orderModal = document.getElementById("orderModal");
    var subscriptionModal = document.getElementById("subscriptionModal");
    var walletModal = document.getElementById("walletModal");


    // Get the profile picture links that open the modal
    var mainProfilePicLink = document.getElementById("mainProfilePicLink");
    var profileSettingsPicLink = document.getElementById("profileSettingsPicLink");
    var serviceLink = document.getElementById("serviceLink");
    var locationLink = document.getElementById("locationLink");
    var priceLink = document.getElementById("priceLink");
    var qualificationLink = document.getElementById("qualificationLink");
    var detailsLink = document.getElementById("detailsLink");
    var bankLink = document.getElementById("bankLink");
    var verificationLink = document.getElementById("verificationLink");
    var notificationLink = document.getElementById("notificationLink");
    var passwordLink = document.getElementById("passwordLink");
    var orderLink = document.getElementById("orderLink");
    var subscriptionLink = document.getElementById("subscriptionLink");
    var walletLink = document.getElementById("walletLink");

    // Get the business info link
    var businessInfoLink = document.getElementById("businessInfoLink");

    // Get the main profile picture element
    var mainProfilePic = document.getElementById("mainProfilePic");

    // Get the <span> elements that close the modals
    var uploadModalClose = uploadModal.getElementsByClassName("close")[0];
    var businessInfoModalClose = businessInfoModal.getElementsByClassName("close")[0];
    var serviceModalClose = serviceModal.getElementsByClassName("close")[0];
    var locationModalClose = locationModal.getElementsByClassName("close")[0];
    var priceModalClose = priceModal.getElementsByClassName("close")[0];
    var qualificationModalClose = qualificationModal.getElementsByClassName("close")[0];
    var detailsModalClose = detailsModal.getElementsByClassName("close")[0];
    var bankModalClose = bankModal.getElementsByClassName("close")[0];
    var verificationModalClose = verificationModal.getElementsByClassName("close")[0];
    var notificationModalClose = notificationModal.getElementsByClassName("close")[0];
    var passwordModalClose = passwordModal.getElementsByClassName("close")[0];
    var orderModalClose = orderModal.getElementsByClassName("close")[0];
    var subscriptionModalClose = subscriptionModal.getElementsByClassName("close")[0];
    var walletModalClose = walletModal.getElementsByClassName("close")[0];

    // Get the current profile picture element in the modal
    var currentProfilePic = document.getElementById("currentProfilePic");

    // When the user clicks on the profile picture link in the main profile, open the modal
    mainProfilePicLink.onclick = function(event) {
        event.preventDefault();
        uploadModal.style.display = "block";
        currentProfilePic.src = mainProfilePic.src;
    }

    // When the user clicks on the profile picture link in the profile settings, open the modal
    profileSettingsPicLink.onclick = function(event) {
        event.preventDefault();
        uploadModal.style.display = "block";
        // currentProfilePic.src = mainProfilePic.src;
    }

    // When the user clicks on the business info link, open the modal
    businessInfoLink.onclick = function(event) {
        event.preventDefault();
        businessInfoModal.style.display = "block";
    }
    serviceLink.onclick = function(event) {
        event.preventDefault();
        serviceModal.style.display = "block";
    }
    locationLink.onclick = function(event) {
        event.preventDefault();
        locationModal.style.display = "block";
    }
    
    priceLink.onclick = function(event) {
        event.preventDefault();
        priceModal.style.display = "block";
    }
    
    qualificationLink.onclick = function(event) {
        event.preventDefault();
        qualificationModal.style.display = "block";
    }
    
    detailsLink.onclick = function(event) {
        event.preventDefault();
        detailsModal.style.display = "block";
    }
    
    
    verificationLink.onclick = function(event) {
        event.preventDefault();
        verificationModal.style.display = "block";
    }
    
    notificationLink.onclick = function(event) {
        event.preventDefault();
        notificationModal.style.display = "block";
    }
    
    passwordLink.onclick = function(event) {
        event.preventDefault();
        passwordModal.style.display = "block";
    }
    
    orderLink.onclick = function(event) {
        event.preventDefault();
        orderModal.style.display = "block";
    }
    
    subscriptionLink.onclick = function(event) {
        event.preventDefault();
        subscriptionModal.style.display = "block";
    }
    
    walletLink.onclick = function(event) {
        event.preventDefault();
        walletModal.style.display = "block";
    }
    // When the user clicks on <span> (x), close the modals
    uploadModalClose.onclick = function() {
        uploadModal.style.display = "none";
    }

    businessInfoModalClose.onclick = function() {
        businessInfoModal.style.display = "none";
    }

    serviceModalClose.onclick = function() {
        serviceModal.style.display = "none";
    }
    
    locationModalClose.onclick = function() {
        locationModal.style.display = "none";
    }
    
    priceModalClose.onclick = function() {
        priceModal.style.display = "none";
    }
    
    qualificationModalClose.onclick = function() {
        qualificationModal.style.display = "none";
    }
    
    detailsModalClose.onclick = function() {
        detailsModal.style.display = "none";
    }
    
    bankModalClose.onclick = function() {
        bankModal.style.display = "none";
    }
    
    verificationModalClose.onclick = function() {
        verificationModal.style.display = "none";
    }
    
    notificationModalClose.onclick = function() {
        notificationModal.style.display = "none";
    }
    
    passwordModalClose.onclick = function() {
        passwordModal.style.display = "none";
    }
    
    orderModalClose.onclick = function() {
        orderModal.style.display = "none";
    }
    
    subscriptionModalClose.onclick = function() {
        subscriptionModal.style.display = "none";
    }
    
    walletModalClose.onclick = function() {
        walletModal.style.display = "none";
    }


    // When the user clicks anywhere outside of the modals, close them
    window.onclick = function(event) {
        if (event.target == uploadModal) {
            uploadModal.style.display = "none";
        }
        if (event.target == businessInfoModal) {
            businessInfoModal.style.display = "none";
        }
        if (event.target == serviceModal) {
            serviceModal.style.display = "none";
        }
        
        if (event.target == locationModal) {
            locationModal.style.display = "none";
        }
        
        if (event.target == priceModal) {
            priceModal.style.display = "none";
        }
        
        if (event.target == qualificationModal) {
            qualificationModal.style.display = "none";
        }
        if (event.target == detailsModal) {
            detailsModal.style.display = "none";
        }
        if (event.target == bankModal) {
            bankModal.style.display = "none";
        }
        if (event.target == verificationModal) {
            verificationModal.style.display = "none";
        }
        if (event.target == notificationModal) {
            notificationModal.style.display = "none";
        }
        if (event.target == passwordModal) {
            passwordModal.style.display = "none";
        }
        if (event.target == orderModal) {
            orderModal.style.display = "none";
        }
        if (event.target == subscriptionModal) {
            subscriptionModal.style.display = "none";
        }
        if (event.target == walletModal) {
            walletModal.style.display = "none";
        }
    }

   

function removeDiv(id) {
    const element = document.getElementById(id);
    if (element) {
      element.style.display = 'none';
    }
  }
  
  // Function to auto-hide divs after 8 seconds
  function autoHideDiv(id) {
    setTimeout(() => {
      removeDiv(id);
    }, 8000);
  }
  
  const errorContainer = document.getElementById('error-container');
  
  if (errorContainer) {
    // autoHideDiv('error-container');
  }
  