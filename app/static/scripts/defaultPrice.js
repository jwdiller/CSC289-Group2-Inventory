function defaultPrice() {
	priceList = document.getElementById("priceList").value()

	stockID = document.getElementsByName("stockID")[0].value()
	price = priceList[stockID]
	
	amount = document.getElementByName("amount")[0].value()

	document.getElementByName("price").value = price * amount	
}