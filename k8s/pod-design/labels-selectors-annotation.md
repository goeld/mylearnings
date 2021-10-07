
### Label with Deployments
>Unlike pods deployments you can not have --labels when creating a deployment. You would need to create & then edit/apply. 

```shell

k create deployment deploy-label --image=nginx --replicas=3 --dry-run=client -o yaml --port=80 > deploy-label.yaml
k label deployments deploy-label j=k
k get deployments --selector j=k
```

### Label a Pod
```shell
$ k label pods mypod key=value 
k get pods --show-labels
k label pod pod-label my_new_label=my_new_label
k get pods --selector=my_new_label
```

### Labels with services
```shell
kubectl delete pods,services -l name=myLabel
kubectl logs -l name=mylabel
```
