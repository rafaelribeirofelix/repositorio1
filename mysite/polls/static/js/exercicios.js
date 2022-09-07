let op1 = undefined;
let op2 = undefined;
let operador = undefined;
let resultado = undefined;
let operadores = ["+", "-", "*", "/"];

function resolver(event) {
    const botaoClicado = event.target.textContent;
    console.log(botaoClicado);

    switch (botaoClicado) {
        case "0":
        case "1":
        case "2":
        case "3":
        case "4":
        case "5":
        case "6":
        case "7":
        case "8":
        case "9":
        case ".":
            if (operadores.includes(visor.innerHTML)) {
                visor.innerHTML = botaoClicado;
            } else {
                visor.innerHTML += botaoClicado;
            }
            console.log(botaoClicado);
            break;
        case "+":
        case "-":
        case "*":
        case "/":
            console.log(botaoClicado);
            op1 = parseFloat(visor.innerHTML);
            visor.innerHTML = botaoClicado;
            operador = visor.innerHTML;
            break;
        case "=":
            console.log(botaoClicado);
            op2 = parseFloat(visor.innerHTML);
            switch (operador) {
                case "+":
                    resultado = op1 + op2;
                    break;
                case "-":
                    resultado = op1 - op2;
                    break;
                case "*":
                    resultado = op1 * op2;
                    break;
                case "/":
                    resultado = op1 / op2;
                    break;

            }
            visor.innerHTML = resultado.toFixed(4);
            break;

        case "+/-":
            visor.innerHTML = parseFloat(visor.innerHTML) * -1;
            break;

        case "C":
            op1 = undefined;
            op2 = undefined;
            operador = undefined;
            resultado = undefined;
            visor.innerHTML = "";
            break;

    }
}

const botoes = document.querySelectorAll('.btn');
const visor = document.querySelector('#display');

botoes.forEach(function (botao) {
    botao.addEventListener('click', resolver);
});