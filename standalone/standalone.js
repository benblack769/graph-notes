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
function node_changed(node_data,node_name){
    if(!node_name){
        node_name = node_data[0]['node']
    }

    window.location = (""+window.location).replace(/#[A-Za-z0-9_]*$/,'')+"#"+node_name
    document.getElementById("svg_obj").data = "graphs/"+node_name+".svg"
}
function setup_state(node_data){
    var a = document.getElementById("svg_obj");
    var svgDoc = a.contentDocument;
    // get the inner element by id
    node_data.forEach(function(data){
        var name = data['node']

        var delta = svgDoc.getElementById(name);
        if(delta){
            // add behaviour
            delta.addEventListener("mousedown",function(){
                node_changed(node_data,name)
            }, false);
        }
    })
}
function on_data_load(){
    setup_state(node_js_info, (''+window.location).split('#')[1])
}
$(document).ready(function(){
    setup_popup()

    document.getElementById("svg_obj").onload = on_data_load
    node_changed(node_js_info,(''+window.location).split('#')[1])

    //node_changed(node_js_info,node_js_info[0]['node'])
    //setup_initial_state(node_js_info)
})
