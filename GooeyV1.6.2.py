from tkinter import *
from threading import *
from PIL import Image, ImageTk
import cv2

def main():
    UniPadx = 1
    UniPady = 1
    UniHighlight = 1
    UniTuple = -1.2

    root = Tk()

    # DIMENSIONS HEIGHT, WIDTH
    TopHeight = 180
    TopWidth = (int)(TopHeight * .125)

    TopDimensions = [(int)(TopWidth * UniTuple), (int)(TopHeight * UniTuple)] 
    LowerDimensions = [(int)(TopDimensions[0] * .636 * UniTuple), (int)(TopDimensions[1] * .5 * UniTuple)] # FRAME RATIOS

    # MAIN CAM FRAME PARENT
    CamParent = Frame(root, highlightbackground= "black", highlightthickness= UniHighlight)

    # LAYER FRAMES
    middleFrame = Frame(CamParent, highlightbackground= "black", highlightthickness= UniHighlight, height = 20, width = 80)
    bottomFrame = Frame(CamParent, highlightbackground= "black", highlightthickness= UniHighlight, height = 20, width = 80)
    topFrame = Frame(CamParent, highlightbackground= "black", highlightthickness= 5, height = 20, width = 80)

    # CAM 1 - STANDALONE TOP FRAME
    frame1 = Frame(topFrame, highlightbackground= "black", highlightthickness= UniHighlight)
    frame1.pack(padx= UniPadx, pady= UniPady, expand= True, fill = BOTH, side= LEFT)   # PACKING INTERIOR FRAME INTO EXTERIOR FRAME

    myCam1 = Label(frame1, text = "CAM1", height= TopDimensions[0], width= TopDimensions[1])
    myCam1.pack_propagate(0)
    myCam1.pack(expand= True)

    # CAM 2 - MIDDLE FRAME
    frame2 = Frame(middleFrame, highlightbackground= "black", highlightthickness= UniHighlight)
    frame2.pack(padx= UniPadx, pady= UniPady, expand= True, fill = BOTH, side= LEFT)   # PACKING INTERIOR FRAME INTO EXTERIOR FRAME

    myCam2 = Label(frame2, text="CAM2", height= LowerDimensions[0], width = LowerDimensions[1]) # PACKING LABEL INTO INTERIOR FRAME
    myCam2.pack_propagate(0)
    myCam2.pack(expand= True)

    # CAM 3 - MIDDLE FRAME
    frame3 = Frame(middleFrame, highlightbackground= "black", highlightthickness= UniHighlight)
    frame3.pack(padx= UniPadx, pady= UniPady, expand = True, fill = BOTH, side= RIGHT)   # PACKING INTERIOR FRAME INTO EXTERIOR FRAME

    myCam3 = Label(frame3, text="CAM3", height= LowerDimensions[0], width= LowerDimensions[1]) # PACKING LABEL INTO INTERIOR FRAME
    myCam3.pack_propagate(0)
    myCam3.pack(expand= True)

    # CAM 4 - BOTTOM FRAME
    frame4 = Frame(bottomFrame, highlightbackground= "black", highlightthickness= UniHighlight)
    frame4.pack(padx= UniPadx, pady= UniPady, expand= True, fill = BOTH, side= LEFT)   # PACKING INTERIOR FRAME INTO EXTERIOR FRAME

    myCam4 = Label(frame4, text="CAM4", height= LowerDimensions[0], width= LowerDimensions[1]) # PACKING LABEL INTO INTERIOR FRAME
    myCam4.pack_propagate(0)
    myCam4.pack(expand= True)

    # CAM 5 - BOTTOM FRAME
    frame5 = Frame(bottomFrame, highlightbackground= "black", highlightthickness= UniHighlight)
    frame5.pack(padx= UniPadx, pady= UniPady, expand = True, fill = BOTH, side= RIGHT)   # PACKING INTERIOR FRAME INTO EXTERIOR FRAME

    myCam5 = Label(frame5, text="CAM5", height= LowerDimensions[0], width= LowerDimensions[1]) # PACKING LABEL INTO INTERIOR FRAME
    myCam5.pack_propagate(0)
    myCam5.pack(expand= True)

    # Shoving it into the CamParent
    topFrame.grid(row = 0, column = 2) # TOP - CAM 1

    middleFrame.grid(row = 1, column = 2) # MIDDLE - CAM 2 & 3

    bottomFrame.grid(row = 2, column = 2) # MIDDLE - CAM 4 & 5

    # PLACING CAM PARENT TO WHICHEVER SIDE
    CamParent.pack_propagate(0)
    CamParent.pack(fill = BOTH, side= RIGHT, expand= True)

    #-----------------------------------------------#
    # CONTROLLER DISPLAY
    sideframe = Frame(root, highlightbackground= "black", highlightthickness= UniHighlight, height = 10, width = int(LowerDimensions[1]) * 5)
    
    sideframe.pack_propagate(0)
    sideframe.pack(fill=BOTH, side=LEFT)

    ControllerText = Label(sideframe, text="CONTROLLER TEXT", height= LowerDimensions[0], width= int(LowerDimensions[1] * .3)) # PACKING LABEL INTO INTERIOR FRAME
    ControllerText.pack(expand= True)

    #---------CAMERA DISPLAY----------#
    def threading(cap, label, camnum, height, width):
        # Call camDisplay
        t1 = Thread(target=camDisplay(cap, label, camnum, height, width))
        t1.start()

    def camDisplay(cap, label, camnum, h, w):
        #print(f"CamDisplay {camnum}, ACTIVE")

        # Get the latest frame and convert into Image
        cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)

        img = Image.fromarray(cv2image)
        # Convert image to PhotoImage
        imgtk = ImageTk.PhotoImage(image = img)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        # Repeat after an interval to capture continiously
        label.after(24, camDisplay, cap, label, camnum, h, w)
    
    #---------CAM VAR SETUP---------#
    # Cam 1
    cam1= cv2.VideoCapture(0)
    threading(cam1, myCam1, 1, TopDimensions[0], TopDimensions[1])
    # Cam 2
    cam2= cv2.VideoCapture(1)
    threading(cam2, myCam2, 2, LowerDimensions[0], LowerDimensions[1])
    # Cam 3
    cam3= cv2.VideoCapture(0)
    threading(cam3, myCam3, 3, LowerDimensions[0], LowerDimensions[1])
    # Cam 4
    cam4= cv2.VideoCapture(1)
    threading(cam4, myCam4, 4, LowerDimensions[0], LowerDimensions[1])
    # Cam 5
    cam5= cv2.VideoCapture(0)
    threading(cam5, myCam5, 5, LowerDimensions[0], LowerDimensions[1])

    root.mainloop()



if __name__ == "__main__":
    main()
