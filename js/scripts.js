//jquerty.js
$(function(){
var dataSourseField = $('#Add_equipment');
var i = $('#Add_equipment p').size() + 1;

$('#Add_equipment_spase').on('click', function(){
$('<p><label for="input_element"><input type="text" id="input_element" size="20" name="equipment" value="" placeholder="Input Value"/></label><a href="" class="remove">Remove</a></p>').appendTo(dataSourseField);
i++;
return false;
});
$('#Add_equipment').on('click', '.remove',function(){
if (i > 2){
$(this).parent('p').remove();
i--;
}
return false;
});
});