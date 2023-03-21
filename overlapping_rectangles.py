def overlap_rectangles(rect1, rect2):
  overlapped_x = 0
  overlapped_y = 0
  
  if (rect2[0] < rect1[2] ) and (rect2[1] < rect1[3]): 
    overlapped_x = abs(rect1[0] - rect2[0])
    overlapped_y = abs(rect1[1] - rect2[1])

  return overlapped_x * overlapped_y
