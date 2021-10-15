<h1>Covid Detection from Xrays Using Convolutional Neral Networks.</h1>
<img src="https://www.spiedigitallibrary.org/ContentImages/Journals/JMIOBU/8/S1/014001/WebImages/JMI_8_S1_014001_f005.png">
<hr>
<h2>Overview</h2>
<p>
The traditional Methods of detecting covid 19 are slow and tedious and as have been seen in the case of this deadly virus the more dealay in detecting it the more patients become victim of the virus hence we need some fast procedures that could detect corona as fast as possible hence i worked on the machine learning model that could extract features from the X-ray of the lungs of patients and with accuracy of 73% can tell whether the patient is infected or not. 
<br><br>
 <b>The Online Deployed link : <span href="https://covid-detection-steveroger.herokuapp.com/">https://covid-detection-steveroger.herokuapp.com/</span></b>
</p>
<hr>
<h2>Dataset And Libraries</h2>
<p>
<b>Dataset : </b> Chest Xrays Dataset from kaggle.<br>
<b>Libraries : </b> Python , Numpy , Pandas, NLTK , Sklearn , Node.js , Express.js.<br>
<b>Frameworks : </b> VScode , jupyter Notebook , Heroku.<br>
<b>Notebook For developing the Machine Learning model :<br><br>Link : <span href = "https://colab.research.google.com/drive/1WB-6DCzp6Wv3xXvJTpaAkYZxM_Yy7L3f?usp=sharing">https://colab.research.google.com/drive/1WB-6DCzp6Wv3xXvJTpaAkYZxM_Yy7L3f?usp=sharing</span><br></b>
</p>
<hr>
<h2>Project Methodology</h2>
<p>In this project i have ultilized the power of Convolutional neural networks to detect complex patterns that doctors tend to find whether the chest x-ray of an individual contains the patterns as they have been found in the corona patient.The steps that i have used in developing the mahine learning and deploying it using the web development are below mentioned :<br>
<b>1. Dataset Preparation : </b>Kaggle source of chest x-rays it consited of healthy and diseased patients and then i have developed my own dataset using pandas and numpy libraries.<br>
<b>2. Keras model : pipeline <br></b>
 (i) Convolutional Layer with 32 units.<br>
 (ii) Convolutional layer with 64 units.<br>
 (iii) Flatten to reduce channels.<br>
 (iv) Neural network dense layer with 8 units.<br>
 (v) Output unit with 1 unit to output whether infected or not infected.<br>
 <br>
 <b>On training the model the Keras pipeline gave 73% accuracy on training dataset.</b>
 </p>
 <hr>
 <h2>Screenshots of the project deployed</h2>

