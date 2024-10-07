# RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdListsGet200ResponseInner

A work breakdown structure pattern

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Segment item list name | [optional] 
**segment_items_count** | **int** | Number of segment items in the list | [optional] 
**erp_integrated** | **bool** | Whether or not the list is ERP integrated | [optional] 
**available_to_use_on_new_projects** | **bool** | Whether or not the list can be use on new projects | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_lists_get200_response_inner import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdListsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdListsGet200ResponseInner from a JSON string
rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_lists_get200_response_inner_instance = RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdListsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdListsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_lists_get200_response_inner_dict = rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_lists_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdListsGet200ResponseInner from a dict
rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_lists_get200_response_inner_from_dict = RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdListsGet200ResponseInner.from_dict(rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_lists_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


