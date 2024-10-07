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

from procore_sdk.models.bim_model_revision_viewpoint_batch_create_response_errors_inner import BIMModelRevisionViewpointBatchCreateResponseErrorsInner

class TestBIMModelRevisionViewpointBatchCreateResponseErrorsInner(unittest.TestCase):
    """BIMModelRevisionViewpointBatchCreateResponseErrorsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BIMModelRevisionViewpointBatchCreateResponseErrorsInner:
        """Test BIMModelRevisionViewpointBatchCreateResponseErrorsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BIMModelRevisionViewpointBatchCreateResponseErrorsInner`
        """
        model = BIMModelRevisionViewpointBatchCreateResponseErrorsInner()
        if include_optional:
            return BIMModelRevisionViewpointBatchCreateResponseErrorsInner(
                bim_model_revision_id = 91,
                bim_viewpoint_id = 83,
                primary = False,
                errors = procore_sdk.models.rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch_200_response_errors_inner_all_of_errors.RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch_200_response_errors_inner_allOf_errors(
                    field_name = [
                        ''
                        ], )
            )
        else:
            return BIMModelRevisionViewpointBatchCreateResponseErrorsInner(
                bim_model_revision_id = 91,
                bim_viewpoint_id = 83,
        )
        """

    def testBIMModelRevisionViewpointBatchCreateResponseErrorsInner(self):
        """Test BIMModelRevisionViewpointBatchCreateResponseErrorsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
