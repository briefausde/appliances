function get_product_details(pk){
    $.ajax({
        url: "/product/" + pk + "/",
        type: 'POST',
        data: {
            csrfmiddlewaretoken: tokens.csrf_token
        },
        success: function(html){
            $('#product-detail').html(html);
            modal.style.display = "block";
        }
    });
}

var modal = document.getElementById('myModal');
var span = document.getElementsByClassName("close")[0];

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
