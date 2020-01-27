function on_popup_create(){
    //$()
}
function setup_popup(){
    $("#popup").click(function(event) {
        $("#popup").hide()
    });
    $("#popup_body_id").click(function(event) {
        event.stopPropagation();
    });
    $("#popup_button").click(function(e){
        $("#popup").show()
    })
}
function setup_nodeselect(node_data){

}
function setup_state(node_data){
    var a = document.getElementById("svg_obj");\
    var svgDoc = a.contentDocument;
    // get the inner element by id
    node_data.forEach(function(data){
        var name = data['node']

        var delta = svgDoc.getElementById(name);
        // add behaviour
        delta.addEventListener("mousedown",function(){

        }, false);
    })
}

$(document).ready(function(){
    setup_popup()
    setup_nodeselect(node_js_info)
    //setup_initial_state(node_js_info)
})
