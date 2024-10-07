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

from procore_sdk.models.rest_v10_projects_project_id_generic_tools_generic_tool_id_generic_tool_items_post_request import RestV10ProjectsProjectIdGenericToolsGenericToolIdGenericToolItemsPostRequest

class TestRestV10ProjectsProjectIdGenericToolsGenericToolIdGenericToolItemsPostRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdGenericToolsGenericToolIdGenericToolItemsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdGenericToolsGenericToolIdGenericToolItemsPostRequest:
        """Test RestV10ProjectsProjectIdGenericToolsGenericToolIdGenericToolItemsPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdGenericToolsGenericToolIdGenericToolItemsPostRequest`
        """
        model = RestV10ProjectsProjectIdGenericToolsGenericToolIdGenericToolItemsPostRequest()
        if include_optional:
            return RestV10ProjectsProjectIdGenericToolsGenericToolIdGenericToolItemsPostRequest(
                generic_tool_item = procore_sdk.models.the_generic_tool_item_object/.The Generic Tool Item object.(
                    description = 'Ready for review/approval on finishes.', 
                    due_date = 'Mon Aug 31 00:00:00 UTC 2020', 
                    position = 'interior-002', 
                    private = True, 
                    skip_emails = True, 
                    schedule_impact = 'no_impact', 
                    schedule_impact_value = 'none', 
                    cost_impact = 'no_impact', 
                    cost_impact_value = 'none', 
                    status = 'Open', 
                    title = 'Interior Finishes', 
                    received_from_id = 1386682, 
                    location_id = 1234, 
                    cost_code_id = 78261048, 
                    specification_section_id = 782356, 
                    trade_id = 779365, 
                    distribution_member_ids = [
                        56
                        ], 
                    assignee_ids = [
                        56
                        ], 
                    attachments = [
                        procore_sdk.models.rest_v10_work_order_contracts_post_201_response_attachments_inner.RestV10WorkOrderContractsPost_201_response_attachments_inner(
                            id = 5324, 
                            url = 'http://www.example.com/', 
                            filename = 'january_receipt_copy.jpg', )
                        ], 
                    custom_field_%{custom_field_definition_id} = custom field value, 
                    drawing_revision_ids = [4,5], 
                    file_version_ids = [6,7], 
                    form_ids = [7,8], 
                    image_ids = [9,10], 
                    upload_ids = ["4120226e-36a8-416f-970e-880bae78164f","de07e35a-4860-4f96-acd8-8360833dc495"], )
            )
        else:
            return RestV10ProjectsProjectIdGenericToolsGenericToolIdGenericToolItemsPostRequest(
                generic_tool_item = procore_sdk.models.the_generic_tool_item_object/.The Generic Tool Item object.(
                    description = 'Ready for review/approval on finishes.', 
                    due_date = 'Mon Aug 31 00:00:00 UTC 2020', 
                    position = 'interior-002', 
                    private = True, 
                    skip_emails = True, 
                    schedule_impact = 'no_impact', 
                    schedule_impact_value = 'none', 
                    cost_impact = 'no_impact', 
                    cost_impact_value = 'none', 
                    status = 'Open', 
                    title = 'Interior Finishes', 
                    received_from_id = 1386682, 
                    location_id = 1234, 
                    cost_code_id = 78261048, 
                    specification_section_id = 782356, 
                    trade_id = 779365, 
                    distribution_member_ids = [
                        56
                        ], 
                    assignee_ids = [
                        56
                        ], 
                    attachments = [
                        procore_sdk.models.rest_v10_work_order_contracts_post_201_response_attachments_inner.RestV10WorkOrderContractsPost_201_response_attachments_inner(
                            id = 5324, 
                            url = 'http://www.example.com/', 
                            filename = 'january_receipt_copy.jpg', )
                        ], 
                    custom_field_%{custom_field_definition_id} = custom field value, 
                    drawing_revision_ids = [4,5], 
                    file_version_ids = [6,7], 
                    form_ids = [7,8], 
                    image_ids = [9,10], 
                    upload_ids = ["4120226e-36a8-416f-970e-880bae78164f","de07e35a-4860-4f96-acd8-8360833dc495"], ),
        )
        """

    def testRestV10ProjectsProjectIdGenericToolsGenericToolIdGenericToolItemsPostRequest(self):
        """Test RestV10ProjectsProjectIdGenericToolsGenericToolIdGenericToolItemsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
