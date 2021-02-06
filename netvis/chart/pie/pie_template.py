
static_initial_part = """
<html>
    <head>
        <script src="//cdnjs.cloudflare.com/ajax/libs/d3/4.7.2/d3.min.js"></script>
        <script src="./netvis/chart/pie/d3pie.min.js"></script>

        <style>
            .content {
              max-width: 500px;
              margin: auto;
            }
            </style>

    </head>
    <body>

        <div class="content" id="pieChart"></div>
"""


design_part = """

"""


script_part = """

        <script>
            var pie = new d3pie("pieChart", {
                "header": {
                    "title": {
                        "text": "|Title|",
                        "fontSize": 24,
                        "font": "open sans"
                    },
                    "subtitle": {
                        "text": "|SubTopTitle|",
                        "color": "#999999",
                        "fontSize": 12,
                        "font": "open sans"
                    },
                    "titleSubtitlePadding": 9
                },
                "footer": {
                    "text": "|SubBottomTitle|",
                    "color": "#999999",
                    "fontSize": 10,
                    "font": "open sans",
                    "location": "bottom-center"
                },
                "size": {
                    "canvasWidth": 590,
                    "pieOuterRadius": "92%"
                },
                "data": {
                    "sortOrder": "value-desc",
                    "content": |jsonValuesData|
                },
                "labels": {
                    "outer": {
                        "format": "label-value1",
                        "pieDistance": 17
                    },
                    "mainLabel": {
                        "color": "#000000",
                        "fontSize": 11
                    },
                    "percentage": {
                        "color": "#ffffff",
                        "decimalPlaces": 0
                    },
                    "value": {
                        "color": "#000000",
                        "fontSize": 11
                    },
                    "lines": {
                        "enabled": true,
                        "color": "#d40c0c"
                    },
                    "truncation": {
                        "enabled": true
                    }
                },
                "effects": {
                    "pullOutSegmentOnClick": {
                        "effect": "linear",
                        "speed": 400,
                        "size": 8
                    }
                },
                "misc": {
                    "gradient": {
                        "enabled": true,
                        "percentage": 100
                    }
                },
                "callbacks": {}
            });

        </script>

    </body>
</html>
"""


additional_bottom_text = """
    
"""


horizontal_lines_part = """
   
"""
