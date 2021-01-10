
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
  height: 600px;
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

   .title {
  font-size: 22px;
  font-weight: 600;
  }
  .text{
      font-size:14;
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


script_part = """
<script>

const sample =  |jsondata|


var margin = {top: 80, right: 30, bottom: 40, left: 100},
width = 700 - margin.left - margin.right,
height = 600 - margin.top - margin.bottom;
pure_height = 600;

const svg = d3.select("svg").attr("width", width + margin.left + margin.right)
                                    .attr("height", pure_height + margin.top + margin.bottom)



const chartArea = svg.append("g")
                .attr("transform","translate(" + margin.left + "," + margin.top + ")");

                                    
  
 svg.append('text')
        .attr('class', 'title')
        .attr('x', (width / 2 ) + margin.left )
        .attr('y', margin.top / 2)
        .attr('text-anchor', 'middle')
        .text('|title|')

svg.append('text')
        .attr('class', 'label')
        .attr('x', (width / 2) + margin.left )
        .attr('y', height + (margin.top + margin.bottom) + 20 )
        .attr('text-anchor', 'middle')
        .text('|xname|')
        .style("font", "22px times")
                                     
/*
svg.append('text')
        .attr('class', 'label')
        .attr('x', 0 )
        .attr('y', pure_height / 2 )
        .attr('text-anchor', 'middle')
        .text('Y ekseni')
        .attr('transform','rotate(271)')
        .style("font", "22px times");
 */


const xScale = d3.scaleLinear()
                 .range([0,600])
                 .domain([0,d3.max(sample, (d) => Number(d.Nufus))]);

/*

*/
chartArea.append("g").attr("transform", "translate(0," + height + ")")
                .call(d3.axisBottom(xScale))
                .style("font", "15px times")
                .selectAll("text")
                .attr("transform", "translate(-10,0)rotate(-45)")
                .style("text-anchor", "end")



const yScale = d3.scaleBand()
                  .range([0,500])
                  .domain(sample.map(function(d) { return d.|yname|; }))
                  .padding(0.2)

chartArea.append("g").style("font", "15px times").call(d3.axisLeft(yScale));


const barGroups = chartArea.selectAll("bars")
        .data(sample)
        .enter()
        .append("g")

barGroups.append("rect")
        .attr("x",xScale(0))
        .attr("y", function(d) { return yScale(d.|yname|); })
        .attr("width", function(d) { return xScale(d.|xname|); })
        .attr("height",yScale.bandwidth)
        .attr("fill", "#5F89AD");




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
    chart.append('g')
      .attr('class', 'grid')
      .call(makeYLines()
        .tickSize(-width, 0, 0)
        .tickFormat(''))
"""


vertical_lines_part = """
        chart.append('g')
       .attr('class', 'grid')
       .attr('transform', `translate(0, ${height})`)
       .call(makeXLines()
         .tickSize(-height, 0, 0)
         .tickFormat('')
       )
"""
