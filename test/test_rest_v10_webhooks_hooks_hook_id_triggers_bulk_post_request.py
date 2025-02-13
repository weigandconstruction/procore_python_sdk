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

from procore_sdk.models.rest_v10_webhooks_hooks_hook_id_triggers_bulk_post_request import RestV10WebhooksHooksHookIdTriggersBulkPostRequest

class TestRestV10WebhooksHooksHookIdTriggersBulkPostRequest(unittest.TestCase):
    """RestV10WebhooksHooksHookIdTriggersBulkPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10WebhooksHooksHookIdTriggersBulkPostRequest:
        """Test RestV10WebhooksHooksHookIdTriggersBulkPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10WebhooksHooksHookIdTriggersBulkPostRequest`
        """
        model = RestV10WebhooksHooksHookIdTriggersBulkPostRequest()
        if include_optional:
            return RestV10WebhooksHooksHookIdTriggersBulkPostRequest(
                company_id = 5358233,
                api_version = 'v2',
                triggers = [
                    procore_sdk.models.company_trigger_trigger.company_trigger_trigger(
                        resource_name = 'Project Users', 
                        event_type = 'delete', )
                    ],
                project_id = 23498237
            )
        else:
            return RestV10WebhooksHooksHookIdTriggersBulkPostRequest(
                company_id = 5358233,
                api_version = 'v2',
                triggers = [
                    procore_sdk.models.company_trigger_trigger.company_trigger_trigger(
                        resource_name = 'Project Users', 
                        event_type = 'delete', )
                    ],
                project_id = 23498237,
        )
        """

    def testRestV10WebhooksHooksHookIdTriggersBulkPostRequest(self):
        """Test RestV10WebhooksHooksHookIdTriggersBulkPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
