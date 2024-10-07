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

from procore_sdk.models.time_and_material_notification import TimeAndMaterialNotification

class TestTimeAndMaterialNotification(unittest.TestCase):
    """TimeAndMaterialNotification unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeAndMaterialNotification:
        """Test TimeAndMaterialNotification
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeAndMaterialNotification`
        """
        model = TimeAndMaterialNotification()
        if include_optional:
            return TimeAndMaterialNotification(
                creation = [
                    95861
                    ],
                customer_signed = [
                    95861
                    ],
                company_signed = [
                    95861
                    ],
                closed = [
                    95861
                    ],
                group_equipment_totals_by = 'per_ticket',
                notify_dl_on_customer_signed = True,
                notify_dl_on_company_signed = True,
                notify_dl_on_creation = True,
                notify_dl_on_closed = True,
                group_labor_totals_by = 'per_ticket'
            )
        else:
            return TimeAndMaterialNotification(
        )
        """

    def testTimeAndMaterialNotification(self):
        """Test TimeAndMaterialNotification"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
