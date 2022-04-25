
# It will remove all overlapping boxes
def overlapping_eliminator(boxes, eps=0.2):
    #print("len of boxes: {}".format(len(boxes)))
    if not(boxes is list):
        boxes = np.array(boxes).tolist()
        #boxes = boxes.tolist()
    
    selected_boxes=boxes
    #selected_boxes = np.delete(selected_boxes,[0],axis=0)
    #selected_boxes = list(selected_boxes)
    processed_boxes = []
    i=0
    #print("boxes: {}".format(selected_boxes))
    while (i < len(selected_boxes)):
        #print("selected box: {}".format(selected_boxes[i]))
        xa1, ya1, w1, h1 = selected_boxes[i]
        xa2 = xa1 + w1
        ya2 = ya1 + h1

        listBoxes = selected_boxes[i+1:]
        #print("list boxes: {}".format(listBoxes))
        SA = w1*h1
        for b in listBoxes:
            #print("b={}".format(b))
            
            xb1, yb1, w2, h2 = b
            xb2 = xb1 + w2
            yb2 = yb1 + h2

            # Area of Intersection of two boxes
            SI = max(0, (min(xa2, xb2) - max(xa1, xb1))) * max(0, (min(ya2, yb2) - max(ya1, yb1)))
            
            SB = w2*h2
            SU = SA + SB - SI
            if(SI/SU) > eps:        # 0.4 is good
                if b in selected_boxes:
                    selected_boxes.remove(b)
                #print("selected boxes: {}".format(selected_boxes))
                #print("selected boxes[0]: {}".format(selected_boxes[0]))
                #for sel_id, sel_box in enumerate(selected_boxes):
                #    print("sel_id: {}".format(sel_id))
                #    print("sel_box: {}".format(selected_boxes[sel_id]))
                #    print("b: {}".format(b))
                #    if b.tolist() == sel_box.tolist():
                
                        
                        #selected_boxes = np.delete(selected_boxes,b,axis=0)  
                #        break
                continue
        i=i+1
    return selected_boxes
