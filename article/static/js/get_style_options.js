$(function(){
    $('form').on('change', 'select.style_name', function(ev){
        var current_select = ev.target;
        var current_style_id = $(current_select).val();
        $.ajax({
            url: url_to_get_style_options.replace('0', current_style_id),
            async: false,
            dataType: 'json',
            type: 'GET',
            beforeSend: function(){
                $(current_select).parent().find('.add_more').attr('disabled', 'disabled');
                $('#save_form').attr('disabled', 'disabled');
            },
            success: function(data){
                var select_for_option = $(current_select).parent().find('.style_option');
                $(select_for_option).empty();
                for (var i = 0; i < data['data'].length; i++) {
                    var $new_option = $('<option value="' + data['data'][i].id + '">' + data['data'][i].name + '</option>');
                    $(select_for_option).append($new_option);
                }
                $(select_for_option).removeAttr('disabled');
                $(current_select).parent().find('.add_more').removeAttr('disabled');
                $('#save_form').removeAttr('disabled');
            }
        });
    });
});
