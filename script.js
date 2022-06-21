word = "kura"
vwl = word.match(/[a{1}e{1}i{1}o{1}u{1}]/i)
pos = vwl.index
sheng = word.substring(0, pos + 1) + 'mbutu' + word.substring(pos + 1, word.length)
console.log(sheng)