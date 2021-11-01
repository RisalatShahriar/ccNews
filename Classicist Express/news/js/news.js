const bold = $(".bold_btn");
const italic = $(".italic_btn");
const underline = $(".underline_btn");
const next_btn = $("#continue_btn");
const back_btn = $("#back_btn");
const publishing_area = $("#news_publishing");
const writing_area = $("#news_writing");
const writing_field = $("#news_writing > textarea");
const thumbnail = $("#thumbnail");
const btn_edit = $(".btn_edit");
const dlt_btn = $(".btn_delete");
var image_hash = "";
var step = 1;
var draft = 0;

var draftTitle = "Untitled";
var draftDesc = "";

var newsCard = `<div class="news_card" id="d_${draft}">
            <section class="image"></section>
            <h6>${draftTitle}</h6>
            <p>${{draftDesc}}</p>
            <ul class="stats">
                <li title="Saved as draft"><span class="badge badge-danger">Draft</span></li>
            </ul>
            <ul class="actions">
                <li><button type="button" class="btn btn-primary btn-sm" id="d_${draft}"><i class="fas fa-edit"></i> Edit</button></li>
                <li><button type="button" class="btn btn-primary btn-sm" id="d_${draft}"><i class="fas fa-external-link-alt"></i> View</button></li>
                <li><button type="button" class="btn btn-danger btn-sm" id="d_${draft}"><i class="fas fa-trash"></i> Delete</button></li>
            </ul>
        </div>`

function addStr(str, index,end, stringToAdd,stringToFinish){
  finalStr = str.substring(0, index) + stringToAdd + str.substring(index, end)+stringToFinish+str.substring(end,str.length);
  return finalStr;
}
function doFontWork(str){
	if (str.length>=250) {
		str = str.substring(0,250)+"...";
	}
	str = str.replace("[B]","<b>");
	str = str.replace("[/B]","</b>");
	str = str.replace("[U]","<u>");
	str = str.replace("[/U]","</u>");
	str = str.replace("[I]","<i>");
	str = str.replace("[/I]","</i>");

	return str;
}
function setCaretPosition(elemId, caretPos) {
    var elem = document.getElementById(elemId);
    elem.focus();

    if(elem != null) {
        if(elem.createTextRange) {
            var range = elem.createTextRange();
            range.move('character', caretPos);
            range.select();
        }
        else {
            if(elem.selectionStart) {
                elem.focus();
                elem.setSelectionRange(caretPos, caretPos);
            }
            else
                elem.focus();
        }
    }
}

bold.click(function(){
	var startpos = $('.writing-area')[0].selectionStart;
	$('.writing-area').val(addStr($('.writing-area').val(), $('.writing-area')[0].selectionStart,$('.writing-area')[0].selectionEnd, "[B]","[/B]"));
	// setCaretPosition($('.writing-area'),0);
	$('.writing-area').focus();
	$('.writing-area')[0].selectionEnd= startpos+3;
});


italic.click(function(){
	var startpos = $('.writing-area')[0].selectionStart;
	$('.writing-area').val(addStr($('.writing-area').val(), $('.writing-area')[0].selectionStart,$('.writing-area')[0].selectionEnd, "[I]","[/I]"));
	// setCaretPosition($('.writing-area'),0);
	$('.writing-area').focus();
	$('.writing-area')[0].selectionEnd= startpos+3;
});

underline.click(function(){
	var startpos = $('.writing-area')[0].selectionStart;
	$('.writing-area').val(addStr($('.writing-area').val(), $('.writing-area')[0].selectionStart,$('.writing-area')[0].selectionEnd, "[U]","[/U]"));
	// setCaretPosition($('.writing-area'),0);
	$('.writing-area').focus();
	$('.writing-area')[0].selectionEnd= startpos+3;
});

next_btn.click(function(){
	if (step==1) {
		step = 2;
		writing_area.css("display","none");
		publishing_area.css("display","");
		// draft_btn.css("display","block");
		next_btn.html("Publish");
		back_btn.css("display","block");
	}else if(step==2){
		alert("Call publish area");
	}
});

back_btn.click(function(){
	if (step==1) {
		alert("Nothing to go back");
		back_btn.css("display","block");
	}else if(step==2){
		back_btn.css("display","none");
		step = 1;
		publishing_area.css("display","none");
		writing_area.css("display","");
		next_btn.html("Next");
		// draft_btn.css("display","none");
	}
});

thumbnail.change(function(){
	if (!thumbnail[0].files[0]) return 0;
	var fd=new FormData();
	fd.append('file', thumbnail[0].files[0]);
	$.ajax({
        url: './image-management/index.php',
        type: 'post',
        data: fd,
        contentType: false,
        processData: false,
        success: function(response,data){
        	var res = JSON.parse(response);
        	$("#thumbnail_preview").css("background-image","url(./image-management/image/"+res.msg+")");
        	if (draft) {
        		image_hash = res.msg;
        		$("#editing_draft > section").css("background-image","url(./image-management/image/"+res.msg+")");
        	}
            // if(response != 0){
            //    alert('file uploaded');
            // }
            // else{
            //     alert('file not uploaded');
            // }
        },
    });
});

writing_field.keydown(function(){
	if (writing_field.val()=="" && draft==0) {
		$.get("./api/newDraft.php",function(data){
			var res = JSON.parse(data);
			draft = res.draftID;
			$("#exampleModalLabel").html($("#exampleModalLabel").html() + " | <small>saved as draft ("+draft+")</small>");
			var newsCard2 = `<div class="news_card" id="d_${draft}">
            <section class="image"></section>
            <h6>${draftTitle}</h6>
            <p>${{draftDesc}}</p>
            <ul class="stats">
                <li title="Saved as draft"><span class="badge badge-danger">Draft</span></li>
            </ul>
            <ul class="actions">
                <li><button type="button" class="btn btn-primary btn-sm" id="d_${draft}"><i class="fas fa-edit"></i> Edit</button></li>
                <li><button type="button" class="btn btn-primary btn-sm" id="d_${draft}"><i class="fas fa-external-link-alt"></i> View</button></li>
                <li><button type="button" class="btn btn-danger btn-sm" id="d_${draft}"><i class="fas fa-trash"></i> Delete</button></li>
            </ul>
        </div>`
			$(".news_list").prepend(newsCard2);

			$("#writeArticle").html('<i class="fas fa-pen-square"></i> Continue Editing Draft');
		});
	}else{
		// $(`#d_${draft} > p`).html(writing_field.val());
		// alert(writing_field.val());
	}
});

btn_edit.click(function(){
	const id = $(this).attr("value").split("_")[1];
	$.post("./api/getDraft.php",{
		draftID:id
	},function(data){
		// alert(data);

		const res = JSON.parse(data);
		if(res.success){
			draft = id;
			$(".writing-area").html(res.desc);
			$("#newsTitle").val(res.title);
			$("#thumbnail_preview").css("background-image","url(./image-management/image/"+res.image+")");
			image_hash = res.image;
		}
		
	});
	// $(".writing-area");
});

dlt_btn.click(function(){
	const id = $(this).attr("value").split("_")[1];
	$.post("./api/deleteNews.php",{
		newsID:id
	},function(data){
		var info = JSON.parse(data);
		if (info.msg=="Article removed") {
			$(`#d_${id}`).remove();
			toaster("Article deleted successfully");
		}
	});
});

$("#newArticleClose").click(function(){
	$("#writeArticle").html('<i class="fas fa-pen-square"></i> New Article');
	writing_field.val("");
	$("#newsTitle").html("Untitled");
	$("#thumbnail_preview").css("background-image", "url('./images/thumb_prev.png')");
});


setInterval(function(){
	if(draft!=0 && $("#newArticle").hasClass("show")){
		$(`#d_${draft} > p`).html(doFontWork(writing_field.val()));
		$(`#d_${draft} > h6`).html($("#newsTitle").val());
		if (image_hash) $(`#d_${draft} > section`).css("background-image","url(./image-management/image/"+image_hash+")");
		$.post("./api/updateDraft.php",{
			content:doFontWork(writing_field.val()),
			title:$("#newsTitle").val(),
			image:image_hash,
			draftID:draft
		},function(data){
			var res = JSON.parse(data);
			if (!res.success) alert(res.msg);
		});
	}
},1000);

// let str = "This is a string";
// let stringToAdd = "modyfied ";

// console.log(addStr($('.writing-area').val(), 10, stringToAdd));