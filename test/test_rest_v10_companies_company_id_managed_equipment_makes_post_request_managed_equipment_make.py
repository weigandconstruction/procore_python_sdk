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

from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_makes_post_request_managed_equipment_make import RestV10CompaniesCompanyIdManagedEquipmentMakesPostRequestManagedEquipmentMake

class TestRestV10CompaniesCompanyIdManagedEquipmentMakesPostRequestManagedEquipmentMake(unittest.TestCase):
    """RestV10CompaniesCompanyIdManagedEquipmentMakesPostRequestManagedEquipmentMake unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdManagedEquipmentMakesPostRequestManagedEquipmentMake:
        """Test RestV10CompaniesCompanyIdManagedEquipmentMakesPostRequestManagedEquipmentMake
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdManagedEquipmentMakesPostRequestManagedEquipmentMake`
        """
        model = RestV10CompaniesCompanyIdManagedEquipmentMakesPostRequestManagedEquipmentMake()
        if include_optional:
            return RestV10CompaniesCompanyIdManagedEquipmentMakesPostRequestManagedEquipmentMake(
                name = 'CAT',
                is_active = True
            )
        else:
            return RestV10CompaniesCompanyIdManagedEquipmentMakesPostRequestManagedEquipmentMake(
                name = 'CAT',
                is_active = True,
        )
        """

    def testRestV10CompaniesCompanyIdManagedEquipmentMakesPostRequestManagedEquipmentMake(self):
        """Test RestV10CompaniesCompanyIdManagedEquipmentMakesPostRequestManagedEquipmentMake"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
