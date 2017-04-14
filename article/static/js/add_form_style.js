$(function(){
        $('form').on('click', "input.add_more", function (e) {
            var forms_id = parseInt($('#id_form-TOTAL_FORMS').val());
            forms_id += 1;
            $('#id_form-TOTAL_FORMS').val(forms_id);
            var content = $('.form_content').clone();
            content.removeClass("form_content");
            var selects = $('select', content);
            console.log(selects);
            for (var i=0; i< selects.length; i++){
                // var current_select = $(selects[i]).clone();
                $(selects[i]).attr('name', $(selects[i]).attr('name').replace(/\d+/g, forms_id-1));
                $(selects[i]).attr('id', $(selects[i]).attr('id').replace(/\d+/g, forms_id-1));
            }
            $('form').append(content);
        });
    });