Assigning Pods to Nodes
> You can constrain a Pod so that it can only run on particular set of Node(s). There are several ways to do this and the recommended approaches all use label selectors to facilitate the selection. Generally such constraints are unnecessary, as the scheduler will automatically do a reasonable placement (e.g. spread your pods across nodes so as not place the pod on a node with insufficient free resources, etc.) but there are some circumstances where you may want to control which node the pod deploys to - for example to ensure that a pod ends up on a machine with an SSD attached to it, or to co-locate pods from two different services that communicate a lot into the same availability zone.


Steps
* Step One: Attach label to the node
* Step Two: Add a nodeSelector field to your pod configuration 



