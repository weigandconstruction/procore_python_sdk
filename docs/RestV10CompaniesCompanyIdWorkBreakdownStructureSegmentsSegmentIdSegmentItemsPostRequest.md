# RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Segment Item Code | 
**name** | **str** | Segment Item Name | 
**segment_item_list_id** | **int** | Segment Item List ID | [optional] 
**parent_id** | **int** | Parent ID | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_post_request import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest from a JSON string
rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_post_request_instance = RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest.to_json())

# convert the object into a dict
rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_post_request_dict = rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_post_request_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest from a dict
rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_post_request_from_dict = RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest.from_dict(rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


