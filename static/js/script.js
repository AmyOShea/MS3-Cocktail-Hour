$(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();
    $(".dropdown-trigger").dropdown({ 
        hover: true,
        inDuration: 300,
        outDuration: 300
      });
    $('#add-ingredient').on('click', function () {
        const addIngredient = '<div class="input-field"><i class="fas fa-wine-bottle prefix"></i><input id="ingredients" name="ingredients" type="text" class="validate" required><label for="ingredients">Ingredients</label></div>'
        $('#new-ingredient').append(addIngredient);
    });
    $('#add-step').on('click', function () {
      const addStep = '<div class="input-field"><i class="fas fa-list prefix"></i><input id="method" name="method" type="text" class="validate" required><label for="method">Method</label></div>'
      $('#new-step').append(addStep);
  });
});
