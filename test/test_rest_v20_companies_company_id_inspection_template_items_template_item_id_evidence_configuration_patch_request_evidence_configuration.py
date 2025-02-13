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

from procore_sdk.models.rest_v20_companies_company_id_inspection_template_items_template_item_id_evidence_configuration_patch_request_evidence_configuration import RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration

class TestRestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration(unittest.TestCase):
    """RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration:
        """Test RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration`
        """
        model = RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration()
        if include_optional:
            return RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration(
                observation = procore_sdk.models.rest_v20_companies_company_id_inspection_template_items_template_item_id_evidence_configuration_patch_request_evidence_configuration_observation.RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatch_request_evidence_configuration_observation(
                    status_ids = [
                        '1'
                        ], 
                    response_option_ids = [
                        '31'
                        ], ),
                photo = procore_sdk.models.rest_v20_companies_company_id_inspection_template_items_template_item_id_evidence_configuration_patch_request_evidence_configuration_photo.RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatch_request_evidence_configuration_photo(
                    status_ids = [
                        '2'
                        ], 
                    response_option_ids = [
                        '23'
                        ], )
            )
        else:
            return RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration(
        )
        """

    def testRestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration(self):
        """Test RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
