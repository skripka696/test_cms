$(function () {
   $('form').on('change', '#id_field_text', function (ev) {
       field_choice = $('#id_field_text option:selected').text();
       show_field = $('.' + field_choice);
       show_field.css("display", "block");
       show_field.parent().css("display", "block");
   })
});