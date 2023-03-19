function reverse(str) {
    let i = str.length, j = ''

    while (i > 0) {
        j += str.substring(i - 1, i)
        i--
    }
    return j
}
console.log(reverse('Vou inverter isso usando while com concatenação e substring'))

// Esse eu utilizei uma função própria