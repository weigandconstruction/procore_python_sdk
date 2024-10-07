# RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | List of segment item IDs. The API will find and update the children of the provided IDs. | 
**attributes** | [**RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequestAttributes**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequestAttributes.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch_request import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest from a JSON string
rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch_request_instance = RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest.to_json())

# convert the object into a dict
rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch_request_dict = rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch_request_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest from a dict
rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch_request_from_dict = RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsUpdateAllPatchRequest.from_dict(rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_update_all_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


