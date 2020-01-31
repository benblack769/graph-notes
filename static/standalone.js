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
    var node_info = node_data.filter(x=>x['node'] === node_name)[0]

    setup_long_descript(node_info)

    window.location = (""+window.location).replace(/#[A-Za-z0-9_]*$/,'')+"#"+node_name
    //document.getElementById("svg_obj").data = "graphs/"+node_name+".svg"

    var svg_text = document.getElementById(node_name+"__svg").innerHTML
    document.getElementById("svg_obj").innerHTML = svg_text
    setup_state(node_data)
}
function setup_long_descript(node_info){
    document.getElementById("popup_content").innerHTML = ""
    if(node_info['long_description_fname']){
        var node_fname = "/long_descriptions/"+node_info['long_description_fname']+".html"
        $.get(node_fname,"",function(data){
            document.getElementById("popup_content").innerHTML = data
        })
    }
}
function setup_state(node_data){
    var a = document.getElementById("svg_obj");
    // get the inner element by id
    node_data.forEach(function(data){
        var name = data['node']

        var delta = document.getElementById(name+"__el");
        if(delta){
            // add behaviour
            delta.addEventListener("mousedown",function(){
                node_changed(node_data,name)
            }, false);
        }
    })
}
function check_window_resize(){
    var new_width = $('#display_area').parent().width();
    var old_class = document.getElementById("popup").className;
    if(old_class == "popup_global_shader" && new_width > 800){

    }
    else if(old_class != "popup_global_shader" && new_width < 800){

    }
}

$(document).ready(function(){
    var js_info_text = document.getElementById("js_node_info").innerHTML
    var node_js_info = JSON.parse(js_info_text)
    setup_popup()

    node_changed(node_js_info,(''+window.location).split('#')[1])

    //node_changed(node_js_info,node_js_info[0]['node'])
    //setup_initial_state(node_js_info)

    $(window).resize(check_window_resize);
})
