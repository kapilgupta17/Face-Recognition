# Face-Recognition using Haar Cascade and LBPH Algorithm

This project implements a face recognition system using the Haar Cascade for face detection and the Local Binary Patterns Histograms (LBPH) algorithm for face recognition. The Haar Cascade algorithm efficiently detects faces in images or video streams, providing a foundation for accurate face recognition. The LBPH algorithm extracts unique facial features, creating a robust model capable of recognizing faces with high accuracy, even in challenging lighting conditions.

The system offers a user-friendly interface for easy integration into existing applications, making it suitable for various use cases, including security systems, access control, and personalized user experiences. The project demonstrates the effectiveness of combining the Haar Cascade and LBPH algorithms to create a reliable and adaptable face recognition solution.

The following command has to be run to get the results

sh run.sh

(or)

```bash
sh run.sh
```

After running this command two things will happen:

1. A file called "obama_face_train.yml" will be created.
2. The images in test-data folder would be changed with the results that the program is supposed to produce as we have shown in the video.

Please check the test-data folder before executing that the present images are without the required results i.e no green boxes with accuracy percentage.

Please also note out of 11 test cases , we have 4 hard test cases which give false results,i.e, Mr.Barack Obama's face is not recognized.

We have added a folder called "Results" which consists of the required results that we were able to produce and that the programs are supposed to produce for reference 
