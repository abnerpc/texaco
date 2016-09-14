$(function(){

    showFile = function(){
        $('#errors').remove();
        var file_path = $(this).val().split('\\');
        $('#upload-file-info').html(file_path[2]);
    }
    
    $('#upload').on('change', showFile);

});