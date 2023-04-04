function showEncodeImage() {
  var file = document.querySelector("input[name=baseFile]").files[0];

  $(".images .nulled").hide();
  $(".images .message").hide();

  showImage(file, ".original canvas", function() {
    $(".images .original").fadeIn();
    $(".images").fadeIn();    
  });  
}

function showImage(file, canvasSelector, callback) {
  var reader = new FileReader();
  var image = new Image;
  var $canvas = $(canvasSelector);
  var context = $canvas[0].getContext('2d');

  if (file){
    reader.readAsDataURL(file);
  }

  reader.onloadend = function () {
    image.src = URL.createObjectURL(fle);

    image.onload = function () {
      $canvas.prop({
        'width': image.width,
        'height': image.height
      });
      context.drawImage(image, 0, 0);
      callback();      
    }    
  }  
}