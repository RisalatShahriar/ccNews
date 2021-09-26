var textarea = document.querySelector('#_text');


function check(){
    var file = document.querySelector("#myFile");
    var count = 1;
    var type;
    while (count<4) {
        op = file.value.lenght-count
        type += file.value[op]
        count++
    }
    console.log(type)
    
    
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