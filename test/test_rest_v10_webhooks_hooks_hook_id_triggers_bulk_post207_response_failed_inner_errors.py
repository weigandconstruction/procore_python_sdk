# coding: utf-8

"""
    Procore Rest API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Contact: apisupport@procore.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from procore_sdk.models.rest_v10_webhooks_hooks_hook_id_triggers_bulk_post207_response_failed_inner_errors import RestV10WebhooksHooksHookIdTriggersBulkPost207ResponseFailedInnerErrors

class TestRestV10WebhooksHooksHookIdTriggersBulkPost207ResponseFailedInnerErrors(unittest.TestCase):
    """RestV10WebhooksHooksHookIdTriggersBulkPost207ResponseFailedInnerErrors unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10WebhooksHooksHookIdTriggersBulkPost207ResponseFailedInnerErrors:
        """Test RestV10WebhooksHooksHookIdTriggersBulkPost207ResponseFailedInnerErrors
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10WebhooksHooksHookIdTriggersBulkPost207ResponseFailedInnerErrors`
        """
        model = RestV10WebhooksHooksHookIdTriggersBulkPost207ResponseFailedInnerErrors()
        if include_optional:
            return RestV10WebhooksHooksHookIdTriggersBulkPost207ResponseFailedInnerErrors(
                event_type = 'Can't be blank'
            )
        else:
            return RestV10WebhooksHooksHookIdTriggersBulkPost207ResponseFailedInnerErrors(
        )
        """

    def testRestV10WebhooksHooksHookIdTriggersBulkPost207ResponseFailedInnerErrors(self):
        """Test RestV10WebhooksHooksHookIdTriggersBulkPost207ResponseFailedInnerErrors"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
