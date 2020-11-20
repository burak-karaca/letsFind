    const checkboxes = Array.from(document.getElementsByClassName('checkbox'));
    const divElements = Array.from(document.getElementsByClassName('list-group'));
    const shops = Array.from(document.getElementsByClassName('shops'));
    const Arr = [];
    const arrofString = [];
    for(var i = 0; i<shops.length;i++){
        arrofString.push(shops[i].textContent)
    }
    checkboxes.forEach((element,index) => {
        const textofIndex = Array.from(document.getElementsByClassName('eshoptexts')[index].textContent);
        Arr.push(textofIndex.join(''))
        element.addEventListener('click', () => {
            let count=0
            checkboxes.forEach((element,index)=>{
                if(element.checked){
                    arrofString.forEach((currentShop,currentShopIndex) => {
                        if(currentShop === Arr[index])
                        divElements[currentShopIndex].style.display = 'block';
                    })
                }
                if(!element.checked){
                        arrofString.forEach((currentShop,currentShopIndex) =>{
                        if(currentShop === Arr[index])
                        divElements[currentShopIndex].style.display = 'none';
                    })
                    count++
                }
                console.log(checkboxes.length , count)
                if(checkboxes.length==count){
                    arrofString.forEach((currentShop,currentShopIndex) =>{
                        divElements[currentShopIndex].style.display = 'block';
                    })
                }
            })
        })
    })

    const currencyArray = [];
    const userAction = async () => {
    const response = await fetch('https://api.exchangeratesapi.io/latest');
    const myJson = await response.json();
        const stringArr = [];
        const numberofStringArr = [];
        const prices = Array.from(document.getElementsByClassName('prices'));
        const currencydiv = Array.from(document.getElementsByClassName('currencyexchange'));
        const secondcurrencydiv = Array.from(document.getElementsByClassName('secondcurrencyexchange'));
        //removing PLN string and deleting spaces from a string array
        for(var j = 0 ; j<prices.length;j++){
            stringArr.push(prices[j].textContent);
            numberofStringArr.push(stringArr[j].replace("PLN ", ""));
        }
        //converting string integers into integer array
        const priceArr = numberofStringArr.map(function(item) {
            return parseFloat(item, 10);
        });
        //getting rates from currency API
        const values =  Object.values(myJson.rates);

        //rounding currencies
        const euro = [];
        const usd = [];
        for(var l = 0 ; l < priceArr.length ; l++){
            euro.push(Math.round(priceArr[l] / values[19]));
            usd.push(Math.round(euro[l] * values[26]));
        }
        //appending currencies into the div elements
        for(var i = 0 ; i < values.length ; i++){
            currencydiv[i].innerHTML = euro[i];
            secondcurrencydiv[i].innerHTML = usd[i];
        }
    }
    userAction();


        const pricesdiv = Array.from(document.getElementsByClassName('currencydiv'));
        const prices = Array.from(document.getElementsByClassName('prices'));
        prices.forEach((el,index)=>{
            el.addEventListener('mouseover',(elem)=>{
                pricesdiv[index].style.display = 'block';
            });
            el.addEventListener('mouseleave',(elem)=>{
                pricesdiv[index].style.display = 'none';
            })
        })
        console.log(pricesdiv,prices);

