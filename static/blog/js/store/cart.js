var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
  updateBtns[i].addEventListener('click', function(){
    var productId = this.dataset.product
    var action = this.dataset.action
    console.log('productId:', productId, 'action:', action)
    console.log('USER:', user)
    if(user == 'AnonymousUser'){
      console.log('About to execute addCookieItem')
      addCookieItem(productId, action)
      console.log('After executing addCookieItem')
    }else{
      console.log('About to execute updateUserOrder')
      updateUserOrder(productId, action)
      console.log('After executing updateUserOrder')
    }
  })
}

function addCookieItem(productId, action){
  console.log('User is not authenticated')
  console.log('Logged to console from within addCookieItem')
  console.log(cart)
  console.log(cart[productId])

  if(action == 'add'){
    if (cart[productId] === undefined){
      cart[productId] = {'quantity':1}
      console.log("First unit of product", productId, "added")
    }else{
      cart[productId]['quantity'] += 1
      console.log("Another unit of product", productId, "added")
    }
  }

  if (action == 'remove'){
    cart[productId]['quantity'] -= 1
    console.log("One unit of product", productId, "removed")

    if (cart[productId]['quantity'] <= 0){
      console.log('Item should be deleted')
      delete cart[productId]
    }
  }
  console.log('Cart:', cart)
  document.cookie = 'cart=' + JSON.stringify(cart) + ";domain;path=/"
  location.reload()
}

function updateUserOrder(productId, action){
  console.log("User is logged in, sending data...")

  var url = '/store/update_item/'

  fetch(url, {
    method: 'POST',
    headers:{
      'Content-Type':'application/json',
      'X-CSRFToken':csrftoken,
    },
    body:JSON.stringify({'productId':productId, 'action':action})
  })

  .then((response) => {
    return response.json(); 
  })

  .then((data) => {
    console.log('data:', data)
    location.reload()
  })
}
