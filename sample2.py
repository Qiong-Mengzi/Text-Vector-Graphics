# You need cv2 and numpy to save TVG image
import cv2
import numpy as np

import TVG
from TVG.pytvg import TVG_OpenA,TVG_Save,TVG_Show

# Create a new TVG, Width = 200, Height = 200
tvg = TVG_OpenA()
tvg.setSize((200,200))

# Blue Color
Blue = TVG.ToColor('0x0000ff')

# Add a circle
tvg.append(TVG.circle(x=0.5,y=0.5,r=0.4,color=Blue,lr=0.008))

# Add two lines
tvg.append(TVG.line(x1=0.3,y1=0.5,x2=0.5,y2=0.7,color=Blue,lr=0.002))
tvg.append(TVG.line(x1=0.5,y1=0.7,x2=0.7,y2=0.3,color=Blue,lr=0.004))

# Save TVG
with open('TVG-samples/correct.tvg','w') as f:
    f.write(TVG_Save(tvg))

# Convert TVG to RGBA
# It may take lots of time...
cloth = TVG.vEmptyCloth((tvg.Width,tvg.Height))
TVG_Show(tvg,cloth)

# Save PNG Image
cv2.imwrite('TVG-samples/correct.png',
    cv2.cvtColor(np.array(cloth.arr,dtype=np.uint8),cv2.COLOR_RGBA2BGRA)
)
