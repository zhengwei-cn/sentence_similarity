docker build -t sentence_similarity .
docker save -o C:\DockerImages\sentence_similarity.tar sentence_similarity
docker load -i /home/user/my_project_image.tar
docker run -d -p 8000:5000 --name sentence_similarity_container sentence_similarity
