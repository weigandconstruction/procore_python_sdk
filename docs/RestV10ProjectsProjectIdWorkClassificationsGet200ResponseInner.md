# RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner

Work Classification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | The name of the classification | [optional] 
**abbreviation** | **str** | The shortened form of classification | [optional] 
**company_id** | **int** | The comapny ID the classification was created with | [optional] 
**company_visible** | **bool** | Is the classification visible as a company classification | [optional] 
**updated_at** | **datetime** | Date the classification was updated | [optional] 
**created_at** | **datetime** | Date the classification was created | [optional] 
**created_by_id** | **int** | The user ID the classification was created with | [optional] 
**project_ids** | **List[int]** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_work_classifications_get200_response_inner import RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_work_classifications_get200_response_inner_instance = RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_work_classifications_get200_response_inner_dict = rest_v10_projects_project_id_work_classifications_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner from a dict
rest_v10_projects_project_id_work_classifications_get200_response_inner_from_dict = RestV10ProjectsProjectIdWorkClassificationsGet200ResponseInner.from_dict(rest_v10_projects_project_id_work_classifications_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


