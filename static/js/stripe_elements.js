var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
        base: {
            fontFamily: '"Montserrat", sans-serif',
            fontSize: '16px',
            '::placeholder': {
                color: '#bcc8d1'
            }
        },}

var card = elements.create('card', {style:style});
card.mount('#card-element');

const form = document.getElementById('payment-form');

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    card.update({
        'disabled': true
    });
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {
        if (result.error) {
            const messageContainer = document.querySelector('#error-message');
            messageContainer.textContent = `This is an error message`;
            card.update({
                'disabled': false
            });
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                const messageContainer = document.querySelector('#error-message');
                messageContainer.textContent = 'Success! Payment received.';
                form.submit()
            }
        };


    });
});