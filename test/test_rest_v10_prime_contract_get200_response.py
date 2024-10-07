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

from procore_sdk.models.rest_v10_prime_contract_get200_response import RestV10PrimeContractGet200Response

class TestRestV10PrimeContractGet200Response(unittest.TestCase):
    """RestV10PrimeContractGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10PrimeContractGet200Response:
        """Test RestV10PrimeContractGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10PrimeContractGet200Response`
        """
        model = RestV10PrimeContractGet200Response()
        if include_optional:
            return RestV10PrimeContractGet200Response(
                id = 34219,
                accounting_method = 'amount',
                actual_completion_date = 'Thu Dec 31 00:00:00 UTC 2015',
                allow_comments = True,
                allow_markups = False,
                allow_payment_applications = True,
                allow_payments = True,
                allow_redistributions = False,
                approval_letter_date = 'Thu Jan 02 00:00:00 UTC 2014',
                approved_change_orders = '3434.0',
                bill_to = '5000 Construction Street',
                budget_line_item_id = 50123,
                contract_date = 'Thu Jan 02 00:00:00 UTC 2014',
                contract_estimated_completion_date = 'Sun Jan 31 00:00:00 UTC 2016',
                contract_start_date = 'Fri Jan 31 00:00:00 UTC 2014',
                contract_termination_date = 'Sat Dec 31 00:00:00 UTC 2016',
                created_at = '2014-01-01T21:55:10Z',
                deleted_at = '2017-01-04T23:55:19Z',
                delivery_date = 'Sat Feb 15 00:00:00 UTC 2014',
                description = '<p>Owner Contract</p>',
                display_materials_retainage = True,
                display_stored_materials = False,
                display_work_retainage = True,
                draft_change_orders_amount = '750.00',
                exclusions = '<p>Interior finishing</p>',
                executed = True,
                execution_date = 'Thu Jan 02 00:00:00 UTC 2014',
                grand_total = '57750.0',
                inclusions = '',
                issued_on_date = 'Thu Jan 02 00:00:00 UTC 2014',
                letter_of_intent_date = 'Thu Jan 02 00:00:00 UTC 2014',
                line_items_extended_total = '55000.0',
                line_items_total = '50000.0',
                number = 'A-1',
                origin_data = 'XYZ-012',
                origin_id = 'abc-123',
                outstanding_balance = '750.00',
                owner_invoices_amount = '750.00',
                payment_terms = 'Net 30',
                pending_change_orders_amount = '750.00',
                pending_revised_contract_amount = '750.00',
                percentage_paid = '23.0',
                position = 2,
                private = True,
                requisition_number = '2011',
                retainage_percent = '10',
                returned_date = 'Thu Jan 02 00:00:00 UTC 2014',
                revised_contract_amount = '750.00',
                ship_to = '<p>5000 Construction Street</p>',
                ship_via = 'Your truck',
                signed_contract_received_date = 'Sat Feb 15 00:00:00 UTC 2014',
                show_line_items_to_non_admins = True,
                status = 'Approved',
                title = 'ABC Owner Contract',
                total_payments = '0.0',
                type = 'PrimeContract',
                updated_at = '2016-01-04T23:55:19Z',
                original_substantial_completion_date = 'Mon Nov 06 00:00:00 UTC 2017',
                substantial_completion_date = 'Mon Oct 30 00:00:00 UTC 2017',
                architect = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                    id = 160586, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
                assigned_to = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                    id = 160586, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
                attachments = [
                    procore_sdk.models.rest_v10_work_order_contracts_post_201_response_attachments_inner.RestV10WorkOrderContractsPost_201_response_attachments_inner(
                        id = 5324, 
                        url = 'http://www.example.com/', 
                        filename = 'january_receipt_copy.jpg', )
                    ],
                change_order_packages = [
                    procore_sdk.models.rest_v10_work_order_contracts_post_201_response_change_order_packages_inner.RestV10WorkOrderContractsPost_201_response_change_order_packages_inner(
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
                        updated_at = '2012-11-23T21:39:40Z', 
                        currency_configuration = procore_sdk.models.rest_v10_work_order_contracts_get_200_response_inner_currency_configuration.RestV10WorkOrderContractsGet_200_response_inner_currency_configuration(
                            currency_iso_code = 'USD', ), )
                    ],
                change_order_requests = [
                    [
                        procore_sdk.models.rest_v10_work_order_contracts_post_201_response_change_order_requests_inner_inner.RestV10WorkOrderContractsPost_201_response_change_order_requests_inner_inner(
                            id = 3284756, 
                            created_at = '2016-10-23T21:39:40Z', 
                            deleted_at = '2017-07-29T21:39:40Z', 
                            due_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                            invoiced_date = 'Tue Aug 22 00:00:00 UTC 2017', 
                            number = 'B22', 
                            paid_date = 'Fri Aug 25 00:00:00 UTC 2017', 
                            status = 'draft', 
                            title = 'Concrete freezer slab', 
                            updated_at = '2016-10-25T21:39:40Z', 
                            currency_configuration = procore_sdk.models.rest_v10_work_order_contracts_get_200_response_inner_currency_configuration.RestV10WorkOrderContractsGet_200_response_inner_currency_configuration(
                                currency_iso_code = 'USD', ), )
                        ]
                    ],
                contractor = None,
                cost_code = None,
                created_by = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                    id = 160586, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
                line_items = [
                    procore_sdk.models.rest_v10_work_order_contracts_post_201_response_line_items_inner.RestV10WorkOrderContractsPost_201_response_line_items_inner(
                        id = 4896147, 
                        amount = '1000.0', 
                        company = procore_sdk.models.rest_v10_work_order_contracts_post_201_response_line_items_inner_company.RestV10WorkOrderContractsPost_201_response_line_items_inner_company(
                            id = 163215, 
                            name = 'Procore Tech', ), 
                        wbs_code = procore_sdk.models.rest_v10_work_order_contracts_post_201_response_line_items_inner_wbs_code.RestV10WorkOrderContractsPost_201_response_line_items_inner_wbs_code(
                            id = 999, 
                            flat_code = '01-011.CT1', 
                            description = 'Project Engineer.Cost Type 1', ), 
                        cost_code = null, 
                        created_at = '2016-08-01T23:33:54Z', 
                        description = 'Cleanup', 
                        extended_type = 'calculated', 
                        holder = procore_sdk.models.rest_v10_work_order_contracts_post_201_response_line_items_inner_holder.RestV10WorkOrderContractsPost_201_response_line_items_inner_holder(
                            id = 233245, 
                            holder_type = 'WorkOrderContract', ), 
                        line_item_type = procore_sdk.models.line_item_type.LineItemType(
                            id = 12345, 
                            name = 'Equipment', 
                            code = 'LB', 
                            base_type = 'materials', 
                            origin_data = 'OD-2398273424', 
                            origin_id = 'ABC123', ), 
                        origin_data = 'OD-39823232', 
                        origin_id = '239233', 
                        position = 1, 
                        project = procore_sdk.models.rest_v10_work_order_contracts_get_200_response_inner_project.RestV10WorkOrderContractsGet_200_response_inner_project(
                            id = 123456, 
                            name = 'Children's Hospital', ), 
                        quantity = '10.0', 
                        tax_code_id = 1, 
                        total_amount = '1000.0', 
                        extended_amount = '900.0', 
                        unit_cost = '100.0', 
                        uom = 'Lbs', 
                        updated_at = '2016-09-01T21:33:54Z', 
                        change_event_line_item = procore_sdk.models.rest_v10_work_order_contracts_post_201_response_line_items_inner_change_event_line_item.RestV10WorkOrderContractsPost_201_response_line_items_inner_change_event_line_item(
                            id = 5, 
                            cost_rom = '100.0', 
                            revenue_rom = '200.0', 
                            event_id = 6, 
                            currency_configuration = procore_sdk.models.rest_v10_work_order_contracts_get_200_response_inner_currency_configuration.RestV10WorkOrderContractsGet_200_response_inner_currency_configuration(
                                currency_iso_code = 'USD', ), ), 
                        currency_configuration = procore_sdk.models.rest_v10_work_order_contracts_get_200_response_inner_currency_configuration.RestV10WorkOrderContractsGet_200_response_inner_currency_configuration(
                            currency_iso_code = 'USD', ), )
                    ],
                potential_change_orders = [
                    procore_sdk.models.rest_v10_work_order_contracts_post_201_response_potential_change_orders_inner.RestV10WorkOrderContractsPost_201_response_potential_change_orders_inner(
                        id = 570623, 
                        created_at = '2012-10-23T21:39:40Z', 
                        deleted_at = '2012-11-24T21:39:40Z', 
                        due_date = 'Fri Nov 23 00:00:00 UTC 2012', 
                        invoiced_date = 'Wed Oct 24 00:00:00 UTC 2012', 
                        number = '004', 
                        paid_date = 'Wed Nov 21 00:00:00 UTC 2012', 
                        reviewed_at = '2012-10-23T21:44:40Z', 
                        title = 'Field Bulletin #3 - Steel staircase on roof', 
                        status = 'approved', 
                        updated_at = '2012-11-23T21:39:40Z', 
                        currency_configuration = procore_sdk.models.rest_v10_work_order_contracts_get_200_response_inner_currency_configuration.RestV10WorkOrderContractsGet_200_response_inner_currency_configuration(
                            currency_iso_code = 'USD', ), )
                    ],
                payments_received = [
                    procore_sdk.models.rest_v10_work_order_contracts_post_201_response_payments_issued_inner.RestV10WorkOrderContractsPost_201_response_payments_issued_inner(
                        id = 1551516, 
                        amount = '1000000.0', 
                        check_number = 'ABC93759372', 
                        created_at = '2015-07-14T22:03:27Z', 
                        date = 'Wed Jul 15 00:00:00 UTC 2015', 
                        draw_request_number = 5, 
                        invoice_number = 'Invoice 123', 
                        notes = 'January Payment', 
                        payment_number = 5, 
                        attachments = [
                            procore_sdk.models.rest_v10_work_order_contracts_post_201_response_attachments_inner.RestV10WorkOrderContractsPost_201_response_attachments_inner(
                                id = 5324, 
                                url = 'http://www.example.com/', 
                                filename = 'january_receipt_copy.jpg', )
                            ], 
                        origin_id = 'abc-123', 
                        origin_data = 'XYZ-0012', 
                        currency_configuration = procore_sdk.models.rest_v10_work_order_contracts_get_200_response_inner_currency_configuration.RestV10WorkOrderContractsGet_200_response_inner_currency_configuration(
                            currency_iso_code = 'USD', ), )
                    ],
                received_from = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                    id = 160586, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
                vendor = None,
                currency_configuration = procore_sdk.models.rest_v10_work_order_contracts_get_200_response_inner_currency_configuration.RestV10WorkOrderContractsGet_200_response_inner_currency_configuration(
                    currency_iso_code = 'USD', )
            )
        else:
            return RestV10PrimeContractGet200Response(
        )
        """

    def testRestV10PrimeContractGet200Response(self):
        """Test RestV10PrimeContractGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
