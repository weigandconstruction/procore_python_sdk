# RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Drawing Discipline ID | [optional] 
**name** | **str** | Drawing Discipline name | [optional] 
**position** | **int** | Position of the discipline in the drawing log | [optional] 
**abbreviations** | **List[str]** | List of discipline abbreviations | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_drawing_disciplines_get200_response_inner import RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner from a JSON string
rest_v11_projects_project_id_drawing_disciplines_get200_response_inner_instance = RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v11_projects_project_id_drawing_disciplines_get200_response_inner_dict = rest_v11_projects_project_id_drawing_disciplines_get200_response_inner_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner from a dict
rest_v11_projects_project_id_drawing_disciplines_get200_response_inner_from_dict = RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner.from_dict(rest_v11_projects_project_id_drawing_disciplines_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


