// JQuery code taken from CI Boutique Ado

// Disable +/- buttons outside 1 - tour max range
jQuery(document).ready(function ($) {
    function handleEnableDisable(itemId, tourMax) {
        var currentValue = parseInt($(`#id_qty_${itemId}`).val());
        var minusDisabled = currentValue <= 1;
        var plusDisabled = currentValue >= tourMax;
        if (minusDisabled) {
            $(`#decrease-qty_${itemId}`).attr('disabled', 'disabled');
        } else {
            $(`#decrease-qty_${itemId}`).removeAttr('disabled', 'disabled');
        }
        if (plusDisabled) {
            $(`#increase-qty_${itemId}`).attr('disabled', 'disabled');
        } else {
            $(`#increase-qty_${itemId}`).removeAttr('disabled', 'disabled');
        }
    }

    // Increase quantity
    $('.increase-qty').click(function (e) {
        e.preventDefault();
        var closestInput = $(this).closest('.input-group').find('.quantity-input')[0];
        var currentValue = parseInt($(closestInput).val());
        $(closestInput).val(currentValue + 1);
        var itemId = $(this).data('item_id');
        var tourMax = $(this).data('tour_max');
        handleEnableDisable(itemId, tourMax);
    });

    // Decrease quantity
    $('.decrease-qty').click(function (e) {
        e.preventDefault();
        var closestInput = $(this).closest('.input-group').find('.quantity-input')[0];
        var currentValue = parseInt($(closestInput).val());
        $(closestInput).val(currentValue - 1);
        var itemId = $(this).data('item_id');
        var tourMax = $(this).data('tour_max');
        handleEnableDisable(itemId, tourMax);
    });

    // Update quantity on click
    $('.update-link').click(function (e) {
        var form = $(this).closest('.row').prev('.update-form');
        form.submit();
    });

    // Remove item and reload on click
    $('.remove-item').click(function (e) {
        var csrfToken = $('#bag-form input[name=csrfmiddlewaretoken]').val();
        var itemId = $(this).attr('id').split('remove_')[1];
        var bagItemId = $(this).data('bag_item_id');
        var url = `/bag/remove/${itemId}/`;
        var data = {
            'csrfmiddlewaretoken': csrfToken,
            'bag_item_id': bagItemId,
        };

        $.post(url, data)
            .done(function () {
                location.reload();
            });
    });
});