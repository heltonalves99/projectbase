django.jQuery(document).ready(function(){
    django.jQuery('.open-gallery').click(function(){
        newwindow = window.open(django.jQuery(this).attr('href'),'fileupload','height=600,width=980');
        if (window.focus) {newwindow.focus()}
        return false;
    });
});