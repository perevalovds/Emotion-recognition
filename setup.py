import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Emotion-recognition",
    version="0.0.1",
    author="Denis Perevalov (forked from omar 178)",
    author_email="",
    description="Real time emotion recognition",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url="https://github.com/perevalovds/Emotion-recognition",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: Windows :: Windows 10"
    ],
    python_requires='>=3.6.3',
    install_requires=[
       #'coverage==4.5.3',
       'keras', #,===2.2.4',
       'lasagne',
       #'pytest',
       #'matplotlib>2.1.0',
       'numpy', #==1.17.4',
       #'scikit-image>=0.13.1',
       #'scikit-learn>=0.19.1',
       #'scikit-neuralnetwork>=0.7',
       #'scipy==1.0.0',
       'tensorflow', #==1.13.1',
       'opencv-python',
	   #'h5py',
       #'pydot',
       #'graphviz',
	   'imutils',
	   #'cv2',
       'python-osc>=1.7.4',
       
    ]
)
