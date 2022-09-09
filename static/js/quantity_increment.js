// JQuery code taken from CI Boutique Ado

// Disable +/- buttons outside 1 - tour max range
function handleEnableDisable(itemId, tour_max) {
    var currentValue = parseInt($(`#id_qty_${itemId}`).val());
    var minusDisabled = currentValue <= 2;
    var plusDisabled = currentValue >= tour_max-1;
    console.log(currentValue)
    console.log(tour_max)
    if (minusDisabled) {
        $(`#decrease-qty_${itemId}`).attr('disabled', 'disabled');
    } else {
        $(`#decrease-qty_${itemId}`).removeAttr('disabled', 'disabled');
    };
    if (plusDisabled) {
        $(`#increase-qty_${itemId}`).attr('disabled', 'disabled');
    } else {
        $(`#increase-qty_${itemId}`).removeAttr('disabled', 'disabled');
    };
}

// Increase quantity
$('.increase-qty').click(function (e) {
    e.preventDefault();
    var closestInput = $(this).closest('.input-group').find('.quantity-input')[0];
    var currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue + 1);
});

// Decrease quantity
$('.decrease-qty').click(function (e) {
    e.preventDefault();
    var closestInput = $(this).closest('.input-group').find('.quantity-input')[0];
    var currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue - 1);
});

    // Update quantity on click
    $('.update-link').click(function(e) {
        var form = $(this).prev('.update-form');
        form.submit();
    })

    // Remove item and reload on click
    $('.remove-item').click(function(e) {
        var csrfToken = "{{ csrf_token }}";
        var itemId = $(this).attr('id').split('remove_')[1];
        var url = `/bag/remove/${itemId}`;
        var data = {'csrfmiddlewaretoken': csrfToken};

        $.post(url, data)
         .done(function() {
             location.reload();
         });
    })