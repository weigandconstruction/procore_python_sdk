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

from procore_sdk.models.rest_v10_companies_company_id_managed_equipment_logs_post_request import RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest

class TestRestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest(unittest.TestCase):
    """RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest:
        """Test RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest`
        """
        model = RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest()
        if include_optional:
            return RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest(
                managed_equipment_log = procore_sdk.models.rest_v10_companies_company_id_managed_equipment_logs_post_request_managed_equipment_log.RestV10CompaniesCompanyIdManagedEquipmentLogsPost_request_managed_equipment_log(
                    project_id = 14406, 
                    managed_equipment_id = 1, 
                    onsite = 'Wed Apr 10 00:00:00 UTC 2019', 
                    offsite = 'Fri May 10 00:00:00 UTC 2019', 
                    inspection_date = 'Wed Apr 10 00:00:00 UTC 2019', 
                    induction_checklist_list_id = 1, 
                    induction_number = '00001', 
                    induction_status = False, )
            )
        else:
            return RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest(
                managed_equipment_log = procore_sdk.models.rest_v10_companies_company_id_managed_equipment_logs_post_request_managed_equipment_log.RestV10CompaniesCompanyIdManagedEquipmentLogsPost_request_managed_equipment_log(
                    project_id = 14406, 
                    managed_equipment_id = 1, 
                    onsite = 'Wed Apr 10 00:00:00 UTC 2019', 
                    offsite = 'Fri May 10 00:00:00 UTC 2019', 
                    inspection_date = 'Wed Apr 10 00:00:00 UTC 2019', 
                    induction_checklist_list_id = 1, 
                    induction_number = '00001', 
                    induction_status = False, ),
        )
        """

    def testRestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest(self):
        """Test RestV10CompaniesCompanyIdManagedEquipmentLogsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
