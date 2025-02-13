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

from procore_sdk.models.rest_v10_change_events_get200_response_inner import RestV10ChangeEventsGet200ResponseInner

class TestRestV10ChangeEventsGet200ResponseInner(unittest.TestCase):
    """RestV10ChangeEventsGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ChangeEventsGet200ResponseInner:
        """Test RestV10ChangeEventsGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ChangeEventsGet200ResponseInner`
        """
        model = RestV10ChangeEventsGet200ResponseInner()
        if include_optional:
            return RestV10ChangeEventsGet200ResponseInner(
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
                deleted_at = '2017-07-29T21:39:40Z',
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
                    procore_sdk.models.rest_v10_change_events_get_200_response_inner_change_event_line_items_inner.RestV10ChangeEventsGet_200_response_inner_change_event_line_items_inner(
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
                        cost_code = null, 
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
                            commitment_contract_cost = 'https://app.procore.com/1513513/project/commitments/purchase_order_contracts/1/schedule_of_values', 
                            commitment_pco_cost = 'https://app.procore.com/1513513/project/commitments/purchase_order_contracts/3/change_orders/potential_change_orders/20?subtab=line_items', 
                            rfq_amount = 'https://app.procore.com/1513513/project/commitments/purchase_order_contracts/1/request_for_quotes/2', 
                            rom = 'https://app.procore.com/1513513/project/change_events/events/639?celi_id=456#456', 
                            prime_pco_cost = 'https://app.procore.com/1513513/project/prime_contract/change_orders/potential_change_orders/25?subtab=line_items', ), 
                        statuses = procore_sdk.models.rest_v10_change_events_get_200_response_inner_change_event_line_items_inner_statuses.RestV10ChangeEventsGet_200_response_inner_change_event_line_items_inner_statuses(
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
                            currency_iso_code = 'USD', ), )
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
                    procore_sdk.models.rest_v10_work_order_contracts_post_201_response_attachments_inner.RestV10WorkOrderContractsPost_201_response_attachments_inner(
                        id = 5324, 
                        url = 'http://www.example.com/', 
                        filename = 'january_receipt_copy.jpg', )
                    ],
                rfqs = [
                    procore_sdk.models.rfq.RFQ(
                        id = 1199, 
                        commitment_contract_id = 418232, 
                        created_at = '2016-06-30T20:41:58Z', 
                        deleted_at = '2016-08-30T18:11:43Z', 
                        description = 'Please see attached documentation for Bulletin 3 and provide pricing within 1 week. If you don't get back to me, I'll assume you have no cost impact.', 
                        due_date = 'Thu Oct 13 00:00:00 UTC 2016', 
                        estimated_amount = 4302.0, 
                        estimated_schedule_impact = 2, 
                        estimated_status = 'rom', 
                        intent_to_quote = False, 
                        number = '013', 
                        original_quote = 4500.0, 
                        position = 13, 
                        private = True, 
                        prostore_file_ids = [3423484,6983730,2736492], 
                        status = 'under_review', 
                        title = 'Field Bulletin #3 - Steel staircase on roof', 
                        updated_at = '2016-08-30T18:11:43Z', 
                        specification_section = procore_sdk.models.rfq_specification_section.RFQ_specification_section(
                            specification_section_id = 32379, 
                            spec_section_description = 'Steel Structure', 
                            spec_section_number = '236400', ), 
                        quotes = [
                            procore_sdk.models.rfq_quote.RFQ Quote(
                                id = 105445, 
                                commitment_quote_number = '2234', 
                                cost = 4500.0, 
                                schedule_impact = 2, 
                                description = 'Need to destroy some of the roofing to install this staircase.', 
                                request_for_quote_id = 136264, 
                                attachments_count = 1, 
                                import_origin_id = 'QWA44H', 
                                created_by_id = 5136213, 
                                created_at = '2016-10-21T21:39:41Z', 
                                deleted_at = '2016-10-23T21:44:45Z', 
                                updated_at = '2016-10-22T21:41:42Z', 
                                prostore_file_ids = [2334,776843,22456], 
                                created_by = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                                    id = 160586, 
                                    login = 'carl.contractor@example.com', 
                                    name = 'Carl Contractor', ), )
                            ], 
                        responses = [
                            procore_sdk.models.rfq_response.RFQ Response(
                                id = 105, 
                                comment = 'This quote needs to be revised. See attached files.', 
                                created_at = '2016-10-22T21:39:40Z', 
                                deleted_at = '2016-10-30T21:39:40Z', 
                                updated_at = '2016-10-26T21:39:40Z', 
                                prostore_file_ids = [3453247,6543893,3476145], )
                            ], 
                        potential_change_orders = procore_sdk.models.rfq_potential_change_orders.RFQ_potential_change_orders(
                            id = 570623, 
                            created_at = '2012-10-23T21:39:40Z', 
                            created_by_id = 12, 
                            deleted_at = '2012-11-24T21:39:40Z', 
                            due_date = 'Fri Nov 23 00:00:00 UTC 2012', 
                            invoiced_date = 'Wed Oct 24 00:00:00 UTC 2012', 
                            number = '004', 
                            paid_date = 'Wed Nov 21 00:00:00 UTC 2012', 
                            reviewed_at = '2012-10-23T21:44:40Z', 
                            title = 'Field Bulletin #3 - Steel staircase on roof', 
                            status = 'approved', 
                            updated_at = '2012-11-23T21:39:40Z', 
                            change_order_request_id = 283764, 
                            executed = False, 
                            grand_total = '3329738.0', 
                            revision = 4, 
                            schedule_impact_amount = 2, 
                            change_reason = 'Deleted', 
                            change_order_request_title = 'Concrete freezer slab', 
                            change_order_package_title = 'Concrete freezer slab', 
                            potential_change_order_acronym_number = 'PCO 95', 
                            change_order_request_acronym_number = 'COR 9001', 
                            change_order_package_acronym_number = 'CCO 42', 
                            change_order_tiers = 3, ), 
                        change_order_packages = procore_sdk.models.rfq_change_order_packages.RFQ_change_order_packages(
                            id = 458661, 
                            contract_id = 64545, 
                            created_at = '2012-10-23T21:39:40Z', 
                            deleted_at = '2017-07-29T21:39:40Z', 
                            due_date = 'Fri Nov 23 00:00:00 UTC 2012', 
                            invoiced_date = 'Wed Oct 24 00:00:00 UTC 2012', 
                            number = '002', 
                            origin_data = 'OD-123654789', 
                            origin_id = '654987123', 
                            paid_date = 'Wed Nov 21 00:00:00 UTC 2012', 
                            reviewed_at = '2012-11-23T21:39:40Z', 
                            title = 'November Changes', 
                            status = 'approved', 
                            updated_at = '2012-11-23T21:39:40Z', ), 
                        commitment_potential_change_orders = procore_sdk.models.rfq_potential_change_orders.RFQ_potential_change_orders(
                            id = 570623, 
                            created_at = '2012-10-23T21:39:40Z', 
                            created_by_id = 12, 
                            deleted_at = '2012-11-24T21:39:40Z', 
                            due_date = 'Fri Nov 23 00:00:00 UTC 2012', 
                            invoiced_date = 'Wed Oct 24 00:00:00 UTC 2012', 
                            number = '004', 
                            paid_date = 'Wed Nov 21 00:00:00 UTC 2012', 
                            reviewed_at = '2012-10-23T21:44:40Z', 
                            title = 'Field Bulletin #3 - Steel staircase on roof', 
                            status = 'approved', 
                            updated_at = '2012-11-23T21:39:40Z', 
                            change_order_request_id = 283764, 
                            executed = False, 
                            grand_total = '3329738.0', 
                            revision = 4, 
                            schedule_impact_amount = 2, 
                            change_reason = 'Deleted', 
                            change_order_request_title = 'Concrete freezer slab', 
                            change_order_package_title = 'Concrete freezer slab', 
                            potential_change_order_acronym_number = 'PCO 95', 
                            change_order_request_acronym_number = 'COR 9001', 
                            change_order_package_acronym_number = 'CCO 42', 
                            change_order_tiers = 3, ), 
                        commitment_change_order_packages = procore_sdk.models.rfq_change_order_packages.RFQ_change_order_packages(
                            id = 458661, 
                            contract_id = 64545, 
                            created_at = '2012-10-23T21:39:40Z', 
                            deleted_at = '2017-07-29T21:39:40Z', 
                            due_date = 'Fri Nov 23 00:00:00 UTC 2012', 
                            invoiced_date = 'Wed Oct 24 00:00:00 UTC 2012', 
                            number = '002', 
                            origin_data = 'OD-123654789', 
                            origin_id = '654987123', 
                            paid_date = 'Wed Nov 21 00:00:00 UTC 2012', 
                            reviewed_at = '2012-11-23T21:39:40Z', 
                            title = 'November Changes', 
                            status = 'approved', 
                            updated_at = '2012-11-23T21:39:40Z', ), 
                        created_by = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                            id = 160586, 
                            login = 'carl.contractor@example.com', 
                            name = 'Carl Contractor', ), 
                        assigned = , 
                        location = procore_sdk.models.location.Location(
                            id = 15504, 
                            name = '1space>1 space', 
                            node_name = '1 space', 
                            parent_id = 788866, 
                            created_at = '2016-08-01T23:33:54Z', 
                            updated_at = '2016-08-01T23:33:54Z', ), 
                        cost_code = null, )
                    ],
                currency_configuration = procore_sdk.models.rfq_currency_configuration.RFQ_currency_configuration(
                    currency_iso_code = 'USD', )
            )
        else:
            return RestV10ChangeEventsGet200ResponseInner(
        )
        """

    def testRestV10ChangeEventsGet200ResponseInner(self):
        """Test RestV10ChangeEventsGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
