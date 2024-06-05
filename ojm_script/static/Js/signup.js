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
      
      if (step === 1) {
        const password = formSteps[1].querySelector('#password');
        const confirmPassword = formSteps[1].querySelector('#confirmPassword');
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
  
    // window.updateStates = () => {
    //   const country = document.getElementById('country').value;
    //   const stateSelect = document.getElementById('state');
    //   const citySelect = document.getElementById('city');
    //   const areaSelect = document.getElementById('area');
      
    //   stateSelect.innerHTML = '<option value="">Select a state</option>';
    //   citySelect.innerHTML = '<option value="">Select a city</option>';
    //   areaSelect.innerHTML = '<option value="">Select an area</option>';
      
    //   if (country && locations[country]) {
    //     Object.keys(locations[country]).forEach(state => {
    //       const option = document.createElement('option');
    //       option.value = state;
    //       option.text = capitalize(state);
    //       stateSelect.add(option);
    //     });
    //   }
    // };
  
    // window.updateCities = () => {
    //   const country = document.getElementById('country').value;
    //   const state = document.getElementById('state').value;
    //   const citySelect = document.getElementById('city');
    //   const areaSelect = document.getElementById('area');
      
    //   citySelect.innerHTML = '<option value="">Select a city</option>';
    //   areaSelect.innerHTML = '<option value="">Select an area</option>';
      
    //   if (country && state && locations[country][state]) {
    //     Object.keys(locations[country][state]).forEach(city => {
    //       const option = document.createElement('option');
    //       option.value = city;
    //       option.text = capitalize(city);
    //       citySelect.add(option);
    //     });
    //   }
    // };
  
    // window.updateAreas = () => {
    //   const country = document.getElementById('country').value;
    //   const state = document.getElementById('state').value;
    //   const city = document.getElementById('city').value;
    //   const areaSelect = document.getElementById('area');
      
    //   areaSelect.innerHTML = '<option value="">Select an area</option>';
      
    //   if (country && state && city && locations[country][state][city]) {
    //     locations[country][state][city].forEach(area => {
    //       const option = document.createElement('option');
    //       option.value = area;
    //       option.text = capitalize(area);
    //       areaSelect.add(option);
    //     });
    //   }
    // };
  
    function capitalize(str) {
      return str.charAt(0).toUpperCase() + str.slice(1);
    }
  });
  