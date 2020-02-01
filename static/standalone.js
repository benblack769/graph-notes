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
    setup_state(node_data,node_name)
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
function setup_state(node_data,node_name){
    var svg_obj = document.getElementById("svg_obj");
    var svg = svg_obj.firstChild;
    var elipse_el = $("#"+node_name+"__el ellipse").get()[0];
    //var elipse_el =
    var graph_div = document.getElementById("svg_container");
    //set the size and position of the parent div
    graph_div.style.position = "absolute";
    graph_div.style.width = svg.width * 2 - 100;
    graph_div.style.height = svg.height * 2 - 100;

    graph_div.style.left = -svg.width + 100;
    graph_div.style.top = -svg.height + 100;

    //set position of svg so that current node is centered
    //svg_obj.style.pos
    /*var elipse_bounds = elipse_el.getBoundingClientRect();
    var cenx = (elipse_bounds.left + elipse_bounds.right)/2
    var ceny = (elipse_bounds.top + elipse_bounds.bottom)/2
    svg_obj.style.positon = "absolute"
    svg_obj.style.left = -cenx;
    svg_obj.style.top = -ceny;
    console.log(elipse_bounds)*/

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
