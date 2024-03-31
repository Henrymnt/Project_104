import cv2

img=cv2.imread("solar-system.jpg")

cv2.putText(img, 
            "The sun",
            (100,50),
            fontFace=cv2.FONT_ITALIC,
            fontScale=1,
            color=(255,255,255)
            )
cv2.putText(img, 
            "Mercury",
            (120,150),
            fontFace=cv2.FONT_ITALIC,
            fontScale=.5,
            color=(255,255,255)
            )
cv2.putText(img, 
            "Venus",
            (200,150),
            fontFace=cv2.FONT_ITALIC,
            fontScale=.5,
            color=(255,255,255)
            )
cv2.putText(img, 
            "Earth",
            (280,150),
            fontFace=cv2.FONT_ITALIC,
            fontScale=.5,
            color=(255,255,255)
            )
cv2.putText(img, 
            "Moon",
            (345,165),
            fontFace=cv2.FONT_ITALIC,
            fontScale=.3,
            color=(255,255,255)
            )
cv2.putText(img, 
            "Mars",
            (385,150),
            fontFace=cv2.FONT_ITALIC,
            fontScale=.5,
            color=(255,255,255)
            )
cv2.putText(img, 
            "Jupiter",
            (500,60),
            fontFace=cv2.FONT_ITALIC,
            fontScale=.7,
            color=(255,255,255)
            )
cv2.putText(img, 
            "Saturn",
            (750,85),
            fontFace=cv2.FONT_ITALIC,
            fontScale=.7,
            color=(255,255,255)
            )
cv2.putText(img, 
            "Uranus",
            (950,100),
            fontFace=cv2.FONT_ITALIC,
            fontScale=.7,
            color=(255,255,255)
            )
cv2.putText(img, 
            "Neptune",
            (1100,100),
            fontFace=cv2.FONT_ITALIC,
            fontScale=.7,
            color=(255,255,255)
            )


cv2.imshow('Image', img)
cv2.waitKey(0)