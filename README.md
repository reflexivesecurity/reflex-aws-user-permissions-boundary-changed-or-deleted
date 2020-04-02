# reflex-aws-user-permissions-boundary-changed-or-deleted
A Reflex rule for detecting the modification or deletion of an IAM User permission boundary.

Note: This rule does _not_ detect the modification of permissions of an IAM Policy that is
actively being used as a permission boundary. It detects when an IAM Policy is attached
to a User as a Permissions Boundary, or when a Permissions Boundary is removed from a User.

To learn more about IAM User permission boundaries, see [the AWS Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html).

## Getting Started
To get started using Reflex, check out [the Reflex Documentation](https://docs.cloudmitigator.com/).

## Usage
To use this rule either add it to your `reflex.yaml` configuration file:  
```
rules:
  aws:
    - user-permissions-boundary-changed-or-deleted:
        version: latest
```

or add it directly to your Terraform:  
```
module "user-permissions-boundary-changed-or-deleted" {
  source            = "git::https://github.com/cloudmitigator/reflex-aws-user-permissions-boundary-changed-or-deleted.git?ref=latest"
  sns_topic_arn     = module.central-sns-topic.arn
  reflex_kms_key_id = module.reflex-kms-key.key_id
}
```

Note: The `sns_topic_arn` and `reflex_kms_key_id` example values shown here assume you generated resources with `reflex build`. If you are using the Terraform on its own you need to provide your own valid values.

## Configuration
This rule has no configuration options.

## Contributing
If you are interested in contributing, please review [our contribution guide](https://docs.cloudmitigator.com/about/contributing.html).

## License
This Reflex rule is made available under the MPL 2.0 license. For more information view the [LICENSE](https://github.com/cloudmitigator/reflex-aws-user-permissions-boundary-changed-or-deleted/blob/master/LICENSE) 
