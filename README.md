# DIY Parabolic Reflector / Satellite Dish

This Python code calculates the measurements for a low-cost, lightweight parabolic reflector dish. The DIY parabolic reflector is created by approximating a paraboloid with tensioned struts.
A fine wire mesh can then be placed over the frame and be secured to create a functional reflector. Grid structures act like solid metallic surfaces as long as their mesh size is smaller than half the wavelength supposed to be reflected.

> **Note:** The resulting reflector's shape is not a perfect paraboloid, as it deviates by the thickness of the material used. However, for applications such as receiving signals from satellites in Low Earth Orbit, this deviation is within acceptable limits and delivers sufficient performance.

<img src="https://github.com/user-attachments/assets/aa9ba178-6a30-4016-9ce8-8fa9f0e3d420" alt="parabolic-reflector" width="600">

This reflector is designed for hobbyists who want to build a lightweight, cost-effective, and customizable satellite dish for their own projects. I have used the shown dish to receive the **High Resolution Picture Transmission (HRPT)** from NOAA satellites. Of course, other satellites of similar frequency will also work.
>  This reflector is not intended for receiving satellite television, etc., and inst suitable to replace regular satellite dishes.










### How it works:

![image](https://github.com/user-attachments/assets/5a860aac-a371-433c-91b5-339a3eebb442)

At the start, enter your desired dish diameter and the desired focal length of the dish (in mm). Run the code and it will output everything needed to construct the dish (it takes a second to run, since the Newton-Raphson-Method is used, change the initial guess to make this faster if you want) 

### Output:

As the output you get the segment lengths of the struts. The segments can be seen in the image below. There are two different parabolas in this design: A and B. C is the outer rim.

A and B have segments of different lengths. It's important to know the segment sizes, because screwholes to connect the struts have to be made there.

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/6e191834-d80b-41db-90dc-8c8d3ae11a3d" alt="image" width="400"></td>
    <td><img src="https://github.com/user-attachments/assets/c1e3fdda-dbb2-4659-ac19-dcedb7f71fda" alt="segments" width="400"></td>
  </tr>
</table>

With these segment lengths, you can create a sketch of the struts and their screwholes.
Parabola A exists 3 times. Parabola B exists 6 times. C exists 12 times.

**IMPORTANT:** You have to add 5mm to both ends of all struts for the additional space needed to create the screwholes there!

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/60a84094-6632-46b6-a4a9-8acfd84f20f1" alt="parabolic-reflector" width="600"></td>
    <td><img src="https://github.com/user-attachments/assets/748d83e1-cb95-4f27-a80f-1067f3d209bd" alt="parabolic-reflector" width="600"></td>
  </tr>
</table>



![image](https://github.com/user-attachments/assets/8cbeea6c-f3a5-47b8-8701-68a1bdca3860)

![image](https://github.com/user-attachments/assets/7870e593-794f-4f9b-b199-2627cc53511d)




![image](https://github.com/user-attachments/assets/06c2bf83-8b69-40b1-9118-e133efb48834)

It also outputs verything else about the parabolas you might want to know for example to 3D model it with a CAD software:

The length of the struts is calculated so that they can be cut out from, for example, MDF. The straight struts then get connected. This creates a basic framework of struts that approximate a paraboloid through tension.

The Python code outputs all parabola functions, so you can 3D model the reflector in a CAD program. It also outputs the length of the parabolas and the length of their segments. This can be used to cut out the struts from wood (like MDF) and add screw holes at the end of segments. I used the data of the lengths to create a DXF file that I later cut out with a laser cutter to create precise struts along with the screw holes. Use any means of cutting that you want—though a laser cutter is recommended.

Reference:
This builds upon Yoshiyuki Takeyasu's idea. You can find everything from his side about the dish on this [page](http://www.terra.dti.ne.jp/~takeyasu/). Very cool stuff he has come up with! I recommend checking it out if you are an antenna enthusiast.
I found his work when looking for a way to build my own lightweight parabolic reflector. He provides an Excel sheet to do the calculations, but I couldn't understand or verify the calculation behind it from just looking at the sheet (needed verification for my bacheolr thesis), so I redid the calculations on my own and wrote my own program to check if the numbers are correct and to output all the things I would need to 3D model the frame.
 
