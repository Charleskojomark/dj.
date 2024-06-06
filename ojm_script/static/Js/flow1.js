document.addEventListener('DOMContentLoaded', () => {
    const formSteps = document.querySelectorAll('.form-step');
    const steps = document.querySelectorAll('.step');
    let currentStep = 0;
  
    
  
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
      formSteps[step].classList.remove('active');
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
          errorTag.innerText = `${input.name} is required`;
        } else if (input.type === 'email' && !validateEmail(input.value)) {
          isValid = false;
          input.classList.add('input-error');
          errorTag.innerText = 'Invalid email format';
        } else {
          input.classList.remove('input-error');
          errorTag.innerText = '';
        }
      });
      
      
    }
  
    function validateEmail(email) {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return re.test(String(email).toLowerCase());
    }
  
  
    function capitalize(str) {
      return str.charAt(0).toUpperCase() + str.slice(1);
    }
  });
  