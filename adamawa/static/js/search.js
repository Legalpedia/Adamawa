

$('#search').keyup(function(){

    var q=$('#search').val();
    if(q.length>=3){
       $('#search').bootcomplete({url:'search'})
    }

});



