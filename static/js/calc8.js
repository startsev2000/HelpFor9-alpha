function count() {
    let result = 0;
    for (let i = 1; i <= 8; i++) {
        if (parseFloat(document.getElementById('n' + i).value.replace(',', '.')) > 5 || parseFloat(document.getElementById('n' + i).value.replace(',', '.')) < 0) {
            alert('Неправильные данные. Средний балл должен быть меньше пяти, но больше нуля.');
            result = 0;
            break;
        }
        else {
            result += parseFloat(document.getElementById('n' + i).value.replace(',', '.'));
        }
    }
    result /= 8;
    document.getElementById('out').innerHTML = result.toFixed(2);
}