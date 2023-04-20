import face_recognition
# from PIL import Image, ImageDraw
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
sanjay_image = face_recognition.load_image_file("abhilash.jpg")
sanjay_face_encoding = face_recognition.face_encodings(sanjay_image)[0]

# # Load a second sample picture and learn how to recognize it.
rishab_image = face_recognition.load_image_file("vinay.jpeg")
rishab_face_encoding = face_recognition.face_encodings(rishab_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    sanjay_face_encoding,rishab_face_encoding
]
known_face_names = [
    "Abhilash",
    "Vinay"
]

# Load an image with an unknown face
# unknown_image = face_recognition.load_image_file("f1.jpg")
while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]
# Find all the faces and face encodings in the unknown image
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # pil_image = Image.fromarray(unknown_image)
    # draw = ImageDraw.Draw(pil_image)

    # Loop through each face found in the unknown image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "random Name"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255),cv2.FILLED)
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255),1)
        if name != "randoName":
            print(name, "was there")
    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()   
    # # Draw a box around the face using the Pillow module
    # draw.rectangle(((left, top), (right, bottom)), outline=(48, 63, 159)) 

    # # Draw a label with a name below the face
    # text_width, text_height = draw.textsize(name)
    # draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(48, 63, 159), outline=(48, 63, 159))
    # draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 0))


# Remove the drawing library from memory as per the Pillow docs
# del draw

# pil_image.show()

# You can also save a copy of the new image to disk if you want by uncommenting this line
# pil_image.save("image_with_boxes.jpg")
