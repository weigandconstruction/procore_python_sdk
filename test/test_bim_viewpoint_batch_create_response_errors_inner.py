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

from procore_sdk.models.bim_viewpoint_batch_create_response_errors_inner import BIMViewpointBatchCreateResponseErrorsInner

class TestBIMViewpointBatchCreateResponseErrorsInner(unittest.TestCase):
    """BIMViewpointBatchCreateResponseErrorsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BIMViewpointBatchCreateResponseErrorsInner:
        """Test BIMViewpointBatchCreateResponseErrorsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BIMViewpointBatchCreateResponseErrorsInner`
        """
        model = BIMViewpointBatchCreateResponseErrorsInner()
        if include_optional:
            return BIMViewpointBatchCreateResponseErrorsInner(
                bim_file_id = 56,
                name = 'Ceiling view',
                view_folder_id = 56,
                upload_uuid = '1ZE146W9K804SAJJZX19JVAD0R',
                camera_data = '{"Type":"Camera","Scale":1,"Up":[0,0,1],"Front":[0,1,2.22],"Right":[1,0,0],"Position":[36.48,22.38,68.27],"View":[-0.11,-0.14,-0.98]}',
                redlines_data = '{"Type":"RedlineCollection","Values":[{"Type":"RedlineEllipse","Thickness":3,"Color":[1,0,0],"MinPoint":[-0.131,0.202],"MaxPoint":[0.144,0.024]}]}',
                sections_data = '{"Type":"ClipPlaneSet","Version":1"}',
                errors = procore_sdk.models.rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch_200_response_errors_inner_all_of_errors.RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch_200_response_errors_inner_allOf_errors(
                    field_name = [
                        ''
                        ], )
            )
        else:
            return BIMViewpointBatchCreateResponseErrorsInner(
                bim_file_id = 56,
                upload_uuid = '1ZE146W9K804SAJJZX19JVAD0R',
                camera_data = '{"Type":"Camera","Scale":1,"Up":[0,0,1],"Front":[0,1,2.22],"Right":[1,0,0],"Position":[36.48,22.38,68.27],"View":[-0.11,-0.14,-0.98]}',
        )
        """

    def testBIMViewpointBatchCreateResponseErrorsInner(self):
        """Test BIMViewpointBatchCreateResponseErrorsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
