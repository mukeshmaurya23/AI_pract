def Tower(n, source, destination, auxilary):
    if n == 1:
        print("moving disk 1 from", source, "destination", destination)
        return
    Tower(n-1, source, auxilary, destination)
    print("moving disk from ", n, "source",
          source, "from destination", destination)
    Tower(n-1, auxilary, destination, source)


n = 3
Tower(n, 'A', 'B', 'C')
