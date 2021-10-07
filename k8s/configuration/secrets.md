
```shell
$ k create secret generic my-secrets-literal --from-literal user=username --from-literal password=userpassword
$ k create secret generic my-secrets --from-file=configuration/secrets.properties
$ kubectl get secrets
$ kubectl create secret generic my-secret --from-literal=dbpass=dbpass
$ kubectl create secret generic my-secret --from-literal=user=admin --from-literal=pass=12345

from file
from environment variables
```


