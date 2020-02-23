function count() {
    var num1, num2, num3, num4, num5, num6, num7, num8, result;

    num1 = document.getElementById('n1').value;
    num1 = parseFloat(num1);

    num2 = document.getElementById('n2').value;
    num2 = parseFloat(num2);

    num3 = document.getElementById('n3').value;
    num3 = parseFloat(num3);

    num4 = document.getElementById('n4').value;
    num4 = parseFloat(num4);

    num5 = document.getElementById('n5').value;
    num5 = parseFloat(num5);

    num6 = document.getElementById('n6').value;
    num6 = parseFloat(num6);

    num7 = document.getElementById('n7').value;
    num7 = parseFloat(num7);

    num8 = document.getElementById('n8').value;
    num8 = parseFloat(num8);

    result = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8) / 8;
    document.getElementById('out').innerHTML = result.toFixed();
}