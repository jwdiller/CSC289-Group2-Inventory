var productIndex = 0;

function addItem() {
    var itemObj = [];

    itemObj.push(document.createElement("div"));
    itemObj[0].setAttribute("class", "product_entry");
    itemObj[0].setAttribute("id", ++productIndex+'_product');

    itemObj.push(document.createElement("div")); //<div class="first_bar" id="1_fb">
    itemObj[1].setAttribute("class", "first_bar");
    itemObj[1].setAttribute("id", productIndex+"_fb");

        var supplier_choice_span = document.createElement("span");
        supplier_choice_span.setAttribute("class", "supplier_choice");
        supplier_choice_span.setAttribute("id", productIndex+"_sc")

            var supplier_choice_option = document.createElement("select");
            supplier_choice_option.setAttribute("onchange", "upDateProductChoice()");
            var supplier_options = [];// that is ajax query to SQL
            for (let supplier in supplier_options) {
                var supplier_option = document.createElement("option");
                supplier_option.innerHTML = supplier;
                supplier_choice_option.appendChild(supplier_option);
            }

            supplier_choice_span.appendChild(supplier_choice_option);

        var product_choice_span = document.createElement("span");
        product_choice_span.setAttribute("class", "product_choice");
        product_choice_span.setAttribute("id", productIndex+"_pc");
        product_choice_span.innerHTML = "Choose a Supplier";

        var remove_product_button = document.createElement("button");

        itemObj[1].appendChild(supplier_choice_span);
        itemObj[1].appendChild(product_choice_span);
        itemObj[1].appendChild(remove_product_button);

    itemObj.push(document.createElement("div")); //<div class="second_bar" id="1_sb">
    itemObj[2].setAttribute("class", "second_bar");
    itemObj[2].setAttribute("id", productIndex+"_sb");

            var product_price_span = document.createElement("span");
            product_price_span.setAttribute("class", "product_price");
            product_price_span.setAttribute("id", productIndex+"_pp");
            product_price_span.innerHTML = "-----";

            var product_amount_span = document.createElement("span");
            product_amount_span.setAttribute("class", "product_amount");
            product_amount_span.setAttribute("id", productIndex+"_pa");

                var product_amount_field = document.createElement("input");
                product_amount_field.setAttribute("type", "number");
                product_amount_field.setAttribute("class", "product_amount_input");
                product_amount_field.setAttribute("id", productIndex+"_ppi");
                product_amount_field.setAttribute("value", 0);
                product_amount_field.setAttribute("oninput", "calculateMiniTotal(" + productIndex + ")");

                product_amount_span.appendChild(product_amount_field);

            var product_miniTotal_span = document.createElement("span");
            product_miniTotal_span.setAttribute("class", "product_minitotal");
            product_miniTotal_span.setAttribute("id", productIndex + "_mt");
            product_miniTotal_span.innerHTML = "-----";

            itemObj[2].appendChild(product_price_span);
            itemObj[2].appendChild(product_amount_field);
            itemObj[2].appendChild(product_miniTotal_span);

    itemObj.push(document.createElement("div"));
    itemObj[3].setAttribute("class", "third_bar");
    itemObj[3].setAttribute("id", productIndex+"_tb");

            var product_discount_span = document.createElement("span");
            product_discount_span.setAttribute("class", "product_discount_span");
            product_discount_span.setAttribute("id", "product_discount_span");
            product_discount_span.innerHTML = "Discount : ";

                var product_discount_field = document.createElement("input");
                product_discount_field.setAttribute("type", "number");
                product_discount_field.setAttribute("class", "product_discount_field");
                product_discount_field.setAttribute("id", productIndex + "_pdf");
                product_discount_field.setAttribute("oninput", "changeDiscount(" + productIndex +")");
                product_discount_span.appendChild(product_discount_field);

            var product_trueTotal_span = document.createElement("span");
            product_discount_field.setAttribute("class", "product_true_total");
            product_discount_field.setAttribute("id", productIndex + "_ppt");
            product_trueTotal_span.innerHTML = "-----";

        itemObj[3].appendChild(product_discount_span);
        itemObj[3].appendChild(product_trueTotal_span);

    for (let looper=1; looper<itemObj.length; looper++) {
        itemObj[0].appendChild(itemObj[looper]);
    }

    document.getElementById("item_ringup").appendChild(itemObj[0]);
}

function removeItem(itemNum) {
    document.getElementById(itemNum + "_product").remove;
}

function subtractDiscount(itemNum) {
    document.getElementById(itemNum + "_ppt").innerHTML = document.getElementById(itemNum + "_mt") - document.getElementById(itemNum + "_pdf").value;
}

function calculateMiniTotal(itemNum) {
    document.getElementById(itemNum + "_mt").innerHTML = document.getElementById(itemNum + "_pp").innerHTML * document.getElementById(itemNum + "_ppi").value;
    subtractDiscount(itemNum);
}

function calculateSubTotal() {

}

function calculateTaxes() {

}

function calculateTotal() {

}

function calculateChange() {

}