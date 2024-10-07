# RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response

Response of a bulk action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successes** | **List[int]** | IDs that succeeded | [optional] 
**failures** | [**List[RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207ResponseFailuresInner]**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207ResponseFailuresInner.md) | List of failures | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete207_response import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response from a JSON string
rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete207_response_instance = RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response.to_json())

# convert the object into a dict
rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete207_response_dict = rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete207_response_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response from a dict
rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete207_response_from_dict = RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsBulkDestroyDelete207Response.from_dict(rest_v10_companies_company_id_work_breakdown_structure_segments_segment_id_segment_items_bulk_destroy_delete207_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


