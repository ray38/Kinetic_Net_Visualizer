
function main(data) {
	console.log(data);
	var views = [];

	var margin = {top: 30, right: 20, bottom: 30, left: 50},
	width = 800 - margin.left - margin.right,
	height = 800 - margin.top - margin.bottom;

	var gui = new dat.GUI( );
	//	svg and sizing
	var svg_left = d3.select("body")
	.append("svg")
	  .attr("width", width + margin.left + margin.right)
	  .attr("height", height + margin.top + margin.bottom)
	  .style("border", "1px solid black")
	.append("g")
	  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	views.push(svg_left);
	var left_gui_folder = gui.addFolder( 'View 1' );

	// Adds the svg canvas
	var svg_right = d3.select("body")
	.append("svg")
	  .attr("width", width + margin.left + margin.right)
	  .attr("height", height + margin.top + margin.bottom)
	  .style("border", "1px solid black")
	.append("g")
	  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	views.push(svg_right);
	var right_gui_folder = gui.addFolder( 'View 2' );
	//	graph data store
	//var data;

	
	
	var view_counter = 2;



	//update();
	add_one_graph(views, svg_left,  width, height, JSON.parse(JSON.stringify(data)), left_gui_folder);
	add_one_graph(views, svg_right, width, height, JSON.parse(JSON.stringify(data)), right_gui_folder);
	//console.log(views);
	window.addEventListener( "keydown", onKeyDown, true);

	function onKeyDown(e){
	
		if (e.keyCode == 107) {

			view_counter += 1;
			var temp_svg = d3.select("body")
				.append("svg")
				  .attr("width", width + margin.left + margin.right)
				  .attr("height", height + margin.top + margin.bottom)
				  .style("border", "1px solid black")
				.append("g")
				  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

				views.push(temp_svg);
				var temp_gui_folder = gui.addFolder( 'View ' + view_counter );

				add_one_graph(views, temp_svg, width, height, JSON.parse(JSON.stringify(data)), temp_gui_folder);
				
			
		}
	}
	
}


function add_one_graph(views, svg,width, height, data, gui_folder){




    svg.append("svg:defs").selectAll("marker")
    .data(["end"])      // Different link/path types can be defined here
  		.enter().append("svg:marker")    // This section adds in the arrows
    .attr("id", 'arrowhead')
    .attr("fill","grey")
    .attr("viewBox", "0 -5 10 10")
    .attr("refX", 15)
    .attr("refY", -1.5)
    .attr("markerWidth", 10)
    .attr("markerHeight", 10)
    .attr("markerUnits","userSpaceOnUse")
    .attr("orient", "auto")
  		.append("svg:path")
    .attr("d", "M0,-5L10,0L0,5");

	var view;
	views.push(view);
	var time, pulse;
	var time_list = [], pulse_list = [];
	var graph;

	var time_choice_list = Object.keys(data).sort();
	var pulse_choice_list = Object.keys(data[time_choice_list[0]]).sort();

	var time_choice_object =  arrayToIdenticalObject(time_choice_list);
	var pulse_choice_object = arrayToIdenticalObject(pulse_choice_list);

	graph = data[time_choice_list[0]][pulse_choice_list[0]];
	
	var color = d3.scaleOrdinal(d3.schemeCategory10);

	var tooltip = d3.select("body")
	      .append("div")
	      .attr("class", "tooltip")
	      .style("opacity", 0);

	// elements for data join
	var link = svg.append("g").selectAll(".link"),
		node = svg.append("g").selectAll(".node");

	var options= new function(){
			this.time = time_choice_list[0];
			this.pulse = pulse_choice_list[0];
			this.link_strength = 0.5;
			this.link_stroke = 1.0;
			this.node_size_multiplier = 1.0;
			this.node_size_property = "num_source";
		}

	console.log(svg);


	gui_folder.add(options, 'time', time_choice_object )
	.onChange(function(Value) {
		remove();
		graph = data[options.time][options.pulse];
		update();
	  //bars.attr('height', config['height']);
	});

	gui_folder.add(options, 'pulse', pulse_choice_object )
	.onChange(function(Value) {
		remove();
		graph = data[options.time][options.pulse];
		update();
	  //bars.attr('height', config['height']);
	});

	gui_folder.add(options, 'link_strength', 0, 1 ).step(0.01)
	.onChange(function(Value) {
		inputted();
	  //bars.attr('height', config['height']);
	});

	gui_folder.add(options, 'link_stroke', 0, 5 ).step(0.1)
	.onChange(function(Value) {
		remove();
		update();
		//inputted();
	  //bars.attr('height', config['height']);
	});

	gui_folder.add(options, 'node_size_property', {"num source": "num_source", "num target":"num_target", "num both": "num_both"} )
	.name("node size property")
	.onChange(function(Value) {
		remove();
		update();
		//inputted();
	  //bars.attr('height', config['height']);
	});


	gui_folder.add(options, 'node_size_multiplier', 0, 5 ).step(0.1)
	.name("node size")
	.onChange(function(Value) {
		remove();
		update();
		//inputted();
	  //bars.attr('height', config['height']);
	});

	
	gui_folder.open();


	//	d3 color scheme
	

	//	simulation initialization
	var simulation = d3.forceSimulation()
	    .force("link", d3.forceLink().id(function(d) { return d.id; }).strength(function(d) { return d.value*0.01; }))
	    .force("charge", d3.forceManyBody())
	    .force("center", d3.forceCenter(width / 2, height / 2))

	//	button event handling
	d3.select("#switch-btn").on("click", function() {
		update();
	});

	//d3.select("input[type=range]").on("input", inputted);

	update();

	function remove(){
		link.remove();
		node.remove();
	}

	//	follow v4 general update pattern
	function update() {
		
		
		
		//link = link.data(firstLinks ? graph.links1 : graph.links2);
		link = link.data(graph.links);
		link.exit().remove();

	       
		/*link = svg.append("g")
	          .attr("class", "links")
	        .selectAll("line")
	        .data(graph.links)
	        .enter().append("line")
	          .attr("stroke-width", function(d) { return Math.sqrt(d.value) * options.link_stroke; })
	        .on("mouseover", mouseover_link)
	        .on("mouseout", mouseout_link);*/

	    link = svg.append("g")
	          .attr("class", "links")
	        .selectAll("line")
	        .data(graph.links)
            .enter()
            .append("svg:path")
            .attr("stroke-width", function(d) { return Math.sqrt(d.value) * options.link_stroke; })
            .attr('marker-end','url(#arrowhead)');

        link.style('fill', 'none')
  		.style('stroke', "grey");


		node = node.data(graph.nodes);

		// EXIT
		node.exit().remove();

		// ENTER
		node = svg.append("g")
	        .attr("class", "nodes")
	        .selectAll(".node")
	        .data(graph.nodes)
	        .enter().append("g")
	        .attr("class", "node")
	        .on("mouseover", mouseover_node)
	        .on("mouseout", mouseout_node)
	        .call(d3.drag()
	          .on("start", dragstarted)
	          .on("drag", dragged)
	          .on("end", dragended))
	        .on('dblclick',releasenode)
	        .on('mouseover.tooltip', mouseover_node_tooltip)
	        //.on('mouseover.fade', fade(0.1))
	        .on("mouseout.tooltip", function() {
	            tooltip.transition()
	              .duration(100)
	              .style("opacity", 0);
	          })
	        //.on('mouseout.fade', fade(1))
	          .on("mousemove", function() {
	            tooltip.style("left", (d3.event.pageX) + "px")
	              .style("top", (d3.event.pageY + 10) + "px");
	          });

	      node.append("circle")
	        //.attr("r", 5)
	        .attr("r", function(d) { 
	        	return 1 * options.node_size_multiplier * d[options.node_size_property]+1; 
	        })
	        .attr("fill", function(d) {return color(d.group);});

	      node.append("text")
	        .text(function(d) { return d.id; });

		//	Set nodes, links, and alpha target for simulation
		simulation
			.nodes(graph.nodes)
			.on("tick", ticked);

	  	simulation.force("link")
	          .links(graph.links);

	  	simulation.alphaTarget(0.3).restart();
	}
	//	drag event handlers
	function inputted() {
		simulation.force("link").strength(function(d) { return options.link_strength* d.value*0.1; });
		simulation.alpha(1).restart();
	}

	function dragstarted(d) {
      if (!d3.event.active) simulation.alphaTarget(0.3).restart();
      d.fx = d.x;
      d.fy = d.y;
    }

    function dragged(d) {
      d.fx = d3.event.x;
      d.fy = d3.event.y;
    }

    function dragended(d) {
      if (!d3.event.active) simulation.alphaTarget(0);
      //d.fx = null;
      //d.fy = null;
    }
    function releasenode(d) {
        d.fx = null;
        d.fy = null;
    }

	//	tick event handler (nodes bound to container)
	function ticked() {
		/*link
			.attr("x1", function(d) { return d.source.x; })
			.attr("y1", function(d) { return d.source.y; })
			.attr("x2", function(d) { return d.target.x; })
			.attr("y2", function(d) { return d.target.y; });*/

		/*link
			.attr("d", function(d) {
	        var dx = d.target.x - d.source.x,
	            dy = d.target.y - d.source.y,
	            dr = Math.sqrt(dx * dx + dy * dy);
	        var temp = "M" + 
	            d.source.x + "," + 
	            d.source.y + "A" + 
	            dr + "," + dr + " 0 0,1 " + 
	            d.target.x + "," + 
	            d.target.y;
	        console.log(temp);
	        return temp;
		    });*/
		link.attr("d", positionLink);
		node
			.attr("cx", function(d) { return d.x; })
			.attr("cy", function(d) { return d.y; })
			.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });


	}
	function positionLink(d) {

			var dx = d.target.x - d.source.x,
            dy = d.target.y - d.source.y,
            dr = Math.sqrt(dx * dx + dy * dy);
	        return "M" + 
	            d.source.x + "," + 
	            d.source.y + "A" + 
	            dr + "," + dr + " 0 0,1 " + 
	            d.target.x + "," + 
	            d.target.y;
			}


	function releasenode(d) {
	    d.fx = null;
	    d.fy = null;
	}

	function mouseover_node() {
		d3.select(this).select("circle").transition()
	      .duration(200)
	      .attr("r", function(d) { return 3 * options.node_size_multiplier * d[options.node_size_property]+1; });
	}

	function mouseout_node() {
		d3.select(this).select("circle").transition()
	      .duration(200)
	      .attr("r", function(d) { return 1 * options.node_size_multiplier * d[options.node_size_property]+1; });
	}

	function mouseover_node_tooltip(d) {
	    tooltip.transition()
	      .duration(300)
	      .style("opacity", .8);
	    tooltip.html("Name:" + d.id + "<p/>group:" + d.group)
	      .style("left", (d3.event.pageX) + "px")
	      .style("top", (d3.event.pageY + 10) + "px");
	}

	function mouseover_link() {
	  	d3.select(this).select("circle").transition()
	      .duration(200)
	      .attr("stroke-width", function(d) { return Math.sqrt(d.value*10); });
	}

	function mouseout_link() {
	  	d3.select(this).select("circle").transition()
	      .duration(200)
	      .attr("stroke-width", function(d) { return Math.sqrt(d.value); });
	}



}

function arrayToIdenticalObject(array){
	var result = {}
	for (var i = 0; i < array.length; i++) {
		result[array[i]] = array[i];
	}
	return result;
}

function addOptionBox(view){
	var tempGuiContainer = document.createElement('div');
		
	tempGuiContainer.style.position = 'absolute';
	tempGuiContainer.style.top = view.windowTop +1+ 'px';
	tempGuiContainer.style.left = view.windowLeft +1+ 'px';
	document.body.appendChild(tempGuiContainer);
	var tempGui = new dat.GUI( { autoPlace: false } );
	view.guiContainer = tempGuiContainer;
	view.gui = tempGui;

	tempGuiContainer.appendChild(tempGui.domElement);

}