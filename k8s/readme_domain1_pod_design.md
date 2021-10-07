## List of examples


|Desc| File Name| Remarks|
|:--------------------------|:--------------------------|:-------------|
|Simple pod|pod-nginx| |
|Pod with command | pod-busybox-command| |
|Pod with command & argument| pod-bb-cmd-args | |


## Docker entrypoint/command & Kuberneter Command/Args 

|Scenario| Docker | Kuberneter | Output|
|:----|:-------:|:-----------:|:----------:|
|1| sleep,3600| <>,<>|sleep 3600|
|2| sleep, 3600| ping -c google.com, <>|ping -c google.com|
|3| sleep, 3600| <>, 5000| sleep 5000|
|4| sleep, 3600| ping, yahoo.com| ping yahoo.com|
 

## A comprehensive reference for pod yaml file

```yaml

apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  labels:
    label1: value1
spec:
  containers:
  - image: <image_name>
     name: <container_name>
     env:
      envFrom:
      - secretRef:
           name: <secret_ref_file>
      - configMapRef:
           name: <configmap_ref_file>
      - securityContext:
         - runAsUser:
         - addCapabilities: ["Cap1"]
    tolerations:
    - key: "app"
      value: "blue"
      operator: "Equal"
      effect: "NoSchedule"
    nodeSelector:
      size: Large          //<key>: <value>
```


## Pod commnads

```bash
$ kubectl get pods
$ kubectl describe pods
$ kubectl describe pods <<Pod Name>>
$ kubectl run <<Pod Name>> --image=<<image_name>>
$ kubectl edit pods <<Pod Name>>

```