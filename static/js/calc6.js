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

    result = (num1 + num2 + num3 + num4 + num5 + num6) / 6;
    document.getElementById('out').innerHTML = result.toFixed(2);
}