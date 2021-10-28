# tensorflow-serving
Learning to deploy tensorflow models using tensorflow serving.

## MNIST Example.
- Run the file `mnist-digit-dataset\tf-server\mnist-vanilla-cnn.ipynb` and train a cnn model.
- Run the tensorflow and flask servers using `docker-compose up -d --build`.
- Run `mnist-digit-dataset\request-post.py --image <image-path>`. 