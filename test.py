from ws2812 import WS2812

chain = WS2812( ledNumber=16, brightness=100 )
data = [(255, 102, 0), (127, 21, 0), (63, 10, 0), (31, 5, 0),
        (15, 2, 0), (7, 1, 0), (0, 0, 0), (0,0,0),
        (0, 0, 0), (0, 0, 0), (0, 0, 0), (0,0,0),
        (0, 0, 0), (0, 0, 0), (0, 0, 0), (0,0,0)
       ]
chain.show( data )


while True:
    data = data[1:] + data[0:1]
    chain.show( data )
    time.sleep_ms( 150 )
