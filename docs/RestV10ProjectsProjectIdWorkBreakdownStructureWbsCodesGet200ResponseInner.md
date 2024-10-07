# RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner

A work breakdown structure code

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the Work Breakdown Structure code. | [optional] 
**flat_code** | **str** | The Work Breakdown Structure code made up of segment values, concatenated by the set delimiter | [optional] 
**flat_name** | **str** | The names of the Work Breakdown Structure segments concatenated by the specified with the company&#39;s delimiter and WBS pattern | [optional] 
**description** | **str** | The description of the Work Breakdown Structure code | [optional] 
**status** | **str** | The status of the WBS Code | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**segment_items** | [**List[RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner]**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner.md) |  | [optional] 
**wbs_pattern_id** | **int** | The ID of the WBS Pattern used for a Work Breakdown Structure code | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_get200_response_inner import RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner from a JSON string
rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_get200_response_inner_instance = RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_get200_response_inner_dict = rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner from a dict
rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_get200_response_inner_from_dict = RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesGet200ResponseInner.from_dict(rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


