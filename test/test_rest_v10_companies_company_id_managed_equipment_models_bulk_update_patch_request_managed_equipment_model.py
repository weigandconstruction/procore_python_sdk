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

from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_models_bulk_update_patch_request_managed_equipment_model import RestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequestManagedEquipmentModel

class TestRestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequestManagedEquipmentModel(unittest.TestCase):
    """RestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequestManagedEquipmentModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequestManagedEquipmentModel:
        """Test RestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequestManagedEquipmentModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequestManagedEquipmentModel`
        """
        model = RestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequestManagedEquipmentModel()
        if include_optional:
            return RestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequestManagedEquipmentModel(
                is_active = True,
                managed_equipment_make_id = 533,
                managed_equipment_type_id = 533
            )
        else:
            return RestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequestManagedEquipmentModel(
        )
        """

    def testRestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequestManagedEquipmentModel(self):
        """Test RestV10CompaniesCompanyIdManagedEquipmentModelsBulkUpdatePatchRequestManagedEquipmentModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
