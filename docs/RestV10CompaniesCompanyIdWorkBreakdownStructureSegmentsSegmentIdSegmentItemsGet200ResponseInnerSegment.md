# RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInnerSegment

Segment attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**position** | **int** |  | [optional] 
**delimiter** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**segment_items_count** | **int** |  | [optional] 
**project_can_modify_origin_project** | **bool** |  | [optional] 
**project_can_delete_origin_company** | **bool** |  | [optional] 
**structure** | **str** |  | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**wbs_pattern_id** | **int** | ID of the associated WBS Pattern | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get200_response_inner_segment import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInnerSegment

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInnerSegment from a JSON string
rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get200_response_inner_segment_instance = RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInnerSegment.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInnerSegment.to_json())

# convert the object into a dict
rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get200_response_inner_segment_dict = rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get200_response_inner_segment_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInnerSegment from a dict
rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get200_response_inner_segment_from_dict = RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInnerSegment.from_dict(rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_get200_response_inner_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


