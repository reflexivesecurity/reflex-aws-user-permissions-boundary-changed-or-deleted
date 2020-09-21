""" Module for UserPermissionsBoundaryChangedOrDeleted """

import json

from reflex_core import AWSRule, subscription_confirmation


class UserPermissionsBoundaryChangedOrDeleted(AWSRule):
    """ Rule for detecting the modification or deletion of IAM User permission boundary """

    def __init__(self, event):
        super().__init__(event)

    def extract_event_data(self, event):
        """ Extract required event data """
        self.event_name = event["detail"]["eventName"]
        self.user_name = event["detail"]["requestParameters"]["userName"]

        if self.event_name == "PutUserPermissionsBoundary":
            self.permissions_boundary = event["detail"]["requestParameters"][
                "permissionsBoundary"
            ]

    def resource_compliant(self):
        """
        Determine if the resource is compliant with your rule.

        Return True if it is compliant, and False if it is not.
        """
        # We simply want to know when these events occur. Since this rule was
        # triggered we know that happened, and we want to alert. Therefore
        # the resource is never compliant.
        return False

    def get_remediation_message(self):
        """ Returns a message about the remediation action that occurred """
        if self.event_name == "PutUserPermissionsBoundary":
            return (
                f"The IAM User {self.user_name} had a new User Permissions Boundary set."
                f"The new Permissions boundary is {self.permissions_boundary}"
            )
        return (
            f"The IAM User {self.user_name} had its User Permissions Boundary deleted."
        )


def lambda_handler(event, _):
    """ Handles the incoming event """
    print(event)
    event_payload = json.loads(event["Records"][0]["body"])
    if subscription_confirmation.is_subscription_confirmation(event_payload):
        subscription_confirmation.confirm_subscription(event_payload)
        return
    rule = UserPermissionsBoundaryChangedOrDeleted(event_payload)
    rule.run_compliance_rule()
