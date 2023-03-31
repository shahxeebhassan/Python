import sys
import cowsay


if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])

if len(sys.argv) == 3:
    cowsay.trex("hello, " + sys.argv[1] + sys.argv[2])

