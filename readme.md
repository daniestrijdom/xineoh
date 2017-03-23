## Xineoh Code Test

# NOTES:

Scientific:
----------
Classifier used is K Nearest neighbors.
K is approximated but not optimised due to time contraints.

Observations:
------------
The confusion matrix shows an acceptable degree of accuracy. Noteworthy however there is an error cluster between the
models interpretation of the number 4, 8 and 9, which can be intuitively explained.
The experiment was done with both uniform and distance weightings and as suspected the distance weighting achieved
much higher accuracy.
Finally, even at 0.94 accuracy, the performance is perhaps a bit poor considering the images are fairly simple in nature
and that optimised models on similar datasets outperform this accuracy level. Optimising K and repeating the experiment
with variations of the KNN family of algorithms would likely improve results.

Example Outputs:
----------------

- With distance weighting
![alt tag](https://github.com/daniestrijdom/xineoh/blob/master/result1.PNG)

- with uniform weighting
![alt tag](https://github.com/daniestrijdom/xineoh/blob/master/result2.PNG)

*\note - output format has since been altered
