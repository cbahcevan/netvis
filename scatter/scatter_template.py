initial_html = """<html lang="en">
<head>
  <meta charset="UTF-8"/>

    <script src="https://d3js.org/d3.v5.min.js"></script>

  <div id="scatter-load"></div>


    <style>
"""

css = """
body {
    font-family:"Helvetica Neue";
    color: #686765;
}

div#layout {
  text-align: center;
}

div#container {
  width: 1000px;
  height: 600px;
  margin:auto;
  background-color: |backgroundcolor|;
}

svg {
  width: 100%;
  height: 100%;
}

.name {
    float:right;
    color:#27aae1;
}
.axis {
    fill: none;
    stroke: #AAA;
    stroke-width: 1px;
}
text {
    stroke: none;
    fill: #666666;
    font-size: .6em;
    font-family:"Helvetica Neue"
}
.label {
    fill: #414241;
}
.node {
    cursor:pointer;
}
.dot {
    opacity: .7;
    cursor: pointer;
}
g {
  font-size: 18px
}

</style>
"""

d3_js = """
</head>
<body>
    <div id="scatter-load"></div>
  <script>
    var sample_data = |formatted_data|

showScatterPlot(sample_data);

function showScatterPlot(data) {
  var margins = {
    "left": 60,
    "right": 30,
    "top": 30,
    "bottom": 30
  };

  var width = 800;
  var height = 800;

  var colors = d3.scaleOrdinal(d3.schemeCategory10);

  var svg = d3.select("#scatter-load").append("svg").attr("width", width).attr("height", height).append("g")
    //.attr("transform", "translate(" + margins.left + "," + margins.top + ")");
      .attr("transform", "translate(80,80)");

  var x = d3.scaleLinear()
    .domain(d3.extent(data, function(d) {
      return d.data_x;
    }))
    .range([0, width - margins.left - margins.right]);

  var y = d3.scaleLinear()
    .domain(d3.extent(data, function(d) {
      return d.data_y;
    }))
    .range([height - margins.top - margins.bottom - 20, 0]);

  svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + y.range()[0] + ")")

  svg.append("g")
  .attr("class", "y axis");

  svg.append("text")
    .attr("fill", "#414241")
    .style('font-size','16px')
    .style("text-anchor", "middle")
    .attr("x", width / 2)
    .attr("y", height - 30)
    .text("|xtitle|");

  svg.append("text")
    .attr("transform","rotate(-90)")
    .attr("fill", "#414241")
    .style('font-size','16px')
    .style("text-anchor", "middle")
    .attr("x", -height/2 + 40)
    .attr("y", -30)
    .text("|ytitle|");

  svg.append('text')
    .text('|title|')
    .attr('x',width/2)
    .attr('y', -margins.top)
    .style('font-size','24px')
    .style('fill','|titlecolor|')
    .style("text-anchor", "middle");


  var xAxis = d3.axisBottom(x).tickPadding(2);
  var yAxis = d3.axisLeft(y).tickPadding(2);

  svg.selectAll("g.y.axis").call(yAxis);
  svg.selectAll("g.x.axis").call(xAxis);

  var data = svg.selectAll("g.node").data(data, function(d) {
    return d.name;
  });


  var dataGroup = data.enter().append("g").attr("class", "node")
    .attr('transform', function(d) {
      return "translate(" + x(d.data_x) + "," + y(d.data_y) + ")";
    });

  dataGroup.append("circle")
    .attr("r", 2.5)
    .attr("class", "dot")
    .style("fill", function(d) {
      return colors(d.type);
    });

//  dataGroup.append("text")
//    .style("text-anchor", "middle")
//    .attr("dy", -10)
//    .text(function(d) {
//      return d.name;
//    });
}



</script>
</body>
</html>
"""



horizontal_lines_part = """
    svg.append('g')
      .attr('class', 'grid')
      .call(makeYLines()
        .tickSize(-width, 0, 0)
        .tickFormat(''))
"""


vertical_lines_part = """
        svg.append('g')
       .attr('class', 'grid')
       .attr('transform', `translate(0, ${height})`)
       .call(makeXLines()
         .tickSize(-height, 0, 0)
         .tickFormat('')
       )
"""
