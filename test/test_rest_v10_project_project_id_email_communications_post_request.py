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

from procore_sdk.models.rest_v10_project_project_id_email_communications_post_request import RestV10ProjectProjectIdEmailCommunicationsPostRequest

class TestRestV10ProjectProjectIdEmailCommunicationsPostRequest(unittest.TestCase):
    """RestV10ProjectProjectIdEmailCommunicationsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectProjectIdEmailCommunicationsPostRequest:
        """Test RestV10ProjectProjectIdEmailCommunicationsPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectProjectIdEmailCommunicationsPostRequest`
        """
        model = RestV10ProjectProjectIdEmailCommunicationsPostRequest()
        if include_optional:
            return RestV10ProjectProjectIdEmailCommunicationsPostRequest(
                communication = procore_sdk.models.rest_v10_project_project_id_email_communications_post_request_communication.RestV10ProjectProjectIdEmailCommunicationsPost_request_communication(
                    subject = '', ),
                email = procore_sdk.models.rest_v10_project_project_id_email_communications_post_request_email.RestV10ProjectProjectIdEmailCommunicationsPost_request_email(
                    body = '', 
                    prostore_file_ids = [
                        56
                        ], 
                    drawing_revision_ids = [
                        56
                        ], 
                    file_version_ids = [
                        56
                        ], 
                    form_ids = [
                        56
                        ], 
                    image_ids = [
                        56
                        ], 
                    upload_ids = [
                        '["01HZB4TFFBZWDQ92N3RJFM5J2Z","01HZB4TFERXDDQ354NTB09GEA6"]'
                        ], 
                    distribution_ids = [
                        56
                        ], 
                    cc_distribution_ids = [
                        56
                        ], 
                    bcc_distribution_ids = [
                        56
                        ], )
            )
        else:
            return RestV10ProjectProjectIdEmailCommunicationsPostRequest(
                communication = procore_sdk.models.rest_v10_project_project_id_email_communications_post_request_communication.RestV10ProjectProjectIdEmailCommunicationsPost_request_communication(
                    subject = '', ),
                email = procore_sdk.models.rest_v10_project_project_id_email_communications_post_request_email.RestV10ProjectProjectIdEmailCommunicationsPost_request_email(
                    body = '', 
                    prostore_file_ids = [
                        56
                        ], 
                    drawing_revision_ids = [
                        56
                        ], 
                    file_version_ids = [
                        56
                        ], 
                    form_ids = [
                        56
                        ], 
                    image_ids = [
                        56
                        ], 
                    upload_ids = [
                        '["01HZB4TFFBZWDQ92N3RJFM5J2Z","01HZB4TFERXDDQ354NTB09GEA6"]'
                        ], 
                    distribution_ids = [
                        56
                        ], 
                    cc_distribution_ids = [
                        56
                        ], 
                    bcc_distribution_ids = [
                        56
                        ], ),
        )
        """

    def testRestV10ProjectProjectIdEmailCommunicationsPostRequest(self):
        """Test RestV10ProjectProjectIdEmailCommunicationsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
