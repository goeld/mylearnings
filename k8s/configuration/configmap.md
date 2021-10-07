* [Official Docs](https://kubernetes.io/docs/concepts/configuration/configmap/)

```shell
$ k create cm configmap --from-literal app=myapp
$ k create cm configmap --from-file=<path_to_file>
```

For volume
- configmap-name is required to load all the contents
- To load specific properties use items under the config map