$('.input-data').keyup(function() {
  var q = []
  var inputs = $(".input-data");
  for(var i = 0; i < inputs.length; i++){
      var x = ($(inputs[i]).val());
      if (x != ""){
        q.push(x)
        
      }
  } 
  if (q.length == 4){
    $(".details-div").css('display', 'block');
  }
  else{
    $(".details-div").css('display', 'none');
  }
}); 

$('.details-box').keyup(function() {
  var q = []
  var inputs = $(".details-box");
  for(var i = 0; i < inputs.length; i++){
      var x = ($(inputs[i]).val());
      if (x != ""){
        q.push(x)
        
      }
  } 
  if (q.length == 7){
    $(".div-details").css('display', 'block');
  }
  else{
    $(".div-details").css('display', 'none');
  }  
}); 

$(".div-details").on('click', function(e) {  
  var height = $('#height').val();
  console.log("height",height);
  var length = $('#length').val();
  console.log("length",length);
  var quantity = $('#quantity').val();
  console.log("quantity",quantity);
  $.ajax({
      type: "POST",
      url: "print-label/",
      data: {
        'height': height,
        'length': length,
        'quantity': quantity,
      }
  }).done(function(response) {
    console.log(response)
  });
});

$(function() {
  $('#company_autocomplete_input').autocomplete({
    open: function() {
    },
    source: 'auto-search/',
    select: function (event, ui) {
      $("#company_autocomplete_input").val(ui.item.category);
      var img = "/media/" + ui.item.image;
      $("#image-div").attr("src",img);
      return false;
    },    
  }).data("ui-autocomplete")._renderItem = function(ul, item) {
    return $("<li></li>")
      .data("item.autocomplete", item)
      .append("<div>" + item.comName + '-' + item.category + '-'+ item.partNum + '-'+ item.supplier + '-' + item.uom + "<img src='" + '/media/' + item.image + "' height='55' ' class='image-position' /></div>")
      .appendTo(ul);
  };
});