

groupped_template = """


  pure_height = 600;



chart.append('text')
        .attr('class', 'title')
        .attr('x', (width / 2.5 ) + margin.left )
        .attr('y', 20)
        .attr('text-anchor', 'middle')
        .text('|title|')

chart.append('text')
        .attr('class', 'label')
        .attr('x', (width / 2))
        .attr('y', height + 50  )
        .attr('text-anchor', 'middle')
        .text('|group|')
        .style("font", "22px times")




  var data = |jsondata|

  var subgroups = |groups|

  var groups = d3.map(data, function(d){return(d.|group|)}).keys()


  var x = d3.scaleBand()
      .domain(groups)
      .range([0, width])
      .padding([0.2])
  chart.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x).tickSize(0));

  var y = d3.scaleLinear()
    .domain([0, 40])
    .range([ height, 0 ]);
  chart.append("g")
    .call(d3.axisLeft(y));

  var xSubgroup = d3.scaleBand()
    .domain(subgroups)
    .range([0, x.bandwidth()])
    .padding([0.05])


  var color = d3.scaleOrdinal()
    .domain(subgroups)
    .range(colorGroup)


var startY  =130;
var fixCircleX = 480;
var fixLegendTextX = 500

for (var i=0;i<subgroups.length;i++){

  svg.append("circle").attr("cx",fixCircleX).attr("cy",startY).attr("r", 6).style("fill", colorGroup[i])
  svg.append("text").attr("x", fixLegendTextX).attr("y", startY).text(subgroups[i]).style("font-size", "15px").attr("alignment-baseline","middle")
  startY = startY + 30

}


  // Show the bars
  chart.append("g")
    .selectAll("g")
    .data(data)
    .enter()
    .append("g")
      .attr("transform", function(d) { return "translate(" + x(d.|group|) + ",0)"; })
    .selectAll("rect")
    .data(function(d) { return subgroups.map(function(key) { return {key: key, value: d[key]}; }); })
    .enter().append("rect")
      .attr("x", function(d) { return xSubgroup(d.key); })
      .attr("y", function(d) { return y(d.value); })
      .attr("width", xSubgroup.bandwidth())
      .attr("height", function(d) { return height - y(d.value); })
      .attr("fill", function(d) { return color(d.key); });


      </script>
      </body>
      </html>

"""
