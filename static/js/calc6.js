function count() {
    let result = 0;
    console.group();
    for (let i = 1; i <= 6; i++) {
        console.log(typeof document.getElementById('n' + i).value.replace(',', '.'));
        if (parseFloat(document.getElementById('n' + i).value.replace(',', '.')) > 5 || parseFloat(document.getElementById('n' + i).value.replace(',', '.')) < 0) {
            alert('Неправильные данные. Средний балл должен быть меньше пяти, но больше нуля.');
            result = 0;
            break;
        }
        else {
            result = parseFloat(document.getElementById('n' + i).value.replace(',', '.'));
        }
    }
    result /= 6;
    document.getElementById('out').innerHTML = result.toFixed(2);
}