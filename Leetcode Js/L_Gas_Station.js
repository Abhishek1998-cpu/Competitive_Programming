// Gas Station 
// Array Greedy 


/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
 var canCompleteCircuit = function(gas, cost) {
     var leftOverGas = []
     var totalGasUnit = 0
     var totalCostUnit = 0
     for(let i = 0; i < gas.length; i++){
         totalGasUnit = totalGasUnit + gas[i]
         totalCostUnit = totalCostUnit + cost[i]
         leftOverGas[i] = gas[i] - cost[i] 
     }
    if(totalCostUnit > totalGasUnit){
        return -1
    }
    var currentGas = 0
    var start = 0
    for(let i = 0; i < leftOverGas.length; i++){
        currentGas = currentGas + leftOverGas[i]
        if(currentGas < 0){
            currentGas = 0
            start = i + 1
        }
    }
    return start

};

console.log(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
console.log(canCompleteCircuit([1,2,3,4,5], [3,4,5,6,7]))