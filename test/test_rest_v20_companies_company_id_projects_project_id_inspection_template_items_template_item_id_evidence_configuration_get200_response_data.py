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

from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get200_response_data import RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseData

class TestRestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseData(unittest.TestCase):
    """RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseData:
        """Test RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseData`
        """
        model = RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseData()
        if include_optional:
            return RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseData(
                item_id = '44',
                photo = procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get_200_response_data_photo.RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet_200_response_data_photo(
                    status_ids = [
                        '2'
                        ], 
                    response_option_ids = [
                        '23'
                        ], ),
                observation = procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_template_items_template_item_id_evidence_configuration_get_200_response_data_observation.RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet_200_response_data_observation(
                    status_ids = [
                        '1'
                        ], 
                    response_option_ids = [
                        '31'
                        ], ),
                is_editable = True,
                created_at = '2012-10-23T21:39:40Z',
                updated_at = '2012-10-23T21:39:40Z'
            )
        else:
            return RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseData(
        )
        """

    def testRestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseData(self):
        """Test RestV20CompaniesCompanyIdProjectsProjectIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationGet200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
