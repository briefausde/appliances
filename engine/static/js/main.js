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
                $('#myModal').css("display", "block");
            }
        });
    }

    $(".w3-quarter").click(function() {
        get_product_details(parseInt($(this).data("pk")));
    });

    $(".close").click(function() {
        $('#myModal').css("display", "none");
    });
});
