# Function to adjust volume based on finger movement
def adjust_volume(hand, fingertips):
    global gesture_area, gesture_start_x, volume
    
    # Calculate distance between thumb and index finger
    thumb_tip = fingertips[0]
    index_tip = fingertips[1]
    distance = calculate_distance(thumb_tip, index_tip)
    
    # Define gesture area if not already defined
    if gesture_area is None:
        gesture_area = (hand[0][0], hand[1][1], hand[1][0], hand[0][1])
        gesture_start_x = index_tip[0]
    
    # Check if thumb is inside the gesture area
    if gesture_area[0] < thumb_tip[0] < gesture_area[2] and gesture_area[1] < thumb_tip[1] < gesture_area[3]:
        # Adjust volume based on thumb movement relative to index finger
        delta_x = thumb_tip[0] - gesture_start_x
        new_volume = volume + delta_x
        
        # If distance between thumb and index finger decreases, increase volume
        if distance < previous_distance:
            new_volume += 1  # Increase volume
        
        volume = min(max(new_volume, min_volume), max_volume)
        gesture_start_x = thumb_tip[0]
    
    # Update previous distance
    previous_distance = distance


previous_distance = float('inf')  # Initialize previous distance
