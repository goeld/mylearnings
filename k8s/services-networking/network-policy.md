

```shell
$ k create ingress my-ingress --rule="host/path=service-dns-name:8080"
```

**Ingress with a service**

Network Policy Ingress [Image](network-policy-ingress.png)
Network Policy Ingress [Image](network-policy-example.png)

Network Policy
@TrafficFlow

**Description of Network Policy from the yaml file**

- podSelector Defines which pod the policy is for
- policyTypes : Defines what are the policies either ingress or egress

**Both Ingress/egress can accept the traffic from 3 sources**
- A pod selector
- Namespace selector
- IP Range (ipblock)

Also, need to define port on which policy is associated


> NetworkPolicies are an application-centric construct which allow you to specify how a pod is allowed to communicate with various network "entities"
