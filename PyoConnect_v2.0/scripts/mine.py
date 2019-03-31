scriptTitle = "Test left right"
scriptDescription = "Control Impress presentations"

def onPoseEdge(pose, edge):
	# the next IF will be true for any LibreOffice product
	if (myo.getPoseSide() == "waveRight"): # next slide
            print ("RIght:")
	if (myo.getPoseSide() == "waveLeft"): # prev slide
            print ("LEFT:")


