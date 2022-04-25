def extract_text_regions(img):
    import cv2
    img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 180, 255, cv2.THRESH_BINARY)
    image_final = cv2.bitwise_and(img2gray, img2gray, mask=mask)
    
    text_regions={}
    
    ret, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY)  # for black text , cv.THRESH_BINARY_INV
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))  # to manipulate the orientation of dilution , large x means horizonatally dilating  more, large y means vertically dilating more
    dilated = cv2.dilate(new_img, kernel, iterations=9)  # dilate , more the iteration more the dilation
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # findContours returns 3 variables for getting contours
    
    idx2 = 0
    
    for idx, contour in enumerate(contours):

        [x, y, w, h] = cv2.boundingRect(contour)

        # Don't plot small false positives that aren't text
        if w < 100 and h < 100:
            continue
        cropped = img[y :y +  h , x : x + w]
        if len(text_regions) == 0:
            text_regions[idx2]=cropped
            idx2 = idx2 + 1
            continue
        
        regions = list(text_regions.items())
        for k,v in regions:
            #print(v)
            #print("v: {}".format(v))
            #print("-----------")
            #print("cropped: {}".format(cropped))
            #print("-----------")
            if v.all()==cropped.all():
                #print(v)
                #print("Matched")
                continue
            else:
                text_regions[idx2]=cropped
                idx2 = idx2 + 1
       
        
    # Detect Black Text
    ret, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY_INV)  # for black text , cv.THRESH_BINARY_INV
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))  # to manipulate the orientation of dilution , large x means horizonatally dilating  more, large y means vertically dilating more
    dilated = cv2.dilate(new_img, kernel, iterations=9)  # dilate , more the iteration more the dilation
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # findContours returns 3 variables for getting contours
    for idx, contour in enumerate(contours):

        [x, y, w, h] = cv2.boundingRect(contour)
        #print(x, y, w, h)
        # Don't plot small false positives that aren't text
        if w < 100 and h < 100:
            continue
        cropped = img[y :y +  h , x : x + w]
        if len(text_regions) == 0:
            text_regions[idx2]=cropped
            idx2 = idx2 + 1
            continue
        regions = list(text_regions.items())
        for k,v in regions:
            if v.all()==cropped.all():
                #print(v)
                #print("Matched")
                continue
            else:
                text_regions[idx2]=cropped
                idx2 = idx2  + 1

        
    
    return text_regions
