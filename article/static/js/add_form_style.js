$(function(){
        var content_first = $('.form_content').clone();
        content_first.removeClass("form_content");
        $('form').on('click', "input.add_more", function (e) {
            var forms_id = parseInt($('#id_form-TOTAL_FORMS').val());
            forms_id += 1;
            $('#id_form-TOTAL_FORMS').val(forms_id);
            var content = $(content_first).clone();
            var selects = $('select', content);
            $('.add_more').val('Remove').addClass('remove').removeClass('add_more');
            $('.remove', content).val('Add More').addClass('add_more').removeClass('remove');
            for (var i=0; i< selects.length; i++){

                $(selects[i]).attr('name', $(selects[i]).attr('name').replace(/\d+/g, forms_id-1));
                $(selects[i]).attr('id', $(selects[i]).attr('id').replace(/\d+/g, forms_id-1));
            }
            $('.add_content').append(content);
        });
        $('form').on('click', "input.remove", function (e) {
            var forms_id = parseInt($('#id_form-TOTAL_FORMS').val());
            forms_id -= 1;
            $('#id_form-TOTAL_FORMS').val(forms_id);
            $(this).parent().parent().fadeOut(300, function(){
                $(this).remove();
            });
            var divs = $('div', 'form');
            for (var i=0; i< divs.length; i++){
                var selects = $('select', divs[i]);
                for (var j=0; j< selects.length; j++){
                    $(selects[j]).attr('name', $(selects[j]).attr('name').replace(/\d+/g, i));
                    $(selects[j]).attr('id', $(selects[j]).attr('id').replace(/\d+/g, i));
                }

            }
        })
    });
