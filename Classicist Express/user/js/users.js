$(document).ready(function(){
	// Activate tooltip
	$('[data-toggle="tooltip"]').tooltip();
	
	// Select/Deselect checkboxes
	var checkbox = $('table tbody input[type="checkbox"]');
	$("#selectAll").click(function(){
		if(this.checked){
			checkbox.each(function(){
				this.checked = true;                        
			});
		} else{
			checkbox.each(function(){
				this.checked = false;                        
			});
		} 
	});
	checkbox.click(function(){
		if(!this.checked){
			$("#selectAll").prop("checked", false);
		}
	});
});

$("#sendInvite").click(function(){
	// alert();
	// alert($("#inviteMail").val());
	var inviteName = $("#inviteToName").val();
	var inviteTo = $("#inviteMail").val();
	var role = $("#invite_user_role").val();
	toaster("Sending...",10);
	$.post("./api/sendMail.php",{mail_to:inviteTo,role:role,name:inviteName,type:"invitation"},function(data){
		var xd = JSON.parse(data);
		$("#invitationModal").removeClass("show in");
		$(".modal-backdrop").removeClass("modal-backdrop");
		toaster(xd.msg);
	});
});