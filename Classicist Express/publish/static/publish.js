var textarea = document.querySelector('#_text');


function check(){
    var file = document.querySelector("#myFile").value;
    extension = file.split('.').pop();
    if (extension == 'png' || extension == 'jpg' || extension == 'jpge') {
        document.querySelector("#_check").value = 'Pass'
    }
}

function bold() {
    textarea.value += '<b></b>';
    textarea.focus();
    textarea.setSelectionRange(textarea.value.length,textarea.value.length-4)
}

function italic() {
    textarea.value += '<i></i>';
    textarea.focus();
    textarea.setSelectionRange(textarea.value.length,textarea.value.length-4)
}