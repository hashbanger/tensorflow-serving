# tensorflow-serving
Learning to deploy tensorflow models using tensorflow serving.

## MNIST Example.
- Run the file `mnist-digit-dataset\mnist-vanilla-cnn.ipynb` and train a cnn model.
- Run the container using `docker-compose up -d` or alternatively run the command in `mnist-digit-dataset\serving_commands.txt`.
- Open the `mnist-digit-dataset\request.ipynb`, load the testing images and hit the API using the requesting code.