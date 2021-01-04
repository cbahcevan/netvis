initial_html = """
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <meta http-equiv="X-UA-Compatible" content="ie=edge"/>


  <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">
  <script src="https://d3js.org/d3.v5.min.js"></script>
  <style>
"""

#changing font colors using css rather than assigning attr to svg elements

css = """
body {
  font-family: 'Open Sans', sans-serif;
}

div#layout {
  text-align: center;
}

div#container {
  width: 1100px;
  height: 700px;
  margin: auto;
  background-color: |backgroundcolor|; //background-color of entire svg
}

svg {
  width: 100%;
  height: 100%;
}

text {
  font-size: 12px;
  fill: black;

}

path {
  stroke: gray;
}

.line {
  fill:none;
  stroke: orange;
  stroke-width: 2;
}


.grid path {
  stroke-width: 0;
}

.grid .tick line {
  stroke: white;
  stroke-opacity: 0.3;
}


text.value {
  font-size: 14px;
  fill: black;
}

text.title {
  font-size: 22px;
  font-weight: 600;
}

text.axis_title {
  font-size: 16px;
  font-weight: 400;
  fill: black;
}

text.source {
  font-size: 10px;
}
rect {
  fill: lightsteelblue; //background color of chart |chart-color|
}
</style>
</head>
<body>
  <div id='layout'>
    <div id='container'>
      <svg />
    </div>
  </div>


"""

d3_js = """
<script>

  var scatter_data = |jsondata|


  const svg = d3.select('svg')
  const svgContainer = d3.select('#container');

  var margin = {
    "left": 40,
    "right": 30,
    "top": 20,
    "bottom": 30
  };

  const width = 1000 - margin.left - margin.right;
  const height = 600 - margin.top - margin.bottom;


  var colors = d3.scaleOrdinal(d3.schemeCategory10);


  const chart = svg.append('g')
    .attr('transform',`translate(${margin.left + margin.right},${margin.top + margin.bottom})`)
    .attr('class','chart');

  var x = d3.scaleLinear()
      .domain(d3.extent(scatter_data, function(d) {
        return d.data_x;
      }))
      .range([0, width]);

  var y = d3.scaleLinear()
      .domain(d3.extent(scatter_data, function(d) {
        return d.data_y;
      }))
      .range([height, 0]);

  var x_axis = d3.axisBottom(x).tickPadding(5)

  var y_axis = d3.axisLeft(y).tickPadding(5)

  chart.append('rect')
        .attr('class','rect')
        .attr('width',width)
        .attr('height',height)

  chart.append('g')
    .attr('transform',`translate(0,${height})`)
    .call(x_axis)

  chart.append('g')
    .attr('transform',`translate(0,0)`)
    .call(y_axis)


  var data = chart.selectAll("g.node").data(scatter_data, function(d) {
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

  function make_x_gridlines () {
    return d3.axisBottom(x).ticks(5)
  }

  function make_y_gridlines () {
    return d3.axisLeft(y).ticks(5)
  }

  chart.append('g')
    .attr('class','grid')
    .call(make_y_gridlines()
          .tickSize(-width)
          .tickFormat("")
        )

  chart.append('g')
      .attr('class', 'grid')
      .attr("transform", "translate(0," + height + ")")
      .call(make_x_gridlines()
          .tickSize(-height)
          .tickFormat("")
      );

  chart.append('text')
    .attr('class','title')
    .attr('text-anchor','middle')
    .attr('x',width/2)
    .attr('y', -margin.top)
    .text('|title|')

  chart.append('text')
    .attr('class','axis_title')
    .attr('x',width/2)
    .attr('y',height + margin.top + margin.bottom)
    .attr('text-anchor','middle')
    .text('|xtitle|')

  chart.append('text')
      .attr('class','axis_title')
      .attr("transform","rotate(-90)")
      .attr('y', -margin.left)
      .attr('x', -height/2)
      .attr('text-anchor','middle')
      .text('|ytitle|')


  chart.append('svg:image')
      .attr('xlink:href','logos/white-long-logo.png')
      .attr('width',300)
      .attr('height',300)
      .attr('x',width/2 - 300/2)
      .attr('y',height/2 - 300/2)
      .attr('text-align','center')
      .style('opacity', 0.30)

  </script>
</body>
</html>

"""


additional_bottom_text = """
"""


horizontal_lines_part = """
"""


vertical_lines_part = """
"""
