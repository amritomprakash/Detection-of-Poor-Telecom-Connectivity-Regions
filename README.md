# Detection-of-Poor-Telecom-Connectivity-Regions
Problem statement: 
Detecting Poor Telecom Connectivity (Cellular) regions using user device signal strength

Components:
1. Android Application: Designed using MIT App inventor to calculate the signal strength
2. Python Flask: Back end- web server for generating visualization of the signal strength and run ML algorithm to predict the signal strength of a region whose signal strength is unnkown

Working:
1.Android Application designed to calculate the signal strength of the region in which the device is present
2.The signal strength along with the latitude and longitude values of the reading taken are pushed into a NOSql database server
3.Python Flask script reads the data and creates an interactive visualization map on a webpage marking the areas whose data is present with their corresponding signal strengths
4. K-NN Algorithm(Machine Learning) is used to estimate the signal strength of a region whose data is not present

Instructions to run the Android APP:
1.Install the Android APK
2.Click on the EXPORT button to publish the signal strength

Instruction to use the Python script
1.Save all the files regarading the python script on the same folder
2.First run the model.py
3.Then, run final.py(flask server)
4.Open the front.html page

FOR FURTHER DETAILS REFER TO THE PPT ATTACHED
