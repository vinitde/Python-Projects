import cv2

# Function to perform image processing
def process_frame(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Perform edge detection
    edges = cv2.Canny(gray, 100, 200)
    
    return edges

# Main function
def main():
    # Open default camera
    cap = cv2.VideoCapture(0)
    
    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error: Couldn't open camera")
        return
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Couldn't capture frame")
            break
        
        # Process frame
        processed_frame = process_frame(frame)
        
        # Display the resulting frame
        cv2.imshow('Original', frame)
        cv2.imshow('Processed', processed_frame)
        
        # Check for 'q' key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
