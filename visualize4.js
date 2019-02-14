console.log('starting');
var uploader = document.getElementById("uploader");
var uploader_wrapper = document.getElementById("uploader_wrapper");

var controller_wrapper = document.getElementById("controller_wrapper");
var link_strength_controller = document.getElementById("link_strength_controller");


uploader.addEventListener("change", handleFiles, false);

function handleFiles() {
    var file = this.files[0];
    console.log(file);
    console.log(this);
    uploader.parentNode.removeChild(uploader);
    uploader_wrapper.parentNode.removeChild(uploader_wrapper);
    controller_wrapper.style.display = "block";
    main(file.path);
    
}

function main(filename) {

	var views = [];

	var margin = {top: 30, right: 20, bottom: 30, left: 50},
	width = 500 - margin.left - margin.right,
	height = 500 - margin.top - margin.bottom;

	//	svg and sizing
	var svg_left = d3.select("body")
	.append("svg")
	  .attr("width", width + margin.left + margin.right)
	  .attr("height", height + margin.top + margin.bottom)
	.append("g")
	  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	views.push(svg_left);

	// Adds the svg canvas
	var svg_right = d3.select("body")
	.append("svg")
	  .attr("width", width + margin.left + margin.right)
	  .attr("height", height + margin.top + margin.bottom)
	.append("g")
	  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	views.push(svg_right);
	//	graph data store
	//var data;
	
	d3.json(filename, function(err, data) {
		if (err) throw err;
		//console.log("link");
		//console.log(link);
		//data = g;
		//graph = data["0.00867999999999999"]["192"];

		//console.log(graph);
		//update();
		add_one_graph(views, svg_left,  width, height, data, "0.00867999999999999", "192");
		add_one_graph(views, svg_right, width, height, data, "0.00867999999999999", "63");
		console.log(views);
		//add_one_graph(svg_right,width, height, data);
		//console.log("read_data");
		//callback(null);
	});


	

}


function add_one_graph(views, svg,width, height, data, time, pulse){
	var view;
	views.push(view);
	var time, pulse;
	var time_list = [], pulse_list = [];
	var graph;

	graph = data[time][pulse];
	

	//	d3 color scheme
	var color = d3.scaleOrdinal(d3.schemeCategory10);

	var tooltip = d3.select("body")
	      .append("div")
	      .attr("class", "tooltip")
	      .style("opacity", 0);

	// elements for data join
	var link = svg.append("g").selectAll(".link"),
		node = svg.append("g").selectAll(".node");

	//	simulation initialization
	var simulation = d3.forceSimulation()
	    .force("link", d3.forceLink().id(function(d) { return d.id; }).strength(0.5))
	    .force("charge", d3.forceManyBody())
	    .force("center", d3.forceCenter(width / 2, height / 2))

	//	button event handling
	d3.select("#switch-btn").on("click", function() {
		update();
	});

	d3.select("input[type=range]").on("input", inputted);

	update();


	//	follow v4 general update pattern
	function update() {
		console.log("link update");
		console.log(link);
		
		//link = link.data(firstLinks ? graph.links1 : graph.links2);
		link = link.data(graph.links);
		link.exit().remove();

		link = svg.append("g")
	          .attr("class", "links")
	        .selectAll("line")
	        .data(graph.links)
	        .enter().append("line")
	          .attr("stroke-width", function(d) { return Math.sqrt(d.value); })
	        .on("mouseover", mouseover_link)
	        .on("mouseout", mouseout_link);


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
	        .attr("r", function(d) { return 5; })
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
		simulation.force("link").strength(+this.value);
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
		link
			.attr("x1", function(d) { return d.source.x; })
			.attr("y1", function(d) { return d.source.y; })
			.attr("x2", function(d) { return d.target.x; })
			.attr("y2", function(d) { return d.target.y; });

		node
			.attr("cx", function(d) { return d.x; })
			.attr("cy", function(d) { return d.y; })
			.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
	}


	function releasenode(d) {
	    d.fx = null;
	    d.fy = null;
	}

	function mouseover_node() {
		d3.select(this).select("circle").transition()
	      .duration(200)
	      .attr("r", function(d) { return 15; });
	}

	function mouseout_node() {
		d3.select(this).select("circle").transition()
	      .duration(200)
	      .attr("r", function(d) { return 5; });
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

function iterationCopy(src) {
  let target = {};
  for (let prop in src) {
    if (src.hasOwnProperty(prop)) {
      target[prop] = src[prop];
    }
  }
  return target;
}