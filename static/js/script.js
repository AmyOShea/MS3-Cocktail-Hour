$(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('#add-ingredient').on('click', function () {
        const addIngredient = '<div class="input-field"><i class="fas fa-wine-bottle prefix"></i><input id="ingredients" name="ingredients" type="text" class="validate" required><label for="ingredients">Ingredients</label></div>'
        $('#new-ingredient').append(addIngredient);
    });
});
