# RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the wbs code. | [optional] 
**segment_items** | [**List[RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesPostRequestSegmentItemsInner]**](RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesPostRequestSegmentItemsInner.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_post_request import RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesPostRequest from a JSON string
rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_post_request_instance = RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesPostRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_post_request_dict = rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_post_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesPostRequest from a dict
rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_post_request_from_dict = RestV10ProjectsProjectIdWorkBreakdownStructureWbsCodesPostRequest.from_dict(rest_v10_projects_project_id_work_breakdown_structure_wbs_codes_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


