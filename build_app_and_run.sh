echo "Stopping container.."
docker stop app
echo "Deleting container.."
docker rm app
echo "Deleting docker image.."
docker image rm app
echo "Building docker image.."
docker build -t app .
echo "Running container.."
docker run -it -d -p 8081:8081 --name app app
echo "Container started"
