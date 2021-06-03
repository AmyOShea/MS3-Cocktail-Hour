/*jshint esversion: 6 */

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

    // Dynamically adding more ingredient inputs
    let ing = 1;

    $(".add-ingredient").click(function (e) {
        e.preventDefault();
            ing++;
            $(".new-ing").append(`
            <div class="input-field">
            <i class="fas fa-wine-bottle prefix"></i>
            <input id="ingredients${ing}" name="ingredients" type="text" class="validate" required>
            <label for="ingredients${ing}">Ingredient</label>
            <button type="button" class="btn deleteIngredient">Delete</button></div>`);
    });
    
    // Dynamically removing added ingredient inputs
    $("body").on('click', ".deleteIngredient", function () {
        $(this).parent('div').remove();
        ing--;
    });
    
    // Method
    let step = 1;
    
    // Dynamically adding more method steps inputs
    $(".add-step").click(function (e) {
        e.preventDefault();
            step++;
            $(".new-step").append(`
            <div class="input-field">
            <i class="fas fa-list prefix"></i>
            <input id="method${step}" name="method" type="text" class="validate" required>
            <label for="method${step}">Method</label>
            <button type="button" class="btn deleteStep">Delete</button></div>`);
    });

    // Dynamically removing added method steps inputs
    $("body").on('click', ".deleteStep", function () {
        $(this).parent('div').remove();
        step--;
    });
});
