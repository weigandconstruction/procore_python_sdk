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

from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_patch_request_evidence_configuration import RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration

class TestRestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration(unittest.TestCase):
    """RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration:
        """Test RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration`
        """
        model = RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration()
        if include_optional:
            return RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration(
                observation = procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_patch_request_evidence_configuration_observation.RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatch_request_evidence_configuration_observation(
                    status_ids = [
                        '1'
                        ], 
                    response_option_ids = [
                        '31'
                        ], ),
                photo = procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_patch_request_evidence_configuration_photo.RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatch_request_evidence_configuration_photo(
                    status_ids = [
                        '2'
                        ], 
                    response_option_ids = [
                        '23'
                        ], )
            )
        else:
            return RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration(
        )
        """

    def testRestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration(self):
        """Test RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequestEvidenceConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
