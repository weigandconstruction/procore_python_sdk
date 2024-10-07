# RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**code** | **str** | Code | [optional] 
**name** | **str** | Name | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**parent_id** | **int** | Parent ID | [optional] 
**path_ids** | **List[int]** | Path variable IDs | [optional] 
**path_code** | **str** | Path Variable Code | [optional] 
**is_parent** | **bool** |  | [optional] 
**path_codes** | **List[str]** | Path variable codes | [optional] 
**path_names** | **List[str]** | Path variable names | [optional] 
**in_use** | **bool** | Whether or not this item is tagged on an entity | [optional] 
**segment** | [**RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInnerSegment**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInnerSegment.md) |  | [optional] 
**status** | **str** | Segment item status | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get200_response_inner import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner from a JSON string
rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get200_response_inner_instance = RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get200_response_inner_dict = rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner from a dict
rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get200_response_inner_from_dict = RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner.from_dict(rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


