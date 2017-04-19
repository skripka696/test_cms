$(function(){
  console.log('tra-ta-ta');
    var title = document.querySelector('.title');
  $.ajax({
                url: url_to_get_field_style,
                async: false,
                dataType: 'json',
                type: 'GET',
                success: function (data) {
                    console.log('sff');
                    console.log(data['title']['color']);
                    title.style.setProperty('--title-color', data['title']['color'])
                }
            });
});