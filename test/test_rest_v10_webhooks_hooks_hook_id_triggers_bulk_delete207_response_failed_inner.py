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

from procore_sdk.models.rest_v10_webhooks_hooks_hook_id_triggers_bulk_delete207_response_failed_inner import RestV10WebhooksHooksHookIdTriggersBulkDelete207ResponseFailedInner

class TestRestV10WebhooksHooksHookIdTriggersBulkDelete207ResponseFailedInner(unittest.TestCase):
    """RestV10WebhooksHooksHookIdTriggersBulkDelete207ResponseFailedInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10WebhooksHooksHookIdTriggersBulkDelete207ResponseFailedInner:
        """Test RestV10WebhooksHooksHookIdTriggersBulkDelete207ResponseFailedInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10WebhooksHooksHookIdTriggersBulkDelete207ResponseFailedInner`
        """
        model = RestV10WebhooksHooksHookIdTriggersBulkDelete207ResponseFailedInner()
        if include_optional:
            return RestV10WebhooksHooksHookIdTriggersBulkDelete207ResponseFailedInner(
                code = '403',
                trigger = 43
            )
        else:
            return RestV10WebhooksHooksHookIdTriggersBulkDelete207ResponseFailedInner(
        )
        """

    def testRestV10WebhooksHooksHookIdTriggersBulkDelete207ResponseFailedInner(self):
        """Test RestV10WebhooksHooksHookIdTriggersBulkDelete207ResponseFailedInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
