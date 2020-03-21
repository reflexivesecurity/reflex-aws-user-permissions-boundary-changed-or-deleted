# reflex-aws-user-permissions-boundary-changed-or-deleted
TODO: Write a brief description of your rule and what it does.

## Usage
To use this rule either add it to your `reflex.yaml` configuration file:  
```
rules:
  - reflex-aws-user-permissions-boundary-changed-or-deleted:
      version: latest
```

or add it directly to your Terraform:  
```
...

module "reflex-aws-user-permissions-boundary-changed-or-deleted" {
  source           = "github.com/cloudmitigator/reflex-aws-user-permissions-boundary-changed-or-deleted"
}

...
```

## License
This Reflex rule is made available under the MPL 2.0 license. For more information view the [LICENSE](https://github.com/cloudmitigator/reflex-aws-user-permissions-boundary-changed-or-deleted/blob/master/LICENSE) 