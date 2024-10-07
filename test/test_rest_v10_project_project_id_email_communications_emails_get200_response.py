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

from procore_sdk.models.rest_v10_project_project_id_email_communications_emails_get200_response import RestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response

class TestRestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response(unittest.TestCase):
    """RestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response:
        """Test RestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response`
        """
        model = RestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response()
        if include_optional:
            return RestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response(
                emails = [
                    procore_sdk.models.rest_v10_project_project_id_email_communications_emails_get_200_response_emails_inner.RestV10ProjectProjectIdEmailCommunicationsEmailsGet_200_response_emails_inner(
                        id = 29, 
                        communication_id = 2, 
                        subject = 'subject of the email', 
                        private = True, 
                        attachments = [
                            procore_sdk.models.rest_v10_project_project_id_email_communications_emails_get_200_response_emails_inner_attachments_inner.RestV10ProjectProjectIdEmailCommunicationsEmailsGet_200_response_emails_inner_attachments_inner(
                                id = 123, 
                                name = 'Example', 
                                url = 'http://www.example.com/', )
                            ], 
                        bcc_distribution = [
                            procore_sdk.models.rest_v10_project_project_id_email_communications_id_get_200_response_emails_inner_bcc_distribution_inner.RestV10ProjectProjectIdEmailCommunicationsIdGet_200_response_emails_inner_bcc_distribution_inner(
                                id = 123, 
                                company_name = 'Some Company Name', 
                                locale = 'ko', 
                                login = 'person18@example.com', 
                                name = 'Paul Dou', 
                                avatar = 'http://s3.amazonaws.com/pro-core.com/prostore/20150713184222_production_74548228.gif?AWSAccessKeyId=0PFNH01C4MZVXKXZNK82&Expires=2067964943&Signature=l4zpZIM3bgxydrr4hn6lM%2FdtreQ%3D', 
                                initials = 'PD', )
                            ], 
                        body = 'Doe Construction', 
                        sanitized_body_html = '<p>Test email body</p>', 
                        cc_distribution = [
                            procore_sdk.models.rest_v10_project_project_id_email_communications_id_get_200_response_emails_inner_bcc_distribution_inner.RestV10ProjectProjectIdEmailCommunicationsIdGet_200_response_emails_inner_bcc_distribution_inner(
                                id = 123, 
                                company_name = 'Some Company Name', 
                                locale = 'ko', 
                                login = 'person18@example.com', 
                                name = 'Paul Dou', 
                                avatar = 'http://s3.amazonaws.com/pro-core.com/prostore/20150713184222_production_74548228.gif?AWSAccessKeyId=0PFNH01C4MZVXKXZNK82&Expires=2067964943&Signature=l4zpZIM3bgxydrr4hn6lM%2FdtreQ%3D', 
                                initials = 'PD', )
                            ], 
                        distribution = [
                            
                            ], 
                        email_sent_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        login_information = procore_sdk.models.rest_v10_project_project_id_email_communications_id_get_200_response_emails_inner_login_information.RestV10ProjectProjectIdEmailCommunicationsIdGet_200_response_emails_inner_login_information(
                            id = 123, 
                            company_name = 'Some Company Name', 
                            locale = 'ko', 
                            login = 'person18@example.com', 
                            name = 'Paul Dou', 
                            avatar = 'http://s3.amazonaws.com/pro-core.com/prostore/20150713184222_production_74548228.gif?AWSAccessKeyId=0PFNH01C4MZVXKXZNK82&Expires=2067964943&Signature=l4zpZIM3bgxydrr4hn6lM%2FdtreQ%3D', 
                            initials = 'PD', ), )
                    ],
                total = 12,
                new_communication_email = 'procore-inbound-email@example.com'
            )
        else:
            return RestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response(
        )
        """

    def testRestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response(self):
        """Test RestV10ProjectProjectIdEmailCommunicationsEmailsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
