# tensorflow-serving
Learning to deploy tensorflow models using tensorflow serving.

## MNIST Example.
- Run the file `mnist-vanilla-cnn.ipynb` and train a cnn model.
- Open a terminal in the root directory of the repo and start the container using the following command:   
    `docker run -p 8500:8500 -p 8501:8501 --name tfserver -v ${PWD}/mnist-digit-dataset/serving:/models/mnist_digit -e MODEL_NAME=mnist_digit -t tensorflow/serving`
- Open the `request.ipynb`, load the testing images and hit the API using the requesting code.