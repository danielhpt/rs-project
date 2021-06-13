docker build -t db db/
docker build -t api api/
docker build -t web web/
kubectl apply -f kubernetes/persistent-volume.yml
kubectl apply -f kubernetes/persistent-volume-claim.yml
kubectl apply -f kubernetes/statefulset.yml
kubectl apply -f kubernetes/statefulset-service.yml
kubectl apply -f kubernetes/deployment-api.yml
kubectl apply -f kubernetes/deployment-web.yml
kubectl apply -f kubernetes/load-balancer-api.yml
kubectl apply -f kubernetes/load-balancer-web.yml