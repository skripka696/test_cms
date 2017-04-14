$(function(){
        $('#add_more').on('click', function (e) {
            var forms_id = parseInt($('#id_form-TOTAL_FORMS').val());
            forms_id += 1;
            total_form.val(forms_id);
            var content = $('.form_content').clone();
            var selects = $('select', content);
            console.log(selects);
            for (var i=0; i< selects.length; i++){
                var current_select = $(selects[i]).clone();
                $(current_select).attr('name', $(current_select).attr('name').replace(/\d+/g, forms_id-1));
                $(current_select).attr('id', $(current_select).attr('id').replace(/\d+/g, forms_id-1));
                // $('form').append(current_select);
            }
            $('form').append(content);
        });
    });