
# Namespace

Create Namespace
```shell
$ k create ns dev
```

Get current Context
```shell
$ k config current-context
```
(e.g. minikube in local) 

To Switch namespace
```shell
$ k config set-context $(k config current-context) --namespace=dev
```
This will set the namespace (in current context - minikube) to dev

To get pod in another namespace
```shell
$ k get pods --namespace=dev
```

To get pods in all namespaces
```shell
$ k get pods --all-namespaces
OR 
$ k get pods -A
```

# Resource Quota
>A resource quota, defined by a ResourceQuota object, provides constraints that limit aggregate resource consumption per namespace. 
> It can limit the quantity of objects that can be created in a namespace by type, 
> as well as the total amount of compute resources that may be consumed by resources in that namespace.
```shell
$ k get resourcequota
```

```shell
$ kubectl create namespace teama
$ kubectl get namespces
$ kubectl get pods
$ kubectl get pods --namespace kube-system
$ kubectl run nginx --image=nginx --namespace=teama
$ kubectl get pods --namespace=teama
$ kubectl delete pods nginx --namespace=teama

```



# Limit Range

> By default, containers run with unbounded compute resources on a Kubernetes cluster. With resource quotas, cluster administrators can restrict resource consumption and creation on a namespace basis. Within a namespace, a Pod or Container can consume as much CPU and memory as defined by the namespace's resource quota. There is a concern that one Pod or Container could monopolize all available resources. A LimitRange is a policy to constrain resource allocations (to Pods or Containers) in a namespace.

A LimitRange provides constraints that can:

* Enforce minimum and maximum compute resources usage per Pod or Container in a namespace.
* Enforce minimum and maximum storage request per PersistentVolumeClaim in a namespace.
* Enforce a ratio between request and limit for a resource in a namespace.
* Set default request/limit for compute resources in a namespace and automatically inject them to Containers at runtime.


* Limit range are scoped by namespace.

This is for enable 
* default Request memory = 256Mi
* default memory (Disk) = 512Mi

