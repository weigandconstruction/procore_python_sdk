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

from procore_sdk.models.body20 import Body20

class TestBody20(unittest.TestCase):
    """Body20 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Body20:
        """Test Body20
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Body20`
        """
        model = Body20()
        if include_optional:
            return Body20(
                project_id = 55001,
                commitment_id = 66005,
                requisition = procore_sdk.models.requisition_(subcontractor_invoice).Requisition (Subcontractor Invoice)(
                    items = [
                        procore_sdk.models.requisition__subcontractor_invoice__1_items_inner.Requisition__Subcontractor_Invoice__1_items_inner(
                            id = 1001, 
                            line_item_id = 1001, 
                            detail_line_item_id = 1001, 
                            item_type = 'contract_detail_item', 
                            work_completed_this_period = '1000', 
                            materials_presently_stored = '500', 
                            materials_presently_stored_from_previous_progress = '250', 
                            new_materials = '0.00', 
                            stored_materials = '0.00', 
                            work_completed_retainage_retained_this_period = '100', 
                            materials_stored_retainage_currently_retained = '50', 
                            work_completed_retainage_released_this_period = '0', 
                            work_completed_this_period_quantity = '10', 
                            work_completed_retainage_percent_this_period = '10', 
                            materials_stored_retainage_percent_this_period = '10', 
                            subcontractor_claimed_amount = '20.5', 
                            status = 'rejected', 
                            comment = 'This work was not yet completed', )
                        ], 
                    period_id = 20093, 
                    requisition_start = 'Tue Oct 01 00:00:00 UTC 2013', 
                    requisition_end = 'Thu Oct 31 00:00:00 UTC 2013', 
                    billing_date = 'Thu Oct 31 00:00:00 UTC 2013', 
                    final = True, 
                    invoice_number = 'ABC-1234', 
                    payment_date = 'Fri Nov 15 00:00:00 UTC 2013', 
                    origin_data = 'XYZ-0012', 
                    origin_id = 'abc-123', 
                    status = 'under_review', 
                    submitted_at = 'Sat Nov 02 00:00:00 UTC 2013', 
                    prostore_file_ids = [42], 
                    custom_field_%{custom_field_definition_id} = custom field value, )
            )
        else:
            return Body20(
                project_id = 55001,
                commitment_id = 66005,
        )
        """

    def testBody20(self):
        """Test Body20"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
