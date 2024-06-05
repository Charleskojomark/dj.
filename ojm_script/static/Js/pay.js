document.addEventListener('DOMContentLoaded', () => {
    // Show only the selected section and reset selections
    window.showSection = function(sectionId) {
        resetSelections();
        document.getElementById('subscribe-section').style.display = 'none';
        document.getElementById('fund-wallet-section').style.display = 'none';
        document.getElementById(sectionId).style.display = 'block';
    };

    // Reset selections
    function resetSelections() {
        const subscribeCheckboxes = document.querySelectorAll('input[name="subscribe-plan"]');
        subscribeCheckboxes.forEach(checkbox => checkbox.checked = false);
        const fundCheckboxes = document.querySelectorAll('input[name="fund-plan"]');
        fundCheckboxes.forEach(checkbox => checkbox.checked = false);

        document.getElementById('selected-subscription').style.display = 'none';
        document.getElementById('selected-plan').style.display = 'none';
        document.getElementById('selected-subscription-price').innerText = '';
        document.getElementById('selected-subscription-save').innerText = '';
        document.getElementById('selected-plan-price').innerText = '';
        document.getElementById('selected-plan-save').innerText = '';
    }

    // Select a subscription plan and show details
    window.selectSubscriptionPlan = function(id, priceText, discountedPrice, savings) {
        const checkboxes = document.querySelectorAll('input[name="subscribe-plan"]');
        checkboxes.forEach(checkbox => {
            checkbox.checked = checkbox.id === id;
        });
        document.getElementById('selected-subscription').style.display = 'block';
        document.getElementById('selected-subscription-price').innerText = priceText;
        document.getElementById('selected-subscription-save').innerText = `${discountedPrice} (${savings})`;
    };

    // Select a fund plan and show details
    window.selectFundPlan = function(id, priceText, discountedPrice, savings) {
        const checkboxes = document.querySelectorAll('input[name="fund-plan"]');
        checkboxes.forEach(checkbox => {
            checkbox.checked = checkbox.id === id;
        });
        document.getElementById('selected-plan').style.display = 'block';
        document.getElementById('selected-plan-price').innerText = priceText;
        document.getElementById('selected-plan-save').innerText = `${discountedPrice} (${savings})`;
    };
});
