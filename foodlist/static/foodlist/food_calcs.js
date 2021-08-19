function test() {
    
    if (testString == 'Test Worked'){
        document.getElementById("cost").innerHTML = "Test"
    } else {
        document.getElementById("cost").innerHTML = "Test Worked"
    }
}





var list = []
function calculateCost(ingredient_cost, name, qty, food_cost) {

    console.log(ingredient_cost, name, qty, food_cost)
    
    ingredient = {
        ingredient_name : name,
        cost : food_cost,
        quantity : qty
    }

    list.push(ingredient)

    // Does Object exist in array? .find(ingredient name)
    // If yes, update qty
    // If no, add new object (name, qty, cost)
    // Iterate through list to calucatle cost (for each object cost += (qty * ing cost))
    // update cost label and input value

    


}