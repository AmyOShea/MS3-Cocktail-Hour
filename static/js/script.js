$(document).ready(function(){
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown({
        inDuration: 300,
        outDuration: 300
    });
    $('select').formSelect();
    $('.collapsible').collapsible();

    // Add another ingredient

    $('#add-ingredient').on('click', function () {
        const addIngredient = '<div class="input-field"><i class="fas fa-wine-bottle prefix"></i><input id="ingredients" name="ingredients" type="text" class="validate" required><label for="ingredients">Ingredients</label></div>'
        $('#new-ingredient').append(addIngredient);
    });

    // Add another method step

    $('#add-step').on('click', function () {
      const addStep = '<div class="input-field"><i class="fas fa-list prefix"></i><input id="method" name="method" type="text" class="validate" required><label for="method">Method</label></div>'
      $('#new-step').append(addStep);
    });

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

