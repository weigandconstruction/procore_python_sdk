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

from procore_sdk.models.rest_v10_companies_company_id_meeting_templates_get200_response_inner_agendas_inner_attachments_inner import RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAgendasInnerAttachmentsInner

class TestRestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAgendasInnerAttachmentsInner(unittest.TestCase):
    """RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAgendasInnerAttachmentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAgendasInnerAttachmentsInner:
        """Test RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAgendasInnerAttachmentsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAgendasInnerAttachmentsInner`
        """
        model = RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAgendasInnerAttachmentsInner()
        if include_optional:
            return RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAgendasInnerAttachmentsInner(
                name = 'agenda.pdf',
                url = 'https://binder-staging1.procoretech-qa.com/v4/d/us-east-1/pro-core.com/prostore/20230208201914_test_95.pdf?sig=4019988aeaadc6196dc497045e5e349848be4f8b139f1cc33916ac9f380a8a1e'
            )
        else:
            return RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAgendasInnerAttachmentsInner(
        )
        """

    def testRestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAgendasInnerAttachmentsInner(self):
        """Test RestV10CompaniesCompanyIdMeetingTemplatesGet200ResponseInnerAgendasInnerAttachmentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
