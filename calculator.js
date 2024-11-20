class SimpleCalculator {
    add(a, b) {
        return a + b;
    }

    subtract(a, b) {
        return a - b;
    }

    multiply(a, b) {
        return a * b;
    }

    divide(a, b) {
        if (b === 0) {
            throw new Error("Cannot divide by zero");
        }
        return a / b;
    }

    factorial(n) {
        if (n === 0) {
            return 1;
        } else {
            return n * this.factorial(n - 1);
        }
    }
}

function main() {
    const calculator = new SimpleCalculator();
    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });

    readline.question("Enter operation (add, subtract, multiply, divide, factorial): ", operation => {
        operation = operation.trim().toLowerCase();
        if (operation === "factorial") {
            readline.question("Enter a number: ", n => {
                console.log(`Factorial: ${calculator.factorial(parseInt(n))}`);
                readline.close();
            });
        } else {
            readline.question("Enter first number: ", a => {
                readline.question("Enter second number: ", b => {
                    a = parseFloat(a);
                    b = parseFloat(b);
                    switch (operation) {
                        case "add":
                            console.log(`Addition: ${calculator.add(a, b)}`);
                            break;
                        case "subtract":
                            console.log(`Subtraction: ${calculator.subtract(a, b)}`);
                            break;
                        case "multiply":
                            console.log(`Multiplication: ${calculator.multiply(a, b)}`);
                            break;
                        case "divide":
                            try {
                                console.log(`Division: ${calculator.divide(a, b)}`);
                            } catch (error) {
                                console.log(error.message);
                            }
                            break;
                        default:
                            console.log("Invalid operation");
                    }
                    readline.close();
                });
            });
        }
    });
}

main();