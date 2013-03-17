from numpy import *

def MeanShiftCluster(dataPts, bandWidth):
    dataPts = asarray( dataPts )
    bandWidth = float( bandWidth )
    plotFlag = False    
    
    numDim, numPts = dataPts.shape
    numClust        = 0
    bandSq          = bandWidth**2
    initPtInds      = arange( numPts )
    maxPos          = dataPts.max(0)                          #biggest size in each dimension
    minPos          = dataPts.min(0)                          #smallest size in each dimension
    boundBox        = maxPos-minPos                        #bounding box size
    sizeSpace       = norm(boundBox)                       #indicator of size of data space
    stopThresh      = 1e-3*bandWidth                       #when mean has converged
    clustCent       = []                                   #center of clust
    beenVisitedFlag = zeros( numPts, dtype = uint8 )              #track if a points been seen already
    numInitPts      = numPts                               #number of points to possibly use as initilization points
    clusterVotes    = [] #zeros( numPts, dtype = uint16 )             #used to resolve conflicts on cluster membership
    
    while numInitPts:
        
        rand = random.rand()
        tempInd         = int(floor( (numInitPts-1e-6)*rand ))        #pick a random seed point
        stInd           = initPtInds[ tempInd ]                  #use this point as start of mean
        myMean          = dataPts[ :, stInd ]                           # intilize mean to this points location
        myMembers       = []                                   # points that will get added to this cluster                          
        thisClusterVotes    = zeros( numPts, dtype = uint16 )         #used to resolve conflicts on cluster membership
        
        while True:     #loop untill convergence
            
            sqDistToAll = (( myMean[:,newaxis] - dataPts )**2).sum(0)    #dist squared from mean to all points still active
            inInds      = where(sqDistToAll < bandSq)               #points within bandWidth
            thisClusterVotes[ inInds ] = thisClusterVotes[ inInds ]+1  #add a vote for all the in points belonging to this cluster
            
            
            myOldMean   = myMean                                   #save the old mean
            myMean      = mean( dataPts[ :, inInds[0] ], 1 )                #compute the new mean
            myMembers.extend( inInds[0] )                       #add any point within bandWidth to the cluster
            beenVisitedFlag[myMembers] = 1                         #mark that these points have been visited
                        
            #**** if mean doesn't move much stop this cluster ***
            if norm(myMean-myOldMean) < stopThresh:
                
                #check for merge posibilities
                mergeWith = None
                for cN in xrange( numClust ):
                    distToOther = norm( myMean - clustCent[ cN ] )     #distance from possible new clust max to old clust max
                    if distToOther < bandWidth/2:                    #if its within bandwidth/2 merge new and old
                        mergeWith = cN
                        break
                
                
                if mergeWith is not None:    # something to merge
                    clustCent[ mergeWith ]       = 0.5*( myMean + clustCent[ mergeWith ] )             #record the max as the mean of the two merged (I know biased twoards new ones)
                    #clustMembsCell{mergeWith}    = unique([clustMembsCell{mergeWith} myMembers]);   #record which points inside 
                    clusterVotes[ mergeWith ]    += thisClusterVotes    #add these votes to the merged cluster
                else:    #its a new cluster
                    numClust                    = numClust+1                   #increment clusters
                    clustCent.append( myMean )                       #record the mean  
                    #clustMembsCell{numClust}    = myMembers;                    #store my members
                    clusterVotes.append( thisClusterVotes )
    
                break
        
        initPtInds      = where(beenVisitedFlag == 0)[0]           #we can initialize with any of the points not yet visited
        numInitPts      = len(initPtInds)                   #number of active points in set
    
    data2cluster = asarray( clusterVotes ).argmax(0)                #a point belongs to the cluster with the most votes

    return clustCent, data2cluster


def norm( a ):
    '''
    Vector norm, behaves like Matlab's norm when 'a' is a vector.
    '''
    a = asarray( a )
    ## Make sure 'a' is a vector.
    assert prod( a.shape ) == max( a.shape )
    a = a.ravel()
    return sqrt( ( a ** 2 ).sum() )


def test():
    print '=== beginning test ==='
    dataPts = asarray([[1],[2],[3],[9],[9],[9],[10]]).T
    bandwidth = 2
    print 'data points:', dataPts
    print 'bandwidth:', bandwidth
    clustCent, data2cluster = MeanShiftCluster(dataPts, 2)
    print 'cluster centers:', sorted( asarray( clustCent ).squeeze().tolist() )
    print 'data2cluster:', data2cluster
    assert len( clustCent ) == 2
    assert sorted( asarray( clustCent ).squeeze().tolist() ) == [ 2., 9.25 ]
    print '=== passed test ==='

def main():
    test()

if __name__ == '__main__': main()
