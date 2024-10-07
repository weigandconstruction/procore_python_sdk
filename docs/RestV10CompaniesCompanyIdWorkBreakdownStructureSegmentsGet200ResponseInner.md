# RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsGet200ResponseInner

A work breakdown structure segment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**type** | **str** | The type of Wbs Segment. | [optional] 
**name** | **str** | The i18n display name of the Wbs Segment. | [optional] 
**position** | **int** | Position of the Wbs Segment according to the Company Wbs Pattern. | [optional] 
**segment_items_count** | **int** | Number of items that belong to this segment | [optional] 
**required** | **bool** | Whether this Wbs Segment is required. | [optional] 
**delimiter** | **str** | The delimiter between this Wbs Segment and the subsequent Wbs Segment. | [optional] 
**project_can_modify_origin_project** | **bool** | Whether project-specific Segment Items are able to be added to a Project. | [optional] 
**project_can_delete_origin_company** | **bool** | Whether Segment Items inherited from the company-level are able to be deleted from a Project. | [optional] 
**structure** | **str** | The Structure for this Wbs Segment. | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**wbs_pattern_id** | **int** | ID of the associated WBS Pattern | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_work_breakdown_structure_segments_get200_response_inner import RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsGet200ResponseInner from a JSON string
rest_v10_companies_company_id_work_breakdown_structure_segments_get200_response_inner_instance = RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_work_breakdown_structure_segments_get200_response_inner_dict = rest_v10_companies_company_id_work_breakdown_structure_segments_get200_response_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsGet200ResponseInner from a dict
rest_v10_companies_company_id_work_breakdown_structure_segments_get200_response_inner_from_dict = RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsGet200ResponseInner.from_dict(rest_v10_companies_company_id_work_breakdown_structure_segments_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


