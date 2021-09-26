var textarea = document.querySelector('#_text');


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
