$(document).ready(function() {
    function get_product_details(pk){
        $.ajax({
            url: "/product/" + pk + "/",
            type: 'GET',
            success: function(product){
                $("#modal-img").attr("src", product.product_img);
                $('#modal-category').html(product.product_category);
                $('#modal-name').html(product.product_name);
                $('#modal-description').html(product.product_description);
                $('#modal-price').html(product.product_price);
                $('#modal-clicks').html(product.product_clicks);
                $('#modal-created-date').html(product.product_created_date);
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
});
