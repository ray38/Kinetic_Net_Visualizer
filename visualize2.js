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



    var tooltip = d3.select("body")
      .append("div")
      .attr("class", "tooltip")
      .style("opacity", 0);

    var svg = d3.select("svg"),
        width = +svg.attr("width"),
        height = +svg.attr("height");
    var color = d3.scaleOrdinal(d3.schemeCategory20);


    var simulation = d3.forceSimulation()
        .force("link", d3.forceLink().id(function(d) { return d.id; }).strength(0.5))
        .force("charge", d3.forceManyBody())
        .force("center", d3.forceCenter(width / 2, height / 2))
        // .alphaDecay(0);

    d3.select("input[type=range]")
        .on("input", inputted);

    d3.json(filename, function(error, graph) {
      if (error) throw error;

      var link = svg.append("g")
          .attr("class", "links")
        .selectAll("line")
        .data(graph.links)
        .enter().append("line")
          .attr("stroke-width", function(d) { return Math.sqrt(d.value); })
        .on("mouseover", mouseover_link)
        .on("mouseout", mouseout_link);

      var node = svg.append("g")
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
        .on('mouseover.fade', fade(0.1))
        .on("mouseout.tooltip", function() {
            tooltip.transition()
              .duration(100)
              .style("opacity", 0);
          })
        .on('mouseout.fade', fade(1))
          .on("mousemove", function() {
            tooltip.style("left", (d3.event.pageX) + "px")
              .style("top", (d3.event.pageY + 10) + "px");
          });

      node.append("circle")
        //.attr("r", 5)
        .attr("r", function(d) { return d.r; })
        .attr("fill", function(d) { 
          if (d.group==1) {return "blue";}
          else {return "grey";}
        });

      node.append("text")
        .text(function(d) { 
          if (d.group==1) {return d.id;}
          else {return "";}
        });




      simulation
          .nodes(graph.nodes)
          .on("tick", ticked);

      simulation.force("link")
          .links(graph.links);

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


      function fade(opacity) {
        return d => {
          node.style('stroke-opacity', function (o) {
            const thisOpacity = isConnected(d, o) ? 1 : opacity;
            this.setAttribute('fill-opacity', thisOpacity);
            return thisOpacity;
          });

          link.style('stroke-opacity', o => (o.source === d || o.target === d ? 1 : opacity));

        };
      }

      function isConnected(a, b) {
        return linkedByIndex[`${a.index},${b.index}`] || linkedByIndex[`${b.index},${a.index}`] || a.index === b.index;
      }

      const linkedByIndex = {};
      graph.links.forEach(d => {
        linkedByIndex[`${d.source.index},${d.target.index}`] = 1;
      });
    });


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

    function mouseover_node() {
      d3.select(this).select("circle").transition()
          .duration(200)
          .attr("r", function(d) { return d.r*3; });
    }

    function mouseout_node() {
      d3.select(this).select("circle").transition()
          .duration(200)
          .attr("r", function(d) { return d.r; });
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