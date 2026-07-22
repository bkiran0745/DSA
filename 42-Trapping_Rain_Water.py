def Trapping_Rain_Water(h):
  l = 0 # left pointer
  r = len(h)-1 # right pointer
  t = 0 # varible to store Trapping Rain Water
  lm = 0 # varible to store left max value
  rm = 0 # varible to store right max value
  while l < r:
    if h[l] < h[r]:
      if h[l] > lm:
        lm = h[l]
      else:
        t += lm - h[l]
      l += 1
    else:
      if h[r]>rm:
        rm = h[r]
      else:
        t += rm-h[r]
      r -= 1
  return t 
  
print(Trapping_Rain_Water([0,1,0,2,1,0,1,3,2,1,2,1]))
