
static_initial_part = """
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <meta http-equiv="X-UA-Compatible" content="ie=edge"/>


  <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">
  <script src="https://d3js.org/d3.v5.min.js"></script>
  <style>
"""



design_part = """
body {
  font-family: 'Open Sans', sans-serif;
}

div#layout {
  text-align: center;
}

div#container {
  width: 1000px;
  height: 700px;
  margin: auto;
  background-color: |backgroundcolor|;
}

svg {
  width: 100%;
  height: 100%;
}

.bar {
  fill: |barcolor|;
}

text {
  font-size: 12px;
  fill: |textcolor|;
}

path {
  stroke: gray;
}

line {
  stroke: gray;
}

line#limit {
  stroke: #FED966;
  stroke-width: 3;
  stroke-dasharray: 3 6;
}

.grid path {
  stroke-width: 0;
}

.grid .tick line {
  stroke: #000;
  stroke-opacity: 0.3;
}

text.divergence {
  font-size: 14px;
  fill: #2F4A6D;
}

text.value {
  font-size: 14px;
}

text.title {
  font-size: 22px;
  font-weight: 600;
}

text.label {
  font-size: 14px;
  font-weight: 400;
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

"""

d3_dark = """
<script>

 const svg = d3.select('svg')
 const svgContainer = d3.select('#container');

  var margin = {
    "left": 40,
    "right": 30,
    "top": 20,
    "bottom": 30
  };

  const width = 780 - margin.left - margin.right;
  const height = 508 - margin.top - margin.bottom;

  const chartArea = svg.append('g')
    .attr('transform',`translate(${margin.left + margin.right},${margin.top + margin.bottom})`)
    .attr('class','chart');

  chartArea.append('rect')
        .style('fill','lightslategrey')
        .attr('width',width)
        .attr('height',height)


  chartArea.append('svg:image')
        //.attr('xlink:href','https://raw.githubusercontent.com/cbahcevan/netvis/main/templates/logos/white-long-logo.png?token=AKHWOQ2ZBD3KJLVYZZANV2LABV5AM' )
        .attr('width',300)
        .attr('height',300)
        .attr('x',width/2 - 300/2)
        .attr('y',height/2 - 300/2)
        .attr('text-align','center')
        .style('opacity', 0.30)

  const colorGroup = ['#ffa600','#ff6349','#ff2185']

"""

d3_light = """
<script>

 const svg = d3.select('svg')
 const svgContainer = d3.select('#container');

  var margin = {
    "left": 40,
    "right": 30,
    "top": 20,
    "bottom": 30
  };

  const width = 780 - margin.left - margin.right;
  const height = 520 - margin.top - margin.bottom;

  const chartArea = svg.append('g')
    .attr('transform',`translate(${margin.left + margin.right},${margin.top + margin.bottom})`)
    .attr('class','chart');

  chartArea.append('rect')
        .style('fill','white')
        .attr('width',width)
        .attr('height',height)


  chartArea.append('svg:image')
        //.attr('xlink:href','https://raw.githubusercontent.com/cbahcevan/netvis/main/templates/logos/white-long-logo.png?token=AKHWOQ2ZBD3KJLVYZZANV2LABV5AM' )
        .attr('width',300)
        .attr('height',300)
        .attr('x',width/2 - 300/2)
        .attr('y',height/2 - 300/2)
        .attr('text-align','center')
        .style('opacity', 0.30)

  const colorGroup = ['#e41a1c','#377eb8','#4daf4a','#984ea3','#ff7f00','#ffff33','#a65628','#f781bf','#999999']
"""

d3_blue = """
<script>

 const svg = d3.select('svg')
 const svgContainer = d3.select('#container');

  var margin = {
    "left": 40,
    "right": 30,
    "top": 20,
    "bottom": 30
  };

  const width = 780 - margin.left - margin.right;
  const height = 508 - margin.top - margin.bottom;

  const chartArea = svg.append('g')
    .attr('transform',`translate(${margin.left + margin.right},${margin.top + margin.bottom})`)
    .attr('class','chart');

  chartArea.append('rect')
        .style('fill','steelblue')
        .attr('width',width)
        .attr('height',height)


  chartArea.append('svg:image')
        //.attr('xlink:href','https://raw.githubusercontent.com/cbahcevan/netvis/main/templates/logos/white-long-logo.png?token=AKHWOQ2ZBD3KJLVYZZANV2LABV5AM' )
        .attr('width',300)
        .attr('height',300)
        .attr('x',width/2 - 300/2)
        .attr('y',height/2 - 300/2)
        .attr('text-align','center')
        .style('opacity', 0.30)

  const colorGroup = ['#ffa600','#ff6361','#bc5090','#984ea3','#58508d']
 """


d3_paper = """
<script>

 const svg = d3.select('svg')
 const svgContainer = d3.select('#container');

  var margin = {
    "left": 40,
    "right": 30,
    "top": 20,
    "bottom": 30
  };

  const width = 780 - margin.left - margin.right;
  const height = 520   - margin.top - margin.bottom;

  const chartArea = svg.append('g')
    .attr('transform',`translate(${margin.left + margin.right},${margin.top + margin.bottom})`)
    .attr('class','chart');

  chartArea.append('rect')
        .style('fill','LemonChiffon')
        .attr('width',width)
        .attr('height',height)


  chartArea.append('svg:image')
        //.attr('xlink:href','https://raw.githubusercontent.com/cbahcevan/netvis/main/templates/logos/white-long-logo.png?token=AKHWOQ2ZBD3KJLVYZZANV2LABV5AM' )
        .attr('width',300)
        .attr('height',300)
        .attr('x',width/2 - 300/2)
        .attr('y',height/2 - 300/2)
        .attr('text-align','center')
        .style('opacity', 0.30)

  const colorGroup = ['#ff2626','#2965ff','#000000','#984ea3','#2b8f10']
"""



script_part = """


    const sample =  |jsondata|

    

    const xScale = d3.scaleBand()
      .range([0, width])
      .domain(sample.map((s) => s.|xname|))
      .padding(0.4)

    const yScale = d3.scaleLinear()
      .range([height, 0])
      .domain([0, |maxy|]);

    // vertical grid lines
     const makeXLines = () => d3.axisBottom()
       .scale(xScale)

    const makeYLines = () => d3.axisLeft()
      .scale(yScale)

    chartArea.append('g')
      .attr('transform', `translate(0, ${height})`)
      .call(d3.axisBottom(xScale))
      |rotationtext|;


    chartArea.append('g')
      .call(d3.axisLeft(yScale));

    |verticallinepart|

    |horizontallinepart|

    const barGroups = chartArea.selectAll()
      .data(sample)
      .enter()
      .append('g')

    barGroups
      .append('rect')
      .attr('class', 'bar')
      .attr('x', (g) => xScale(g.|xname|))
      .attr('y', (g) => yScale(g.|yname|))
      .attr('height', (g) => height - yScale(g.|yname|))
      .attr('width', xScale.bandwidth())
      .on('mouseenter', function (actual, i) {
        d3.selectAll('.|yname|')
          .attr('opacity', 0.8)

        d3.select(this)
          .transition()
          .duration(300)
          .attr('opacity', 0.6)
          .attr('x', (a) => xScale(a.|xname|) - 5)
          .attr('width', xScale.bandwidth() + 10)

        const y = yScale(actual.|yname|)

        line = chartArea.append('line')
          .attr('id', 'limit')
          .attr('x1', 0)
          .attr('y1', y)
          .attr('x2', width)
          .attr('y2', y)

        barGroups.append('text')
          .attr('class', 'divergence')
          .attr('x', (a) => xScale(a.|xname|) + xScale.bandwidth() / 2)
          .attr('y', (a) => yScale(a.|yname|) + 30)
          .attr('fill', 'white')
          .attr('text-anchor', 'middle')
          .text((a, idx) => {
            const divergence = (a.|yname| - actual.|yname|).toFixed(1)

            let text = ''
            if (divergence > 0) text += '+'
            text += `${divergence}%`

            return idx !== i ? text : '';
          })

      })
      .on('mouseleave', function () {
        d3.selectAll('.|yname|')
          .attr('opacity', 1)

        d3.select(this)
          .transition()
          .duration(300)
          .attr('opacity', 1)
          .attr('x', (a) => xScale(a.|xname|))
          .attr('width', xScale.bandwidth())

        chartArea.selectAll('#limit').remove()
        chartArea.selectAll('.divergence').remove()
      })

    barGroups
      .append('text')
      .attr('class', '|yname|')
      .attr('x', (a) => xScale(a.|xname|) + xScale.bandwidth() / 2)
      .attr('y', (a) => yScale(a.|yname|) + 30)
      .attr('text-anchor', 'middle')
      .text((a) => `${a.|yname|}`)//percentage

svg.append('text')
        .attr('class', 'label')
        .attr("x", - (width / 2)  )
        .attr("y", 15)
        .attr('text-anchor', 'middle')
        .text('|ytitle|')
        .attr("transform", "rotate(-90)")
        .style("font", "22px times");


    svg.append('text')
      .attr('class', 'label')
      .attr('x', width / 2 )
      .attr('y', height + 100 )
      .attr('text-anchor', 'middle')
      .style("font", "22px times")
      .text('|xtitle|')

    svg.append('text')
      .attr('class', 'title')
      .attr('x', width / 2)
      .attr('y', 40)
      .attr('text-anchor', 'middle')
      .text('|title|')
      .style('fill','|titlecolor|')

    chartArea.append('svg:image')
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
    svg.append('text')
      .attr('class', 'source')
      .attr('x', width - margin / 2)
      .attr('y', height + margin * 1.7)
      .attr('text-anchor', 'start')
      .text('|bottomtext|')
"""


horizontal_lines_part = """
    chartArea.append('g')
      .attr('class', 'grid')
      .call(makeYLines()
        .tickSize(-width, 0, 0)
        .tickFormat(''))
"""


vertical_lines_part = """
        chartArea.append('g')
       .attr('class', 'grid')
       .attr('transform', `translate(0, ${height})`)
       .call(makeXLines()
         .tickSize(-height, 0, 0)
         .tickFormat('')
       )
"""

text_rotation = """
      .selectAll("text")
      .attr('text-anchor', 'start')
      .attr("x", 5)
      .attr("transform", "rotate(45)");
"""
