var supplierButtons = [];
var productTabs = [];
var productAmounts = {};
var productDiscounts = {};
var productTotals = {};
var productPrices = {};
var Total = 0;

const list = JSON.parse(document.currentScript.nextElementSibling.textContent);
const buttonDiv = document.getElementById("buttonDiv");
const menuPage = document.getElementById("menuPage");
const totalPart = document.getElementById("totalPart");
const debugDiv = document.getElementById("debug");

const taxPercent = .0725; //Needs an upgrade, stat!

function displayStart() {
    var looper = 0;
    for (key in list) {
        var newButton = document.createElement("button");
        newButton.innerHTML = list[key]['supplierName'];
        newButton.setAttribute("type", "button");
        newButton.setAttribute("class", "btn btn-primary");
        newButton.setAttribute("onclick", "displayTab(" + looper++ + ")");
        supplierButtons.push(newButton);
        buttonDiv.appendChild(newButton);
        productTabs.push(document.createElement("div"));
        productTabs[productTabs.length - 1].setAttribute("style", "display : none;");
        menuPage.append(productTabs[productTabs.length - 1]);
        createList(list[key]['products']);
     }
     productTabs[0].setAttribute("style", "display : inline;");
     supplierButtons[0].disabled = true;
}

function createList(catalog) {
    var looper = 0;
    for (key in catalog) {
        var newTab = document.createElement("div");
        newTab.setAttribute("id", "list" + looper++);
        if (looper % 2 == 0) {
            newTab.setAttribute("class", "productLine evenProduct");
        } else {
            newTab.setAttribute("class", "productLine oddProduct");
        }
        productTabs[productTabs.length - 1].appendChild(newTab);
        //newTab.appendChild(createEntry(catalog[key]));
        newTab.innerHTML = createEntry2(catalog[key]);
    }
}

function displayDict(dictionary) { //For debugging, mainly
    var stringy = "";
    for (entry in dictionary) {
        stringy += entry + " : " + dictionary[entry] + "<br/>";
    }
    return stringy;
}

function displayTab(indexNum) {
    for (let looper=0; looper<productTabs.length; looper++) {
        if (looper == indexNum) {
            supplierButtons[looper].disabled = true;
            productTabs[looper].setAttribute("style", "display : inline;");
        } else {
            supplierButtons[looper].disabled = false;
            productTabs[looper].setAttribute("style", "display : none;");
        }
    }
    //menuPage.removeChild(menuPage.lastChild); //Or whatever is last
	//menuPage.appendChild(productTabs[indexNum]);
}

function createEntry(product) {
    var productLine = []
    var elementIndex = 0;
    productLine.push(document.createElement("div"));
    productLine[elementIndex].setAttribute("class", "productLine");

    productLine.push(document.createElement("span"));
    productLine[++elementIndex].innerHTML = product['productName'];
    productLine[elementIndex].setAttribute("class", "productName");

    productLine.push(document.createElement("label"));
    productLine[++elementIndex].innerHTML = "Price";
    //productLine[elementIndex].setAttribute("class", "col");
    productLine.push(document.createElement("span"));
    productLine[++elementIndex].innerHTML = product['price'];
    //productLine[elementIndex].setAttribute("class", "col");

    productLine.push(document.createElement("label"));
    productLine[++elementIndex].setAttribute("for", "amountField");
    //productLine[elementIndex].setAttribute("class", "col");
    productLine[elementIndex].innerHTML = "Amount";
    productLine.push(document.createElement("input"));
    productLine[++elementIndex].setAttribute("type", "number");
    productLine[elementIndex].setAttribute("id", "amount-" + product['id']);
    productLine[elementIndex].setAttribute("size", 6);
    productLine[elementIndex].setAttribute("class", "amountField");
    productLine[elementIndex].setAttribute("name", "amount-" + product['id']);
    productLine[elementIndex].setAttribute("oninput", "onChangeAmount(" + product['id'] + ")");
    //productLine[elementIndex].setAttribute("onchange", "onChangeAmount(" + product['id'] + ")");
    productLine[elementIndex].setAttribute("placeholder", product['amount'] + " in stock");
    productLine[elementIndex].setAttribute("aria-label", ".form-control-sm");

    productLine.push(document.createElement("label"));
    productLine[++elementIndex].setAttribute("for", "discountField");
    //productLine[elementIndex].setAttribute("class", "col");
    productLine[elementIndex].innerHTML = "Discount";
    productLine.push(document.createElement("input"));
    productLine[++elementIndex].setAttribute("type", "number");
    productLine[elementIndex].setAttribute("id", "discount-" + product['id']);
    productLine[elementIndex].setAttribute("name", "discount-" + product['id']);
    productLine[elementIndex].setAttribute("class", "discount");
    productLine[elementIndex].setAttribute("size", 7);
    productLine[elementIndex].setAttribute("pattern", "^\d*(\.\d{0,2})?$");
    productLine[elementIndex].setAttribute("aria-label", ".form-control-sm");
    productLine[elementIndex].setAttribute("oninput", "onChangeDiscount(" + product['id'] + ")");
    //productLine[elementIndex].setAttribute("onchange", "onChangeDiscount(" + product['id'] + ")");
    productLine[elementIndex].setAttribute("step", ".01");
    productLine[elementIndex].setAttribute("value", 0);

    productLine.push(document.createElement("span"));
    productLine[++elementIndex].innerHTML = "-----";
    //productLine[elementIndex].setAttribute("class", "col");
    productLine[elementIndex].setAttribute("id", "sub-" + product['id']);
    productLine[elementIndex].setAttribute("class", "productTotal");

    for (let looper=1; looper<productLine.length; looper++) {
        productLine[0].appendChild(productLine[looper]);
    }

    productPrices[product['id']] = product['price'];
    productDiscounts[product['id']] = 0;

    return productLine[0];
}

function onChangeAmount(productID) {
    var amountField = document.getElementById("amount-" + productID);
    if (amountField.value < 0) {
        amountField.value *= -1;
    }
    amountField.value = parseInt(amountField.value);
    productAmounts[productID] = amountField.value;
    calculateProductLineTotal(productID);
}

function onChangeDiscount(productID) {
    var discountField = document.getElementById("discount-" + productID);
    if (discountField.value < 0) {
        discountField.value *= -1;
    }
    if (discountField.value.length > 0) {
        productDiscounts[productID] = discountField.value;
    } else {
        productDiscounts[productID] = 0;
    }
    discountField.value = parseFloat(discountField.value).toFixed(2);
    calculateProductLineTotal(productID);
}

function calculateProductLineTotal(productID) {
    lineTotal = parseFloat((productAmounts[productID] * productPrices[productID]) - productDiscounts[productID]).toFixed(2);
    //document.getElementById("sub-" + productID).innerHTML = lineTotal;
    document.getElementById("sub-" + productID).value = lineTotal;
    productTotals[productID] = lineTotal;
    calculateTotals();
}

function calculateTotals() {
    var subTotal = 0;
    for (key in productTotals) {
        subTotal = subTotal + parseFloat(productTotals[key]);
        debugDiv.innerHTML = productTotals[key];
    }
    subTotal = parseFloat(subTotal).toFixed(2);
    var Taxes = parseFloat(subTotal * taxPercent).toFixed(2);
    Total = parseFloat(subTotal * (1 + taxPercent)).toFixed(2);
    document.getElementById("subTotal").innerHTML = subTotal;
    document.getElementById("tax").innerHTML = Taxes;
    document.getElementById("total").innerHTML = Total;
    calculateChange();
}

function calculateChange() {
    var cash = document.getElementById("cash");
    if (cash.value < 0) {
        cash.value = cash.value * -1;
    }
    try {
        var theChange = parseFloat(parseFloat(cash.value) - parseFloat(Total)).toFixed(2);
        document.getElementById("change").innerHTML = theChange;
        if (theChange < 0 || isNaN(theChange))
            document.getElementById("submit").disabled=true;
        else
            document.getElementById("submit").disabled=false;
    } catch {
        document.getElementById("change").innerHTML = "-----";
        document.getElementById("submit").disabled=true;
    }
}

function createEntry2(product) {
    var output="<span class=\"productName\">" + product['productName'] + "</span>";
    output += "<span class=\"priceSpan\"><label for=\"price\">Price</label>";
    output += "<input type readonly disabled class=\"price\" value=\"" + product['price'] + "\" size=3></input></span>";

    output += "<span class=\"amountSpan\"><label for=\"amountField\">Amount</label><input type=\"number\" id=\"";
    output += "amount-" + product['id'] + "\" size=3 class=\"amountField\" name=\"amount-" + product['id'] + "\" ";
    output += "oninput=\"onChangeAmount(" + product['id'] + ")\"></span>";

    output += "<span class=\"discountSpan\"><label for=\"discountField\">Discount</label>";
    output += "<input type=\"number\" ";
    output += "id=\"discount-" + product['id'] + "\"";
    output += " name=\"discount-" + product['id'] + "\"";
    output += " class=\"discountField\"";
    output += "size=4 pattern=\"^\d*(\.\d{0,2})?$\"";
    output += " oninput=\"onChangeDiscount(" + product['id'] + ")\"";
    output += " step=.01 value=0></input></span>";

    output += "<input type readonly disabled class=\"productTotal\" id=\"sub-" + product['id'] + "\" size=4></input>";

    productPrices[product['id']] = product['price'];
    productDiscounts[product['id']] = 0;

    return output;
}