jQuery(document).ready(function ($) {
    let countrySelected = $('#id_default_country').val();
    if (!countrySelected) {
        $('#id_default_country').css('color', '#bcc8d1');
    };
    $('#id_default_country').change(function () {
        countrySelected = $(this).val();
        if (!countrySelected) {
            $(this).css('color', '#bcc8d1');
        } else {
            $(this).css('color', '#000');
        }
    });

    let dateSelected = $('#id_date_of_birth').val();
    if (!dateSelected) {
        $('#id_date_of_birth').css('color', '#bcc8d1');
    };
    $('#id_date_of_birth').change(function () {
        dateSelected = $(this).val();
        if (!dateSelected) {
            $(this).css('color', '#bcc8d1');
        } else {
            $(this).css('color', '#000');
        }
    });

})