from matplotlib import pyplot as plt


#class definitions

class PointLoad:
   def __init__(self, order, location, magnitude):
      self.order = order
      self.location = location
      self.magnitude = magnitude

class DistLoad:
   def __init__(self, order, location, force_per_distance, distance):
      self.order = order
      self.location = location
      self.force_per_distance = force_per_distance
      self.distance = distance


def main():
   print('Welcome to Aidan\'s beam analysis tool. :)\nLet\'s get started...')
   length, num_forces = get_info()
   list_forces = create_classes(num_forces)
   x, y = get_sheer_coords(list_forces)  
   plt.plot(x,y)
   plt.xlabel('X (Meters)')
   plt.ylabel('V (Newtons)')
   plt.title('Sheer Diagram')
   plt.show()


   




def get_info():
   while True:
    try:
        length =  float(input('How long is your beam?'))
        print()
        break
    except: ValueError
   num_forces = int(input('How many forces area applied to your beam? (Please include reactions)'))
   print()
   return(length, num_forces)


def create_classes(num_forces):
    list_forces = []
    print('Enter forces in order from left to right.\nAssign upward forces positive magnitudes, and downward forces negative magnitudes.\nUse SI units.')
    for i in range(num_forces):
       print(f'FORCE {i+1}: ')
       force_type = input('Point or distributed? (p or d)\t')
       if force_type == 'p':
          ord = i+1
          loc = float(input('Enter distance between left end of beam and point force. (m)\t'))
          mag = float(input('Enter magnitude of force. (N)\t'))
          list_forces.append(PointLoad(ord, loc, mag))
       if force_type == 'd':
          ord = i+1
          loc = float(input('Enter distance between left end of beam and beginning of distributed force. (m)\t'))
          dist = float(input('Enter distance between beginnng of distributed force application, and end of distributed force application. (m)\t'))
          fpd = float(input('Enter force per distance. (N/m)\t'))
          list_forces.append(DistLoad(ord, loc, fpd, dist))
       print()
    return(list_forces)


def get_sheer_coords(list_forces):
   x = [0]
   y = [0]
   for force in list_forces:
      if isinstance(force, PointLoad):
         x.append(force.location)
         y.append(y[-1])
         x.append(force.location)
         y.append(force.magnitude + y[-1])
      if isinstance(force, DistLoad):
         x.append(force.location)
         y.append(y[-1])
         x.append(force.location +force.distance)
         y.append(y[-1] + force.force_per_distance * force.distance)

   return x, y
      
   




if __name__ == "__main__":
   main()




