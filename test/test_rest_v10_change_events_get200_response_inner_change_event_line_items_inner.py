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

from procore_sdk.models.rest_v10_change_events_get200_response_inner_change_event_line_items_inner import RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner

class TestRestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner(unittest.TestCase):
    """RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner:
        """Test RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner`
        """
        model = RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner()
        if include_optional:
            return RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner(
                id = 345236,
                budget_code = procore_sdk.models.rest_v10_change_events_get_200_response_inner_change_event_line_items_inner_budget_code.RestV10ChangeEventsGet_200_response_inner_change_event_line_items_inner_budget_code(
                    id = 1, 
                    flat_code = 'O.01-511', 
                    description = 'Earthwork.Materials', 
                    segment_items = [
                        procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get_200_response_inner.RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet_200_response_inner(
                            id = 456, 
                            code = '01-222', 
                            name = 'Lighting', 
                            created_at = '2016-06-30T20:41:58Z', 
                            updated_at = '2016-08-30T18:11:43Z', 
                            parent_id = 123, 
                            path_ids = [123,456], 
                            path_code = 'a', 
                            is_parent = False, 
                            path_codes = ["01 - Requirements","01-222 - Lighting"], 
                            path_names = ["01 - Requirements","01-222 - Lighting"], 
                            in_use = True, 
                            segment = {"id":3,"name":"Cost Code","type":"cost_code","position":1,"delimiter":".","required":true,"segment_items_count":2,"project_can_modify_origin_project":true,"project_can_delete_origin_company":true,"structure":"tiered","created_at":"2016-06-30T20:41:58Z","updated_at":"2016-08-30T18:11:43Z","wbs_pattern_id":4567}, 
                            status = 'active', )
                        ], ),
                cost_code_biller_name = 'Eemer Oakland',
                cost_code = None,
                cost_code_is_budgeted = True,
                description = 'Add caulk to bathtub base',
                event_id = 151512,
                line_item_type = procore_sdk.models.line_item_type.LineItemType(
                    id = 12345, 
                    name = 'Equipment', 
                    code = 'LB', 
                    base_type = 'materials', 
                    origin_data = 'OD-2398273424', 
                    origin_id = 'ABC123', ),
                rom = 17705,
                contract = procore_sdk.models.rest_v10_change_events_get_200_response_inner_change_event_line_items_inner_contract.RestV10ChangeEventsGet_200_response_inner_change_event_line_items_inner_contract(
                    id = 853215, 
                    number = '001', 
                    title = 'PO--001', 
                    name = 'PO--001', ),
                links = procore_sdk.models.rest_v10_change_events_get_200_response_inner_change_event_line_items_inner_links.RestV10ChangeEventsGet_200_response_inner_change_event_line_items_inner_links(
                    edit = 'https://app.procore.com/1513513/project/change_events/events/151512/edit?celi_id=345236#345236', 
                    view = 'https://app.procore.com/1513513/project/change_events/events/151512?celi_id=345236#345236', 
                    contract = 'https://app.procore.com/1513513/project/commitments/purchase_order_contracts/853215', 
                    commitment_contract_cost = 'https://app.procore.com/1513513/project/commitments/purchase_order_contracts/1/schedule_of_values', 
                    commitment_pco_cost = 'https://app.procore.com/1513513/project/commitments/purchase_order_contracts/3/change_orders/potential_change_orders/20?subtab=line_items', 
                    rfq_amount = 'https://app.procore.com/1513513/project/commitments/purchase_order_contracts/1/request_for_quotes/2', 
                    rom = 'https://app.procore.com/1513513/project/change_events/events/639?celi_id=456#456', 
                    prime_pco_cost = 'https://app.procore.com/1513513/project/prime_contract/change_orders/potential_change_orders/25?subtab=line_items', ),
                statuses = procore_sdk.models.rest_v10_change_events_get_200_response_inner_change_event_line_items_inner_statuses.RestV10ChangeEventsGet_200_response_inner_change_event_line_items_inner_statuses(
                    contract = 'Approved', 
                    commitment_contract_cost = 'Draft', 
                    commitment_contract_tooltip = 'PO--001: (no title), Approved', 
                    commitment_pco_cost = 'Draft', 
                    commitment_pco_tooltip = 'PCO #001: CE #400 - CE 400, Draft', 
                    rfq_amount = 'Out for Pricing', 
                    rfq_tooltip = 'RFQ #002: CE #429 - RFI 111, Out for Pricing', 
                    prime_pco_cost = 'Draft', 
                    prime_pco_tooltip = 'PCO #001: CE #428 - RFI 111, Draft', ),
                number = '428',
                status = 'Change Event Status 1',
                title = 'CE #429 - RFI 111',
                vendor = procore_sdk.models.rest_v10_projects_project_id_waste_logs_get_200_response_inner_vendor.RestV10ProjectsProjectIdWasteLogsGet_200_response_inner_vendor(
                    id = 161072, 
                    name = 'SID Architecture', ),
                biller = procore_sdk.models.rest_v10_change_events_get_200_response_inner_change_event_line_items_inner_biller.RestV10ChangeEventsGet_200_response_inner_change_event_line_items_inner_biller(
                    id = 115513, 
                    name = 'Eemer Oakland', 
                    model_name = 'Project', 
                    guid = 'Z2lkOi8vcHJvY29yZS9Qcm9qZWN0LzE', ),
                proposed_vendor_id = 5,
                proposed_contract_id = 4,
                uom = 'hours',
                estimated_cost_amount = '13531.0',
                estimated_cost_quantity = 125.5,
                estimated_cost_unit_cost = 75.5,
                estimated_cost_calculation_strategy = 'manual',
                line_item_type_id = 12345,
                cost_code_id = 12345,
                editable = False,
                deletable = False,
                request_for_quote_id = 12345,
                biller_guid = 'Z2lkOi8vcHJvY29yZS9Qcm9qZWN0LzE',
                commitment_contract_cost = '155524.00',
                commitment_pco_cost = '0.0',
                budget_mod_amount = '0',
                budget_mod = procore_sdk.models.rest_v10_change_events_get_200_response_inner_change_event_line_items_inner_budget_mod.RestV10ChangeEventsGet_200_response_inner_change_event_line_items_inner_budget_mod(
                    created_at = '2016-10-23T21:39:40Z', 
                    transfer_amount = '4500.0', 
                    notes = 'Transfer money for extra concrete.', 
                    from_budget_line_item_id = 348383, 
                    to_budget_line_item_id = 4034034, 
                    from_budget_line_item_name = 'Source Line Item', 
                    to_budget_line_item_name = 'Target Line Item', ),
                prime_pco_cost = '0.0',
                rfq_amount = '1111.00',
                rfq_sent = 'Out for Pricing',
                currency_configuration = procore_sdk.models.rfq_currency_configuration.RFQ_currency_configuration(
                    currency_iso_code = 'USD', )
            )
        else:
            return RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner(
        )
        """

    def testRestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner(self):
        """Test RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
