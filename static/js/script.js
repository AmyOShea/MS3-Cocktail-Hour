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

// Add another ingredient input
function addIngredient(newIng) {
    let addIng = document.createElement('div');
    addIng.innerHTML = '<div id="ingredientInput" class="input-field"><i class="fas fa-wine-bottle prefix"></i><input id="ingredients" type="text" name="ingredients" class="validate"><label for="ingredients" placeholder="Ingredient">Ingredient</label><a class="btn" onClick="deleteIngredient(this)">Remove</a></div>'
    document.getElementById(newIng).appendChild(addIng);
};

//Delete added ingredient input
function deleteIngredient(element) {
 document.getElementById("ingredientInput").remove();
}


// Add another method input
function addSteps(newStep) {
    let addStep = document.createElement('div');
    addStep.innerHTML = '<div id="methodholder" class="input-field"><i class="fas fa-list prefix"></i><input id="method" type="text" name="method" class="validate"><label for="method">Method</label><a class="btn" onClick="deleteStep(this)">Remove</a></div>'
    document.getElementById(newStep).appendChild(addStep);
};

//Delete added method input
function deleteStep(element) {
 document.getElementById("methodholder").remove();
}
