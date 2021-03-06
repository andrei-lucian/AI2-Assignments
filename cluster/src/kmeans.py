import random
"""kmeans.py"""

class Cluster:
    """This class represents the clusters, it contains the
    prototype (the mean of all it's members) and memberlists with the
    ID's (which are Integer objects) of the datapoints that are member
    of that cluster. You also want to remember the previous members so
    you can check if the clusters are stable."""
    def __init__(self, dim):
        self.prototype = [0.0 for _ in range(dim)]
        self.current_members = set()
        self.previous_members = set()


class KMeans:
    def __init__(self, k, traindata, testdata, dim):
        self.traindata = traindata
        self.testdata = testdata
        self.dim = dim

        # Threshold above which the corresponding html is prefetched
        self.prefetch_threshold = 0.5
        # An initialized list of k clusters
        self.clusters = [Cluster(dim) for _ in range(k)]

        # The accuracy and hitrate are the performance metrics (i.e. the results)
        self.accuracy = 0
        self.hitrate = 0

    def train(self):
        # implement k-means algorithm here:
        # Step 1: Select an initial random partioning with k clusters
        for i in range(len(self.traindata)):
            self.clusters[random.randint(len(clusters))].current_members.append(i)

        # Calculate prototype and previousMembers for each cluster
        converged = False
        while not converged:
            for cluster in (self.clusters): # Loop through each cluster
                for member in (cluster.current_members): # Loop through each member in each cluster
                    for j in range(200): 
                        cluster.prototype[j] += self.traindata.get(member)[j] # Add the member vector values to prototype
                for j in range(200):
                    cluster.prototype /= len(cluster.current_members) # Average prototype
                cluster.previous_members.clear() 
                cluster.previous_members.append(cluster.current_members)
                cluster.current_members.clear()
        
        # Step 2: Generate a new partition by assigning each datapoint to its closest cluster center
        # Step 3: recalculate cluster centers
        # Step 4: repeat until clustermembership stabilizes
        pass

    def test(self):
        # iterate along all clients. Assumption: the same clients are in the same order as in the testData
        # for each client find the cluster of which it is a member
        # get the actual testData (the vector) of this client
        # iterate along all dimensions
        # and count prefetched htmls
        # count number of hits
        # count number of requests
        # set the global variables hitrate and accuracy to their appropriate value
        pass


    def print_test(self):
        print("Prefetch threshold =", self.prefetch_threshold)
        print("Hitrate:", self.hitrate)
        print("Accuracy:", self.accuracy)
        print("Hitrate+Accuracy =", self.hitrate+self.accuracy)

    def print_members(self):
        for i, cluster in enumerate(self.clusters):
            print("Members cluster", i, ":", cluster.current_members)

    def print_prototypes(self):
        for i, cluster in enumerate(self.clusters):
            print("Prototype cluster", i, ":", cluster.prototype)