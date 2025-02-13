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

from procore_sdk.models.rest_v10_companies_company_id_projects_project_id_task_item_comments_post_request_task_item_comment import RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequestTaskItemComment

class TestRestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequestTaskItemComment(unittest.TestCase):
    """RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequestTaskItemComment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequestTaskItemComment:
        """Test RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequestTaskItemComment
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequestTaskItemComment`
        """
        model = RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequestTaskItemComment()
        if include_optional:
            return RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequestTaskItemComment(
                comment = 'Clean up area 4',
                status = 'in_progress',
                task_item_id = 731,
                attachments = [
                    ''
                    ],
                drawing_revision_ids = [4,5],
                file_version_ids = [6,7],
                form_ids = [7,8],
                image_ids = [9,10],
                upload_ids = ["4120226e-36a8-416f-970e-880bae78164f","de07e35a-4860-4f96-acd8-8360833dc495"]
            )
        else:
            return RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequestTaskItemComment(
                task_item_id = 731,
        )
        """

    def testRestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequestTaskItemComment(self):
        """Test RestV10CompaniesCompanyIdProjectsProjectIdTaskItemCommentsPostRequestTaskItemComment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
