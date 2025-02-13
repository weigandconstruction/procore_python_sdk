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

from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_types_post_request_managed_equipment_type import RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequestManagedEquipmentType

class TestRestV10CompaniesCompanyIdManagedEquipmentTypesPostRequestManagedEquipmentType(unittest.TestCase):
    """RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequestManagedEquipmentType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequestManagedEquipmentType:
        """Test RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequestManagedEquipmentType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequestManagedEquipmentType`
        """
        model = RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequestManagedEquipmentType()
        if include_optional:
            return RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequestManagedEquipmentType(
                name = 'Backhoe',
                managed_equipment_category_id = 3355,
                is_active = True
            )
        else:
            return RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequestManagedEquipmentType(
                name = 'Backhoe',
                managed_equipment_category_id = 3355,
        )
        """

    def testRestV10CompaniesCompanyIdManagedEquipmentTypesPostRequestManagedEquipmentType(self):
        """Test RestV10CompaniesCompanyIdManagedEquipmentTypesPostRequestManagedEquipmentType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
