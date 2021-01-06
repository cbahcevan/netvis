
static_initial_part = """
<html lang="en">
    <head>
      <meta charset="UTF-8"/>
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      <meta http-equiv="X-UA-Compatible" content="ie=edge"/>
      <title>Pie Chart</title>
      <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">
      <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.min.js"></script>
      <script src="https://d3js.org/d3.v5.min.js"></script>
      <style>
"""



design_part = """
.container {
            width: 25%;
            margin: 25px auto;
        }
img {
            width: 100%;
            opacity: 0.3;

        }

"""


script_part = """

</style>
</head>
<body>
    <div class="container">
        <h2> |Title| </h2>
        <div>
            <canvas id="myChart"></canvas>
            <img src="https://raw.githubusercontent.com/cbahcevan/netvis/main/templates/logos/long-logo.png?token=AKHWOQ5O4UY5E2KUKFOKJ5S773KIG" alt = 'long-logo' style = "float:right;width:140px;height:40px;">

        </div>

    </div>
  <script>
    var ctx = document.getElementById("myChart").getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: |jsonLabelsData|,
        datasets: [{
        backgroundColor: |jsonColorsData|,
        data: |jsonValuesData|
        }]
    }
    });
  </script>
</body>
</html>

"""


script_part_without_logo = """

</style>
</head>
<body>
    <div class="container">
        <h2> |Title| </h2>
        <div>
            <canvas id="myChart"></canvas>
        </div>

    </div>
  <script>
    var ctx = document.getElementById("myChart").getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: |jsonLabelsData|,
        datasets: [{
        backgroundColor: |jsonColorsData|,
        data: |jsonValuesData|
        }]
    }
    });
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
