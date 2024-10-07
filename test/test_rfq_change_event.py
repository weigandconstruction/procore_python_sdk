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

from procore_sdk.models.rfq_change_event import RFQChangeEvent

class TestRFQChangeEvent(unittest.TestCase):
    """RFQChangeEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RFQChangeEvent:
        """Test RFQChangeEvent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RFQChangeEvent`
        """
        model = RFQChangeEvent()
        if include_optional:
            return RFQChangeEvent(
                id = 43453,
                number = 14,
                alphanumeric_number = 'A14',
                origin_data = 'OD-123654789',
                origin_id = '654987123',
                title = 'Bathtub replacement',
                description = 'Replace the bathtub in the bathroom',
                status = 'Pending - Revised',
                project_id = 23446,
                created_at = '2012-10-23T21:39:40Z',
                updated_at = '2012-10-24T21:39:40Z',
                event_type = 'tbd',
                event_scope = 'in_scope',
                change_event_origin_id = 34523,
                change_event_origin_type = 'Rfi::Header',
                rfi = procore_sdk.models.rfq_change_event_rfi.RFQ_change_event_rfi(
                    id = 34523, 
                    title = 'Electrical panel obstructed', 
                    number = 3, 
                    due_date = '2016-11-23T21:39:40Z', 
                    status = 'draft', ),
                change_event_line_items = [
                    procore_sdk.models.rfq_change_event_change_event_line_items_inner.RFQ_change_event_change_event_line_items_inner(
                        id = 345236, 
                        cost_code_biller_name = 'Campus', 
                        cost_code = null, 
                        cost_code_is_budgeted = True, 
                        description = 'Add caulk to bathtub base', 
                        event_id = 623153, 
                        line_item_type = procore_sdk.models.line_item_type.LineItemType(
                            id = 12345, 
                            name = 'Equipment', 
                            code = 'LB', 
                            base_type = 'materials', 
                            origin_data = 'OD-2398273424', 
                            origin_id = 'ABC123', ), 
                        rom = 17705, 
                        contract = procore_sdk.models.rfq_change_event_change_event_line_items_inner_contract.RFQ_change_event_change_event_line_items_inner_contract(
                            id = 11353, 
                            number = '001', ), 
                        links = procore_sdk.models.rfq_change_event_change_event_line_items_inner_links.RFQ_change_event_change_event_line_items_inner_links(
                            edit = 'https://app.procore.com/22585/project/change_events/events/344096/edit?celi_id=336014#336014', 
                            view = 'https://app.procore.com/22585/project/change_events/events/344096?celi_id=336014#336014', 
                            prime_pco_cost = '', 
                            commitment_contract_cost = '', 
                            commitment_pco_cost = '', 
                            rfq_amount = '', 
                            rom = '', ), 
                        statuses = procore_sdk.models.rfq_change_event_change_event_line_items_inner_statuses.RFQ_change_event_change_event_line_items_inner_statuses(
                            commitment_contract_cost = '', 
                            commitment_pco_cost = '', 
                            prime_pco_cost = '', 
                            rfq_amount = '', ), 
                        number = '52225', 
                        status = 'Open', 
                        title = 'Example Title', 
                        vendor = procore_sdk.models.rest_v10_projects_project_id_waste_logs_get_200_response_inner_vendor.RestV10ProjectsProjectIdWasteLogsGet_200_response_inner_vendor(
                            id = 161072, 
                            name = 'SID Architecture', ), 
                        commitment_contract_cost = '0.0', 
                        commitment_pco_cost = '1240.0', 
                        budget_mod_amount = '4500.0', 
                        budget_mod = procore_sdk.models.rfq_change_event_change_event_line_items_inner_budget_mod.RFQ_change_event_change_event_line_items_inner_budget_mod(
                            created_at = '2016-10-23T21:39:40Z', 
                            transfer_amount = '4500.0', 
                            notes = 'Transfer money for extra concrete.', 
                            from_budget_line_item_id = 348383, 
                            to_budget_line_item_id = 4034034, ), 
                        prime_pco_cost = '4500.0', 
                        rfq_amount = '1000.0', 
                        rfq_status = 'Out for Pricing', )
                    ],
                change_order_change_reason = procore_sdk.models.rfq_change_event_change_order_change_reason.RFQ_change_event_change_order_change_reason(
                    id = 3452, 
                    company_id = 2342, 
                    change_reason = 'Allowance', 
                    show_in_select = True, ),
                change_event_status = procore_sdk.models.rfq_change_event_change_event_status.RFQ_change_event_change_event_status(
                    id = 29715, 
                    name = 'Pending - Revised', 
                    mapped_to_status = 'pending', 
                    show_in_select = True, ),
                created_by = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                    id = 160586, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
                attachments = [
                    procore_sdk.models.rfq_quote_attachments_inner.RFQ_Quote_attachments_inner(
                        id = 56, 
                        name = 'filename.ext', 
                        url = 'https://storage.procore.com/v3/d/default/procore-files/1ZE258W9K804SAJJZX19JVAB3R?sig=e7a476ec0a46154d05e0d4a554fb2ea0904cb6604670f9247c54d7c56a84d0b6', )
                    ]
            )
        else:
            return RFQChangeEvent(
        )
        """

    def testRFQChangeEvent(self):
        """Test RFQChangeEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
