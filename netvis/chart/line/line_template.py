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


css = """
body {
  font-family: 'Open Sans', sans-serif;
}

div#layout {
  text-align: center;
}

div#container {
  width: 800px;
  height: 600px;
  margin: auto;
}

svg {
  width: 100%;
  height: 100%;
}

text {
  font-size: 12px;
  fill: |text-color|;
}
.axis line{
  stroke: black;
}

.grid path {
  stroke: none;
}

.grid .tick line {
  stroke: |grid-line|;
  stroke-opacity: 0.3;
}

text.value {
  font-size: 14px;
  fill: |text-color|;
}

text.title {
  font-size: 22px;
  font-weight: 600;
  fill: |text-color|;

}

text.axis_title {
  font-size: 16px;
  font-weight: 400;
  fill: |text-color|;
}

text.source {
  font-size: 10px;
}

</style>
</head>
<body>
  <div id='layout'>
    <div id='container'>
      <svg />
    </div>
  </div>
<script>
"""





#------------------------------------Themes------------------------------------
d3_dark = """

  const svg = d3.select('svg')
  const svgContainer = d3.select('#container');

  var margin = {
    "left": 40,
    "right": 30,
    "top": 20,
    "bottom": 30
  };

  const width = 780 - margin.left - margin.right;
  const height = 468 - margin.top - margin.bottom;

  const chart = svg.append('g')
    .attr('transform',`translate(${margin.left + margin.right},${margin.top + margin.bottom})`)
    .attr('class','chart');

  chart.append('rect')
        .style('fill','lightslategrey')
        .attr('width',width)
        .attr('height',height)

  chart.append('svg:image')
        .attr('xlink:href','https://raw.githubusercontent.com/cbahcevan/netvis/main/templates/logos/white-long-logo.png?token=AKHWOQ2ZBD3KJLVYZZANV2LABV5AM' )
        .attr('width',300)
        .attr('height',300)
        .attr('x',width/2 - 300/2)
        .attr('y',height/2 - 300/2)
        .attr('text-align','center')
        .style('opacity', 0.30)
  const color_palette = ['#ffa600','#ff6349','#ff2185']
"""

d3_light = """

  const svg = d3.select('svg')
  const svgContainer = d3.select('#container');

  var margin = {
    "left": 40,
    "right": 30,
    "top": 20,
    "bottom": 30
  };

  const width = 780 - margin.left - margin.right;
  const height = 468 - margin.top - margin.bottom;

  const chart = svg.append('g')
    .attr('transform',`translate(${margin.left + margin.right},${margin.top + margin.bottom})`)
    .attr('class','chart');

  chart.append('rect')
        .style('fill','white')
        .attr('width',width)
        .attr('height',height)

  chart.append('svg:image')
        .attr('xlink:href','https://raw.githubusercontent.com/cbahcevan/netvis/main/templates/logos/long-logo.png?token=AKHWOQ62L3DTTIRURF2UG5DABWBBS' )
        .attr('width',300)
        .attr('height',300)
        .attr('x',width/2 - 300/2)
        .attr('y',height/2 - 300/2)
        .attr('text-align','center')
        .style('opacity', 0.30)
  const color_palette = ['#e41a1c','#377eb8','#4daf4a','#984ea3','#ff7f00','#ffff33','#a65628','#f781bf','#999999']

"""


d3_blue = """

  const svg = d3.select('svg')
  const svgContainer = d3.select('#container');

  var margin = {
    "left": 40,
    "right": 30,
    "top": 20,
    "bottom": 30
  };

  const width = 780 - margin.left - margin.right;
  const height = 468 - margin.top - margin.bottom;

  const chart = svg.append('g')
    .attr('transform',`translate(${margin.left + margin.right},${margin.top + margin.bottom})`)
    .attr('class','chart');

  chart.append('rect')
        .style('fill','steelblue')
        .attr('width',width)
        .attr('height',height)

  chart.append('svg:image')
        .attr('xlink:href','https://raw.githubusercontent.com/cbahcevan/netvis/main/templates/logos/white-long-logo.png?token=AKHWOQ2ZBD3KJLVYZZANV2LABV5AM')
        .attr('width',300)
        .attr('height',300)
        .attr('x',width/2 - 300/2)
        .attr('y',height/2 - 300/2)
        .attr('text-align','center')
        .style('opacity', 0.30)
  const color_palette = ['#ffa600','#ff6361','#bc5090','#984ea3','#58508d']

"""

d3_paper = """

  const svg = d3.select('svg')
  const svgContainer = d3.select('#container');

  var margin = {
    "left": 40,
    "right": 30,
    "top": 20,
    "bottom": 30
  };

  const width = 780 - margin.left - margin.right;
  const height = 468 - margin.top - margin.bottom;

  const chart = svg.append('g')
    .attr('transform',`translate(${margin.left + margin.right},${margin.top + margin.bottom})`)
    .attr('class','chart');

  chart.append('rect')
        .style('fill','LemonChiffon')
        .attr('width',width)
        .attr('height',height)

  chart.append('svg:image')
        .attr('xlink:href','https://raw.githubusercontent.com/cbahcevan/netvis/main/templates/logos/gray-long-logo.png?token=AKHWOQ4NQYG74M2DXLPTJ23ABWQNE')
        .attr('width',300)
        .attr('height',300)
        .attr('x',width/2 - 300/2)
        .attr('y',height/2 - 300/2)
        .attr('text-align','center')
        .style('opacity', 0.30)
  const color_palette = ['#000000','#ff2626','#2965ff','#984ea3','#2b8f10']

"""




#-------------------------------------------------------------------------------





d3_js = """

  const line_data = |jsondata|
  var line_nest = d3.nest()
    .key(function(d) {
        return d.type;
    })
    .entries(line_data)



  var x = d3.scaleLinear().range([0, width]);

  var y = d3.scaleLinear().range([height, 0]);

  x.domain(d3.extent(line_data, function(d) {
          return d.data_x;
        }))

  y.domain([0, d3.max(line_data, function(d) {
          return +d.data_y;
        })])


  var x_axis = d3.axisBottom(x).tickPadding(2);

  var y_axis = d3.axisLeft(y).tickPadding(2)


  chart.append('g')
    .attr('transform',`translate(0,${height})`)
    .attr('class','axis')
    .call(x_axis)

  chart.append('g')
    .attr('transform',`translate(0,0)`)
    .attr('class','axis')
    .call(y_axis)

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


  var res = line_nest.map(function(d) {return d.key})
  var color = d3.scaleOrdinal().domain(res).range(color_palette)


  chart.selectAll('.line').data(line_nest).enter()
      .append("path")
      .attr('fill','none')
      .attr('stroke', function(d) {return color(d.key)})
      .attr("d", function(d){
             return d3.line()
               .x(function(d) { return x(d.data_x); })
               .y(function(d) { return y(+d.data_y); })
               (d.values)
           })


  </script>
</body>
</html>


"""
