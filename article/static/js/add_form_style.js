$(function(){
        $('form').on('click', "input.add_more", function (e) {
            var forms_id = parseInt($('#id_form-TOTAL_FORMS').val());
            forms_id += 1;
            $('#id_form-TOTAL_FORMS').val(forms_id);
            var content = $('.form_content').clone();
            content.removeClass("form_content");
            $('input[name="form-INITIAL_FORMS"]', content).remove();
            $('input[name="form-TOTAL_FORMS"]', content).remove();
            $('input[name="form-MIN_NUM_FORMS"]', content).remove();
            $('input[name="form-MAX_NUM_FORMS"]', content).remove();
            var selects = $('select', content);
            console.log(selects);
            for (var i=0; i< selects.length; i++){
                $(selects[i]).attr('name', $(selects[i]).attr('name').replace(/\d+/g, forms_id-1));
                $(selects[i]).attr('id', $(selects[i]).attr('id').replace(/\d+/g, forms_id-1));
            }
            $('form').append(content);
        });
    });