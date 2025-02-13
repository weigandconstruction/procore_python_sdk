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

from procore_sdk.models.rest_v11_projects_project_id_schedule_requested_changes_review_patch200_response_inner import RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner

class TestRestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner(unittest.TestCase):
    """RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner:
        """Test RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner`
        """
        model = RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner()
        if include_optional:
            return RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner(
                id = 333713,
                requested_by = 'Bob Dole on Nov. 24',
                change_requested = '<ul><li>Other change: why7</li></ul>',
                reason = '<p>this is a description</p>',
                status = 'Pending',
                status_not_localized = 'pending',
                notes = 'Notes'
            )
        else:
            return RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner(
        )
        """

    def testRestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner(self):
        """Test RestV11ProjectsProjectIdScheduleRequestedChangesReviewPatch200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
