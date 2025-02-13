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

from procore_sdk.models.body104_coordination_issue import Body104CoordinationIssue

class TestBody104CoordinationIssue(unittest.TestCase):
    """Body104CoordinationIssue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Body104CoordinationIssue:
        """Test Body104CoordinationIssue
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Body104CoordinationIssue`
        """
        model = Body104CoordinationIssue()
        if include_optional:
            return Body104CoordinationIssue(
                uuid = '0b1a32a7-9cf4-4e53-bef4-3d70201b709a',
                title = 'Plumbing Issue on second floor',
                description = 'Plumbing conflicts with light fixtures',
                status = 'open',
                creation_source = 'navisworks',
                location_id = 5,
                assignee_id = 624,
                coordination_issue_file_id = 8,
                drawing_revision_id = 9,
                bim_model_id = 19,
                due_date = '2018-08-16',
                issue_type = 'building_code',
                priority = 'high',
                trade_id = 999,
                origin = procore_sdk.models.body_104_coordination_issue_origin.Body_104_coordination_issue_origin(
                    title = 'My BcfTopic', 
                    origin_id = '7b3c8752-e03e-417f-bb57-46bb5aca1139', 
                    origin_type = 'BcfTopic', 
                    deep_link_url = 'https://some-company.com/bcf-topics/156', ),
                attachment_upload_uuids = [
                    '1ZE258W9K804SAJJZX19JVAB3R'
                    ],
                attachments = [
                    ''
                    ],
                viewpoints = [
                    procore_sdk.models.body_104_coordination_issue_viewpoints_inner.Body_104_coordination_issue_viewpoints_inner(
                        name = 'Ceiling view', 
                        view_folder_id = 56, 
                        snapshot_upload_uuid = '1ZE146W9K804SAJJZX19JVAD0R', 
                        camera_data = '{"perspective_camera":{"camera_direction":{"x":-0.24,"y":-0.14,"z":-0.99},"camera_up_vector":{"x":-0.17,"y":-0.74,"z":0.14},"camera_view_point":{"x":-13.86,"y":64.83,"z":31.9},"field_of_view":0.78,"target_distance":9.18,"unit":"ft"}}', 
                        redlines_data = '{"lines":[{"color":{"a":1.0,"b":0,"g":0,"r":1},"end_point":{"x":-0.29,"y":-0.15,"z":0.0},"thickness":3,"start_point":{"x":-0.29,"y":-0.53,"z":0.0}}],"texts":[{"origin":{"x":-0.29,"y":-0.15,"z":0.0},"text":"Issue","color":{"a":1.0,"b":0,"g":0,"r":1}}],"arrows":[{"color":{"a":1.0,"b":0,"g":0,"r":1},"end_point":{"x":-0.16,"y":0.33,"z":0.0},"thickness":3,"start_point":{"x":0.58,"y":0.25,"z":0.0}}],"ellipses":[{"color":{"a":1.0,"b":0,"g":0,"r":1},"max_point":{"x":0.11,"y":-0.25,"z":0.0},"min_point":{"x":0.31,"y":0.68,"z":0.0},"thickness":3}]}', 
                        sections_data = '{"min_boundary":{"x":6.24,"y":12.48,"z":24.96},"max_boundary":{"x":12.48,"y":24.96,"z":48.12},"rotation":{"x":1.0,"y":0.0,"z":2.0}}', 
                        render_mode = 'shaded', 
                        visibility = procore_sdk.models.body_104_coordination_issue_viewpoints_inner_visibility.Body_104_coordination_issue_viewpoints_inner_visibility(
                            default_visibility = True, 
                            exceptions = procore_sdk.models.rest_v10_coordination_issues_get_200_response_inner_all_of_viewpoints_inner_all_of_visibility_exceptions.RestV10CoordinationIssuesGet_200_response_inner_allOf_viewpoints_inner_allOf_visibility_exceptions(
                                object_ids = [24861,46732], 
                                object_ranges = [[24862,24]], ), ), )
                    ]
            )
        else:
            return Body104CoordinationIssue(
                title = 'Plumbing Issue on second floor',
        )
        """

    def testBody104CoordinationIssue(self):
        """Test Body104CoordinationIssue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
