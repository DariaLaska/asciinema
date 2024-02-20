
from asciinema import recorder
import wwrite_2


recorder.record(
        ("127.0.0.1", 5566),
        command = "ping -c 7 google.com", #echo 123
        writer = wwrite_2.DariasWriter


        )


