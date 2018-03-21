function getValueUsingClass(){
    /* declare an checkbox array */
    var chkArray = [];
    /* look for all checkboes that have a class 'chk' attached to it and check if it was checked */
    $(".chk:checked").each(function() {
        chkArray.push($(this).val());
    });
    return chkArray
}