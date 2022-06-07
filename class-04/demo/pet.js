var oscar = {
name: "Oscar",
speak: "Whoof"
}

var sherry = {
name : "Sherry",
speak : "Meooow"
}

function Pet(name, speak){
this.name = name;
this.speak = speak
}

var oscar = new Pet('Oscar', 'Whoof')
var sherry = new Pet('Sherry', 'Meooow')

Pet.prototype.get_sound = function (){
    return this.speak
}


class Pet{
    constructor(name, speak){
    this.name = name,
    this.speak = speak
    }
}

oscar.get_sound()

DRY: Do not Repeat Yourself