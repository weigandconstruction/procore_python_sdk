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

from procore_sdk.models.rest_v20_companies_company_id_inspection_template_items_template_item_id_evidence_configuration_patch_request import RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequest

class TestRestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequest(unittest.TestCase):
    """RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequest:
        """Test RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequest`
        """
        model = RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequest()
        if include_optional:
            return RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequest(
                evidence_configuration = procore_sdk.models.rest_v20_companies_company_id_inspection_template_items_template_item_id_evidence_configuration_patch_request_evidence_configuration.RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatch_request_evidence_configuration(
                    observation = procore_sdk.models.rest_v20_companies_company_id_inspection_template_items_template_item_id_evidence_configuration_patch_request_evidence_configuration_observation.RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatch_request_evidence_configuration_observation(
                        status_ids = [
                            '1'
                            ], 
                        response_option_ids = [
                            '31'
                            ], ), 
                    photo = procore_sdk.models.rest_v20_companies_company_id_inspection_template_items_template_item_id_evidence_configuration_patch_request_evidence_configuration_photo.RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatch_request_evidence_configuration_photo(), )
            )
        else:
            return RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequest(
                evidence_configuration = procore_sdk.models.rest_v20_companies_company_id_inspection_template_items_template_item_id_evidence_configuration_patch_request_evidence_configuration.RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatch_request_evidence_configuration(
                    observation = procore_sdk.models.rest_v20_companies_company_id_inspection_template_items_template_item_id_evidence_configuration_patch_request_evidence_configuration_observation.RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatch_request_evidence_configuration_observation(
                        status_ids = [
                            '1'
                            ], 
                        response_option_ids = [
                            '31'
                            ], ), 
                    photo = procore_sdk.models.rest_v20_companies_company_id_inspection_template_items_template_item_id_evidence_configuration_patch_request_evidence_configuration_photo.RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatch_request_evidence_configuration_photo(), ),
        )
        """

    def testRestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequest(self):
        """Test RestV20CompaniesCompanyIdInspectionTemplateItemsTemplateItemIdEvidenceConfigurationPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
