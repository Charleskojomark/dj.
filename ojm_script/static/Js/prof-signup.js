document.addEventListener('DOMContentLoaded', () => {
    const formSteps = document.querySelectorAll('.form-step');
    const steps = document.querySelectorAll('.step');
    let currentStep = 0;
  
    const locations = {
      nigeria: {
        abia: {
          aba: ['Faulks Road', 'Azikiwe Road'],
          umuahia: ['Orji Uzor Kalu Road', 'Bank Road']
        },
        lagos: {
          ikeja: ['Allen Avenue', 'Oba Akran Avenue'],
          lekki: ['Admiralty Way', 'Freedom Way']
        }
      }
      // Add more countries, states, cities, and areas as needed
    };
  
    formSteps[currentStep].classList.add('active');
    steps[currentStep].classList.add('active');
    
    window.nextStep = (step) => {
      if (validateStep(step - 1)) {
        formSteps[step - 1].classList.remove('active');
        steps[step - 1].classList.remove('active');
        steps[step - 1].classList.add('completed');
        
        currentStep = step;
        
        formSteps[currentStep].classList.add('active');
        steps[currentStep].classList.add('active');
      }
    };
  
    window.previousStep = (step) => {
      formSteps[step].classList.remove
      ('active');
      steps[step].classList.remove('active');
      steps[step].classList.remove('completed');
      
      currentStep = step - 1;
      
      formSteps[currentStep].classList.add('active');
      steps[currentStep].classList.add('active');
    };
  
    function validateStep(step) {
      const form = formSteps[step].querySelectorAll('input, select');
      let isValid = true;
      
      form.forEach(input => {
        const errorTag = input.nextElementSibling;
        if (!input.checkValidity()) {
          isValid = false;
          input.classList.add('input-error');
          if (errorTag) { // Check if errorTag exists
            errorTag.innerText = `${input.name} is required`;
          }
          // errorTag.innerText = `${input.name} is required`;
        } else if (input.type === 'email' && !validateEmail(input.value)) {
          isValid = false;
          input.classList.add('input-error');
          if (errorTag) { // Check if errorTag exists
            errorTag.innerText = 'Invalid email format';
          }
          // errorTag.innerText = 'Invalid email format';
        } else {
          input.classList.remove('input-error');
          if (errorTag) { // Check if errorTag exists
            errorTag.innerText = '';
          }
          // errorTag.innerText = '';
        }
      });
      
      if (step === 2) {
        const password = formSteps[2].querySelector('#password');
        const confirmPassword = formSteps[2].querySelector('#confirmPassword');
        const confirmPasswordError = confirmPassword.nextElementSibling;
        
        if (password.value !== confirmPassword.value) {
          isValid = false;
          password.classList.add('input-error');
          confirmPassword.classList.add('input-error');
          confirmPasswordError.innerText = 'Passwords do not match';
        } else {
          password.classList.remove('input-error');
          confirmPassword.classList.remove('input-error');
          confirmPasswordError.innerText = '';
        }
      }
      
      return isValid;
    }
  
    function validateEmail(email) {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return re.test(String(email).toLowerCase());
    }
  
    
  
    
  
    
  
    function capitalize(str) {
      return str.charAt(0).toUpperCase() + str.slice(1);
    }
  });
