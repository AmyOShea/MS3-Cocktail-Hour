$(document).ready(function(){
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown({
        inDuration: 300,
        outDuration: 300
    });
    $('select').formSelect();
    $('.collapsible').collapsible();

    // Delete recipe modal
    $('.modal').modal();

    // Home page carousel
    $('.carousel').carousel({
        fullWidth: false,
        indicators: true
    });
    // https://stackoverflow.com/questions/36581504/materialize-carousel-slider-autoplay
    // Auto-play for carousel
    autoplay();
    function autoplay() {
    $('.carousel').carousel('next');
    setTimeout(autoplay, 3500);
    }
    

});

function addIngredient(newIng) {

    let addIng = document.createElement('div');
    addIng.innerHTML = '<div id="ingredientholder" class="input-field"><i class="fas fa-wine-bottle prefix"></i><input id="ingredients" type="text" name="ingredients" class="validate"><label for="ingredients" placeholder="Ingredient">Ingredient</label><a onClick="deleteIngredient(this)">Remove</a></div>'
    document.getElementById(newIng).appendChild(addIng);
    counter++;
};

function deleteIngredient(element) {
 document.getElementById("ingredientholder").remove();
}