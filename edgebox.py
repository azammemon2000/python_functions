
def init_edgebox():
    import cv2
    op_model='model.yml.gz'
    
    edge_boxes = cv2.ximgproc.createEdgeBoxes()
    edge_boxes.setMaxBoxes(555)    #1000=0.2132, 400=0.0450, 500=0.5859, 300=0.5714, 200=0.2493, 600=0.5399, 700=0.4562, 550 = 0.6369, 570=0.6043, 560=0.6364, 540=0.5942, 545=0.6154, 555=0.6420
    #edge_boxes.setMinScore(0.05)
    # edge_boxes.setMinScore(10)
    # edge_boxes.setMinBoxArea(1000)
    # edge_boxes.setMaxAspectRatio(1)
    # edge_boxes.setEdgeMinMag(0.3)           #0.3 covers all regions of image
    # edge_boxes.setClusterMinMag(10)
    # edge_boxes.setKappa(0.1)        # scale sensitivity
    # edge_boxes.setAlpha(0.65)        # step size for Sliding window
    # edge_boxes.setBeta(0.8)         # Non-Maximum Suppression
    # edge_boxes.setGamma(0.75)
    # edge_boxes.setEta(0.1)          # adaptation rate for non-maximal suppression
    edge_detection = cv2.ximgproc.createStructuredEdgeDetection(op_model)
    
    return edge_boxes, edge_detection

def find_object_proposals(img, edge_boxes, edge_detection):
    
    edges = edge_detection.detectEdges(np.float32(img)/255.0)
    
    orimap = edge_detection.computeOrientation(edges)
    edges = edge_detection.edgesNms(edges, orimap)
    boxes = edge_boxes.getBoundingBoxes(edges, orimap)
    
    return boxes[0]
    

if __name__ == '__main__':
    edge_boxes, edge_detection = init_edgebox()
    boxes = find_object_proposals(img_i, edge_boxes, edge_detection)
