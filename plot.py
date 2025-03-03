# Import
import matplotlib.pyplot as plt

class specPlot():
    def __init__(self, pathname):
        self.pathname = pathname
        self.wavenumber, self.counts = self.readtxt()
    
    def readtxt(self):
        f = open(self.pathname, 'r') #read txt file
        lines = f.readlines() # reads line per line and stores it in lines variable
        wavenumber = []
        counts = []
        for line in lines[1:]:  # not including header
            parts = line.split()  # split by whitespace
            wavenumber.append(float(parts[0]))
            counts.append(float(parts[1]))
        f.close()
        return wavenumber, counts
    
    def plot(self):
        plt.plot(self.wavenumber, self.counts, linewidth=1)
        plt.title("Raman spectrum")  
        plt.xlabel("Wavenumber")
        plt.ylabel("Counts")
        plt.show()

specPlot('pathname as a string').plot()